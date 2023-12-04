from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.ad_sort import services
from application.constants import AD_SORT_PLATFORM_LIST
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染广告位首页
from utils import R


# 广告位首页
@method_decorator(check_login, name="get")
class AdSortView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:adsort:index",)

    # 接收GET请求
    def get(self, request):
        # 模板参数
        content = {
            'platformList': AD_SORT_PLATFORM_LIST,
        }
        # 渲染模板
        return render(request, "ad_sort/index.html", content)


# 查询广告位分页数据
@method_decorator(check_login, name="get")
class AdSortListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:adsort:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询广告位分页数据方法
        result = services.AdSortList(request)
        # 返回结果
        return result


# 查询广告位详情
@method_decorator(check_login, name="get")
class AdSortDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:adsort:detail",)

    # GET请求渲染HTML模板
    def get(self, request, adsort_id):
        # 调用查询广告位详情服务方法
        data = services.AdSortDetail(adsort_id)
        # 模板参数
        content = {
            'platformList': AD_SORT_PLATFORM_LIST,
            'data': data,
        }
        # 渲染模板并绑定参数
        return render(request, "ad_sort/edit.html", content)


# 添加广告位
@method_decorator(check_login, name="post")
class AdSortAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:adsort:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加广告位服务方法
        result = services.AdSortAdd(request)
        # 返回结果
        return result


# 更新广告位
@method_decorator(check_login, name="put")
class AdSortUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:adsort:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新广告位服务方法
        result = services.AdSortUpdate(request)
        # 返回结果
        return result


# 删除广告位
@method_decorator(check_login, name="delete")
class AdSortDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:adsort:delete',)

    # 接收DELETE请求
    def delete(self, request, adsort_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除广告位服务方法
        result = services.AdSortDelete(adsort_id)
        # 返回结果
        return result
