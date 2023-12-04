from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.config import services
from application.constants import CONFIG_DATA_TYPE_LIST
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染配置首页
from utils import R


# 配置首页
@method_decorator(check_login, name="get")
class ConfigView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:config:index",)

    # 接收GET请求
    def get(self, request):
        # 模板参数
        content = {
            'configTypeList': CONFIG_DATA_TYPE_LIST
        }
        # 渲染模板
        return render(request, "config/index.html", content)


# 查询配置分页数据
@method_decorator(check_login, name="get")
class ConfigListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:config:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询配置分页数据方法
        result = services.ConfigList(request)
        # 返回结果
        return result


# 查询配置详情
@method_decorator(check_login, name="get")
class ConfigDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:config:detail",)

    # GET请求渲染HTML模板
    def get(self, request, config_id):
        # 调用查询配置详情服务方法
        data = services.ConfigDetail(config_id)
        # 模板参数
        content = {
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "config/edit.html", content)


# 添加配置
@method_decorator(check_login, name="post")
class ConfigAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:config:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加配置服务方法
        result = services.ConfigAdd(request)
        # 返回结果
        return result


# 更新配置
@method_decorator(check_login, name="post")
class ConfigUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:config:update',)

    # 接收PUT请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新配置服务方法
        result = services.ConfigUpdate(request)
        # 返回结果
        return result


# 删除配置
@method_decorator(check_login, name="delete")
class ConfigDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:config:delete',)

    # 接收DELETE请求
    def delete(self, request, config_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除配置服务方法
        result = services.ConfigDelete(config_id)
        # 返回结果
        return result
