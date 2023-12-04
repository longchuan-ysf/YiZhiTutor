from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.position import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染岗位首页
from utils import R


# 岗位首页
@method_decorator(check_login, name="get")
class PositionView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:position:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染模板
        return render(request, "position/index.html")


# 查询岗位分页数据
@method_decorator(check_login, name="get")
class PositionListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:position:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询岗位分页数据方法
        result = services.PositionList(request)
        # 返回结果
        return result


# 查询岗位详情
@method_decorator(check_login, name="get")
class PositionDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:position:detail",)

    # GET请求渲染HTML模板
    def get(self, request, position_id):
        # 调用查询岗位详情服务方法
        data = services.PositionDetail(position_id)
        # 模板参数
        content = {
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "position/edit.html", content)


# 添加岗位
@method_decorator(check_login, name="post")
class PositionAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:position:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加岗位服务方法
        result = services.PositionAdd(request)
        # 返回结果
        return result


# 更新岗位
@method_decorator(check_login, name="put")
class PositionUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:position:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新岗位服务方法
        result = services.PositionUpdate(request)
        # 返回结果
        return result


# 删除岗位
@method_decorator(check_login, name="delete")
class PositionDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:position:delete',)

    # 接收DELETE请求
    def delete(self, request, position_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除岗位服务方法
        result = services.PositionDelete(position_id)
        # 返回结果
        return result


# 设置岗位状态
@method_decorator(check_login, name='put')
class PositionStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:position:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置岗位状态服务方法
        result = services.PositionStatus(request)
        # 返回结果
        return result
