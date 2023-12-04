from django.shortcuts import render

# Create your views here.

from django.utils.decorators import method_decorator
from django.views import View

from application.constants import MENU_TYPE_LIST, MENU_TARGET_LIST
from application.menu import services
from application.menu.models import Menu
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染菜单首页
from utils import R


# 菜单首页
@method_decorator(check_login, name='get')
class MenuView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:menu:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染HTML模板
        return render(request, "menu/index.html")


# 查询菜单分页数据
@method_decorator(check_login, name='get')
class MenuListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:menu:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询菜单分页服务方法
        result = services.MenuList(request)
        # 返回结果
        return result


# 查询菜单详情
@method_decorator(check_login, name='get')
class MenuDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:menu:detail",)

    # 接收GET请求
    def get(self, request, menu_id):
        # 调用查询菜单详情服务方法
        data = services.MenuDetail(menu_id)
        # 上级ID
        pid = request.GET.get('pid')
        if pid and len(pid.strip()) > 0:
            data = {'pid': int(pid)}

        # 获取菜单下拉数结构
        menuList = services.MakeList()
        # 获取权限节点
        func_list = Menu.objects.filter(is_delete=False, pid=menu_id, type=1).values()
        funcList = []
        for v in func_list:
            funcList.append(v['sort'])
        # 渲染模板并绑定参数
        content = {
            'data': data,
            'typeList': MENU_TYPE_LIST,
            'targetList': MENU_TARGET_LIST,
            'menuList': menuList,
            'funcList': funcList
        }
        return render(request, "menu/edit.html", content)


# 查询菜单详情
@method_decorator(check_login, name='post')
class MenuAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:menu:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加菜单服务方法
        result = services.MenuAdd(request)
        # 返回结果
        return result


# 更新菜单
@method_decorator(check_login, name='put')
class MenuUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:menu:update",)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新菜单服务方法
        result = services.MenuUpdate(request)
        # 返回结果
        return result


# 删除菜单
@method_decorator(check_login, name='delete')
class MenuDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:menu:delete",)

    # 接收DELETE请求
    def delete(self, request, menu_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除菜单服务方法
        result = services.MenuDelete(menu_id)
        # 返回结果
        return result
