from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.dict import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染字典首页
from utils import R


# 字典首页
@method_decorator(check_login, name="get")
class DictView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dict:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染模板
        return render(request, "dict/index.html")


# 查询字典分页数据
@method_decorator(check_login, name="get")
class DictListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dict:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询字典分页数据方法
        result = services.DictList(request)
        # 返回结果
        return result


# 查询字典详情
@method_decorator(check_login, name="get")
class DictDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dict:detail",)

    # GET请求渲染HTML模板
    def get(self, request, dict_id):
        # 调用查询字典详情服务方法
        data = services.DictDetail(dict_id)
        # 模板参数
        content = {
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "dict/edit.html", content)


# 添加字典
@method_decorator(check_login, name="post")
class DictAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dict:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加字典服务方法
        result = services.DictAdd(request)
        # 返回结果
        return result


# 更新字典
@method_decorator(check_login, name="post")
class DictUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:dict:update',)

    # 接收PUT请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新字典服务方法
        result = services.DictUpdate(request)
        # 返回结果
        return result


# 删除字典
@method_decorator(check_login, name="delete")
class DictDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:dict:delete',)

    # 接收DELETE请求
    def delete(self, request, dict_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除字典服务方法
        result = services.DictDelete(dict_id)
        # 返回结果
        return result
