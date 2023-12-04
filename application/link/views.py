from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.constants import LINK_TYPE_LIST, LINK_PLATFORM_LIST, LINK_FORM_LIST
from application.link import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染友链首页
from utils import R


# 友链首页
@method_decorator(check_login, name="get")
class LinkView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:link:index",)

    # 接收GET请求
    def get(self, request):
        # 模板参数
        content = {
            'typeList': LINK_TYPE_LIST,
            'platformList': LINK_PLATFORM_LIST,
            'formList': LINK_FORM_LIST
        }
        # 渲染模板
        return render(request, "link/index.html", content)


# 查询友链分页数据
@method_decorator(check_login, name="get")
class LinkListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:link:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询友链分页数据方法
        result = services.LinkList(request)
        # 返回结果
        return result


# 查询友链详情
@method_decorator(check_login, name="get")
class LinkDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:link:detail",)

    # GET请求渲染HTML模板
    def get(self, request, link_id):
        # 调用查询友链详情服务方法
        data = services.LinkDetail(link_id)
        # 模板参数
        content = {
            'typeList': LINK_TYPE_LIST,
            'platformList': LINK_PLATFORM_LIST,
            'formList': LINK_FORM_LIST,
            'data': data,
        }
        # 渲染模板并绑定参数
        return render(request, "link/edit.html", content)


# 添加友链
@method_decorator(check_login, name="post")
class LinkAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:link:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加友链服务方法
        result = services.LinkAdd(request)
        # 返回结果
        return result


# 更新友链
@method_decorator(check_login, name="put")
class LinkUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:link:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新友链服务方法
        result = services.LinkUpdate(request)
        # 返回结果
        return result


# 删除友链
@method_decorator(check_login, name="delete")
class LinkDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:link:delete',)

    # 接收DELETE请求
    def delete(self, request, link_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除友链服务方法
        result = services.LinkDelete(link_id)
        # 返回结果
        return result


# 设置友链状态
@method_decorator(check_login, name='put')
class LinkStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:link:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置友链状态服务方法
        result = services.LinkStatus(request)
        # 返回结果
        return result
