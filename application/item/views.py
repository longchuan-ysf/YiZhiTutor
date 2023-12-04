from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.constants import ITEM_TYPE_LIST
from application.item import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染站点首页
from utils import R


# 站点首页
@method_decorator(check_login, name="get")
class ItemView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:item:index",)

    # 接收GET请求
    def get(self, request):
        # 模板参数
        content = {
            'typeList': ITEM_TYPE_LIST
        }
        # 渲染模板
        return render(request, "item/index.html", content)


# 查询站点分页数据
@method_decorator(check_login, name="get")
class ItemListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:item:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询站点分页数据方法
        result = services.ItemList(request)
        # 返回结果
        return result


# 查询站点详情
@method_decorator(check_login, name="get")
class ItemDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:item:detail",)

    # GET请求渲染HTML模板
    def get(self, request, item_id):
        # 调用查询站点详情服务方法
        data = services.ItemDetail(item_id)
        # 模板参数
        content = {
            'typeList': ITEM_TYPE_LIST,
            'data': data,
        }
        # 渲染模板并绑定参数
        return render(request, "item/edit.html", content)


# 添加站点
@method_decorator(check_login, name="post")
class ItemAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:item:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加站点服务方法
        result = services.ItemAdd(request)
        # 返回结果
        return result


# 更新站点
@method_decorator(check_login, name="put")
class ItemUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:item:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新站点服务方法
        result = services.ItemUpdate(request)
        # 返回结果
        return result


# 删除站点
@method_decorator(check_login, name="delete")
class ItemDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:item:delete',)

    # 接收DELETE请求
    def delete(self, request, item_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除站点服务方法
        result = services.ItemDelete(item_id)
        # 返回结果
        return result
