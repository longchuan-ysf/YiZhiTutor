from django.utils.decorators import method_decorator
from django.views import View

from application.role_menu import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

from utils import R


# 查询角色菜单列表
@method_decorator(check_login, name='get')
class RoleMenuView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:rolemenu:index',)

    # 接收GET请求
    def get(self, request, role_id):
        # 调用查询角色菜单方法
        menu_list = services.getRoleMenuList(role_id)
        # 返回结果
        return R.ok(data=menu_list)


# 保存角色菜单数据
@method_decorator(check_login, name='post')
class RoleMenuSaveView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:rolemenu:save',)

    # 接收GET请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用保存数据方法
        result = services.save(request)
        # 返回结果
        return result
