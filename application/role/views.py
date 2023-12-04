from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.role import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染角色首页
from utils import R


# 角色首页
@method_decorator(check_login, name='get')
class RoleView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:role:index',)

    # 接收GET请求
    def get(self, request):
        # 渲染HTML模板
        return render(request, "role/index.html")


# 查询角色分页数据
@method_decorator(check_login, name='get')
class RoleListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:role:list',)

    # 接收GET请求
    def get(self, request):
        # 调用查询角色分页数据
        result = services.RoleList(request)
        # 返回结果
        return result


# 查询角色详情
@method_decorator(check_login, name='get')
class RoleDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:role:detail',)

    # 接收GET请求
    def get(self, request, role_id):
        # 调用查询角色详情方法
        data = services.RoleDetail(role_id)
        # 模板参数
        content = {
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, 'role/edit.html', content)


# 添加角色
@method_decorator(check_login, name='post')
class RoleAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:role:add',)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加角色方法
        result = services.RoleAdd(request)
        # 返回结果
        return result


# 更新角色
@method_decorator(check_login, name='put')
class RoleUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:role:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新角色方法
        result = services.RoleUpdate(request)
        # 返回结果
        return result


# 删除角色
@method_decorator(check_login, name='delete')
class RoleDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:role:delete',)

    # 接收delete请求
    def delete(self, request, role_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除角色方法
        result = services.RoleDelete(role_id)
        # 返回结果
        return result


# 设置角色状态
@method_decorator(check_login, name='put')
class RoleStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:role:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置职级状态服务方法
        result = services.RoleStatus(request)
        # 返回结果
        return result
