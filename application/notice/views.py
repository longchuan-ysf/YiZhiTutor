from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.constants import NOTICE_SOURCE_LIST
from application.notice import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染通知公告首页
from utils import R


# 通知公告首页
@method_decorator(check_login, name="get")
class NoticeView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:notice:index",)

    # 接收GET请求
    def get(self, request):
        # 模板参数
        content = {
            'sourceList': NOTICE_SOURCE_LIST,
        }
        # 渲染模板
        return render(request, "notice/index.html", content)


# 查询通知公告分页数据
@method_decorator(check_login, name="get")
class NoticeListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:notice:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询通知公告分页数据方法
        result = services.NoticeList(request)
        # 返回结果
        return result


# 查询通知公告详情
@method_decorator(check_login, name="get")
class NoticeDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:notice:detail",)

    # GET请求渲染HTML模板
    def get(self, request, notice_id):
        # 调用查询通知公告详情服务方法
        data = services.NoticeDetail(notice_id)
        # 模板参数
        content = {
            'sourceList': NOTICE_SOURCE_LIST,
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "notice/edit.html", content)


# 添加通知公告
@method_decorator(check_login, name="post")
class NoticeAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:notice:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加通知公告服务方法
        result = services.NoticeAdd(request)
        # 返回结果
        return result


# 更新通知公告
@method_decorator(check_login, name="put")
class NoticeUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:notice:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新通知公告服务方法
        result = services.NoticeUpdate(request)
        # 返回结果
        return result


# 删除通知公告
@method_decorator(check_login, name="delete")
class NoticeDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:notice:delete',)

    # 接收DELETE请求
    def delete(self, request, notice_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除通知公告服务方法
        result = services.NoticeDelete(notice_id)
        # 返回结果
        return result
