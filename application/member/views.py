from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.constants import MEMBER_SOURCE_LIST, GENDER_LIST
from application.member import services
from application.member_level.models import MemberLevel
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染会员首页
from utils import R


# 会员首页
@method_decorator(check_login, name="get")
class MemberView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:member:index",)

    # 接收GET请求
    def get(self, request):
        # 模板参数
        content = {
            'sourceList': MEMBER_SOURCE_LIST,
        }
        # 渲染模板
        return render(request, "member/index.html", content)


# 查询会员分页数据
@method_decorator(check_login, name="get")
class MemberListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:member:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询会员分页数据方法
        result = services.MemberList(request)
        # 返回结果
        return result


# 查询会员详情
@method_decorator(check_login, name="get")
class MemberDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:member:detail",)

    # GET请求渲染HTML模板
    def get(self, request, member_id):
        # 调用查询会员详情服务方法
        data = services.MemberDetail(member_id)
        # 查询会员等级列表
        memberLevelList = MemberLevel.objects.filter(is_delete=False).values()
        # 模板参数
        content = {
            'genderList': GENDER_LIST,
            'sourceList': MEMBER_SOURCE_LIST,
            'memberLevelList': memberLevelList,
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "member/edit.html", content)


# 添加会员
@method_decorator(check_login, name="post")
class MemberAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:member:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加会员服务方法
        result = services.MemberAdd(request)
        # 返回结果
        return result


# 更新会员
@method_decorator(check_login, name="put")
class MemberUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:member:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新会员服务方法
        result = services.MemberUpdate(request)
        # 返回结果
        return result


# 删除会员
@method_decorator(check_login, name="delete")
class MemberDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:member:delete',)

    # 接收DELETE请求
    def delete(self, request, member_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除会员服务方法
        result = services.MemberDelete(member_id)
        # 返回结果
        return result


# 设置会员状态
@method_decorator(check_login, name='put')
class MemberStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:member:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置会员状态服务方法
        result = services.MemberStatus(request)
        # 返回结果
        return result
