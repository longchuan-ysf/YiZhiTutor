from django.shortcuts import render

# Create your views here.

from django.utils.decorators import method_decorator
from django.views import View

from application.config_data import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 查询配置项分页数据
from utils import R


# 查询配置项分页数据
@method_decorator(check_login, name="get")
class ConfigDataListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:config:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询配置项分页数据方法
        result = services.ConfigDataList(request)
        # 返回结果
        return result


# 查询配置项详情
@method_decorator(check_login, name="get")
class ConfigDataDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:config:detail",)

    # GET请求渲染HTML模板
    def get(self, request, config_id):
        # 调用查询配置项详情服务方法
        data = services.ConfigDataDetail(config_id)
        # 模板参数
        content = {
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "dict/edit.html", content)


# 添加配置项
@method_decorator(check_login, name="post")
class ConfigDataAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:config:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加配置项服务方法
        result = services.ConfigDataAdd(request)
        # 返回结果
        return result


# 更新配置项
@method_decorator(check_login, name="post")
class ConfigDataUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:config:update',)

    # 接收PUT请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新配置项服务方法
        result = services.ConfigDataUpdate(request)
        # 返回结果
        return result


# 删除配置项
@method_decorator(check_login, name="delete")
class ConfigDataDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:config:delete',)

    # 接收DELETE请求
    def delete(self, request, config_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除配置项服务方法
        result = services.ConfigDataDelete(config_id)
        # 返回结果
        return result


# 设置配置项状态
@method_decorator(check_login, name='put')
class ConfigDataStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:config:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置配置项状态服务方法
        result = services.ConfigDataStatus(request)
        # 返回结果
        return result
