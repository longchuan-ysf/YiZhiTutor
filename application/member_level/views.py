from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.member_level import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染会员等级首页
from utils import R


# 会员等级首页
@method_decorator(check_login, name="get")
class MemberLevelView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:memberlevel:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染模板
        return render(request, "member_level/index.html")


# 查询会员等级分页数据
@method_decorator(check_login, name="get")
class MemberLevelListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:memberlevel:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询会员等级分页数据方法
        result = services.MemberLevelList(request)
        # 返回结果
        return result


# 查询会员等级详情
@method_decorator(check_login, name="get")
class MemberLevelDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:memberlevel:detail",)

    # GET请求渲染HTML模板
    def get(self, request, member_level_id):
        # 调用查询会员等级详情服务方法
        data = services.MemberLevelDetail(member_level_id)
        # 模板参数
        content = {
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "member_level/edit.html", content)


# 添加会员等级
@method_decorator(check_login, name="post")
class MemberLevelAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:memberlevel:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加会员等级服务方法
        result = services.MemberLevelAdd(request)
        # 返回结果
        return result


# 更新会员等级
@method_decorator(check_login, name="put")
class MemberLevelUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:memberlevel:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新会员等级服务方法
        result = services.MemberLevelUpdate(request)
        # 返回结果
        return result


# 删除会员等级
@method_decorator(check_login, name="delete")
class MemberLevelDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:memberlevel:delete',)

    # 接收DELETE请求
    def delete(self, request, member_level_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除会员等级服务方法
        result = services.MemberLevelDelete(member_level_id)
        # 返回结果
        return result
