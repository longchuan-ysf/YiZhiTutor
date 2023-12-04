from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

import application.item.services
from application.item_cate import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

from utils import R


# 渲染栏目首页
@method_decorator(check_login, name="get")
class ItemCateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:itemcate:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染模板
        return render(request, "item_cate/index.html")


# 查询栏目分页数据
@method_decorator(check_login, name="get")
class ItemCateListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:itemcate:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询栏目分页数据方法
        result = services.ItemCateList(request)
        # 返回结果
        return result


# 查询栏目详情
@method_decorator(check_login, name="get")
class ItemCateDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:itemcate:detail",)

    # GET请求渲染HTML模板
    def get(self, request, item_id):
        # 调用查询栏目详情服务方法
        data = services.ItemCateDetail(item_id)
        # 获取站点列表
        itemList = application.item.services.getItemList();
        # 模板参数
        content = {
            'data': data,
            'itemList': itemList
        }
        # 渲染模板并绑定参数
        return render(request, "item_cate/edit.html", content)


# 添加栏目
@method_decorator(check_login, name="post")
class ItemCateAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:itemcate:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加栏目服务方法
        result = services.ItemCateAdd(request)
        # 返回结果
        return result


# 更新栏目
@method_decorator(check_login, name="put")
class ItemCateUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:itemcate:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新栏目服务方法
        result = services.ItemCateUpdate(request)
        # 返回结果
        return result


# 删除栏目
@method_decorator(check_login, name="delete")
class ItemCateDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:itemcate:delete',)

    # 接收DELETE请求
    def delete(self, request, item_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除栏目服务方法
        result = services.ItemCateDelete(item_id)
        # 返回结果
        return result


# 获取栏目树结构
@method_decorator(check_login, name="get")
class ItemCateTreeView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:itemcate:tree',)

    # 接收DELETE请求
    def get(self, request, item_id):
        # 调用删除栏目服务方法
        result = services.GetTreeList(item_id)
        # 返回结果
        return R.ok(result)
