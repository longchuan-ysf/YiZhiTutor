from django.shortcuts import render, redirect

# Create your views here.

from django.utils.decorators import method_decorator
from django.views import View

import application.menu.services
from application.index import services
from application.user.models import User
from config.env import DEBUG
from middleware.login_middleware import check_login
from utils import R

from utils.utils import getImageURL


# 渲染主页
@method_decorator(check_login, name='get')
class IndexView(View):
    # 接收GET请求并渲染HTML
    def get(self, request):
        # 获取用户信息
        user_id = request.session.get('user_id')
        userInfo = User.objects.filter(is_delete=False, id=user_id).first()
        print(userInfo.avatar)
        # 头像
        userInfo.avatar = getImageURL(userInfo.avatar)
        # 获取菜单列表
        menuList = application.menu.services.GetPermissionMenuList(user_id)
        # 模板参数
        content = {
            'userInfo': userInfo,
            'menuList': menuList,
        }
        # 使用render渲染方式
        return render(request, 'index.html', content)


# 欢迎页
@method_decorator(check_login, name='get')
class MainView(View):
    # 接收GET请求并渲染HTML
    def get(self, request):
        # 使用render渲染方式
        return render(request, 'main.html')


# 个人中心
@method_decorator(check_login, name='dispatch')
class UserInfoView(View):
    # 接收GET请求并渲染HTML
    def get(self, request):
        # 用户ID
        user_id = request.session.get('user_id')
        # 获取当前用户信息
        user = User.objects.filter(is_delete=False, id=user_id).first()
        # 用户头像
        user.avatar = getImageURL(user.avatar)
        # 模板参数
        content = {
            'user': user,
        }
        # 使用render渲染方式
        return render(request, 'user_info/index.html', content)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 用户ID
        user_id = request.session.get('user_id')
        # 调用更新用户服务方法
        result = services.UserInfo(request, user_id)
        # 返回结果
        return result


# 更新密码
@method_decorator(check_login, name='dispatch')
class UpdatePwdView(View):
    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 用户ID
        user_id = request.session.get('user_id')
        # 调用更新用户服务方法
        result = services.UpdatePwd(request, user_id)
        # 返回结果
        return result


# 退出登录
@method_decorator(check_login, name='dispatch')
class LogoutView(View):
    # 接收GET请求并渲染HTML
    def get(self, request):
        # 清空SESSION
        request.session.clear()
        # 判断KEY是否存在
        if request.session.exists('user_id'):
            # 删除指定KEY
            del request.session['user_id']
        # 重定向到登录页
        return redirect('/login')
