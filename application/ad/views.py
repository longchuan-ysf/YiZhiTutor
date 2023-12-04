from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

import application.ad_sort.services
from application.ad import services
from application.constants import AD_TYPE_LIST
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired


# 渲染广告首页
from utils import R


@method_decorator(check_login, name="get")
class AdView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:ad:index",)

    # 接收GET请求
    def get(self, request):
        # 模板参数
        content = {
            'typeList': AD_TYPE_LIST,
        }
        # 渲染模板
        return render(request, "ad/index.html", content)


# 查询广告分页数据
@method_decorator(check_login, name="get")
class AdListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:ad:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询广告分页数据方法
        result = services.AdList(request)
        # 返回结果
        return result


# 查询广告详情
@method_decorator(check_login, name="get")
class AdDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:ad:detail",)

    # GET请求渲染HTML模板
    def get(self, request, ad_id):
        # 调用查询广告详情服务方法
        data = services.AdDetail(ad_id)
        # 查询全部广告位列表
        adSortList = application.ad_sort.services.GetAdSortList()
        # 模板参数
        content = {
            'typeList': AD_TYPE_LIST,
            'sortList': adSortList,
            'data': data,
        }
        # 渲染模板并绑定参数
        return render(request, "ad/edit.html", content)


# 添加广告
@method_decorator(check_login, name="post")
class AdAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:ad:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加广告服务方法
        result = services.AdAdd(request)
        # 返回结果
        return result


# 更新广告
@method_decorator(check_login, name="put")
class AdUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:ad:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新广告服务方法
        result = services.AdUpdate(request)
        # 返回结果
        return result


# 删除广告
@method_decorator(check_login, name="delete")
class AdDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:ad:delete',)

    # 接收DELETE请求
    def delete(self, request, ad_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除广告服务方法
        result = services.AdDelete(ad_id)
        # 返回结果
        return result

# 设置状态
@method_decorator(check_login, name='put')
class AdStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:ad:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置职级状态服务方法
        result = services.AdStatus(request)
        # 返回结果
        return result
