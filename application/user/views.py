from django.shortcuts import render

# Create your views here.


from django.utils.decorators import method_decorator
from django.views import View

from application.dept.models import Dept
from application.level.models import Level
from application.position.models import Position
from application.role.models import Role
from application.user import services
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

# 渲染用户首页
from utils import R


# 用户首页
@method_decorator(check_login, name="get")
class UserView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:user:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染模板
        return render(request, "user/index.html")


# 查询用户分页数据
@method_decorator(check_login, name="get")
class UserListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:user:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询用户分页数据方法
        result = services.UserList(request)
        # 返回结果
        return result


# 查询用户详情
@method_decorator(check_login, name="get")
class UserDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:user:detail",)

    # GET请求渲染HTML模板
    def get(self, request, user_id):
        # 调用查询用户详情服务方法
        data = services.UserDetail(user_id)
        # 查询角色列表
        roleList = Role.objects.filter(is_delete=False).values()
        # 查询部门列表
        deptList = Dept.objects.filter(is_delete=False).values()
        # 查询职级列表
        levelList = Level.objects.filter(is_delete=False).values()
        # 查询岗位列表
        positionList = Position.objects.filter(is_delete=False).values()

        # 模板参数
        content = {
            'roleList': roleList,
            'deptList': deptList,
            'levelList': levelList,
            'positionList': positionList,
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, "user/edit.html", content)


# 添加用户
@method_decorator(check_login, name="post")
class UserAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:user:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加用户服务方法
        result = services.UserAdd(request)
        # 返回结果
        return result


# 更新用户
@method_decorator(check_login, name="put")
class UserUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:user:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新用户服务方法
        result = services.UserUpdate(request)
        # 返回结果
        return result


# 删除用户
@method_decorator(check_login, name="delete")
class UserDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:user:delete',)

    # 接收DELETE请求
    def delete(self, request, user_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除用户服务方法
        result = services.UserDelete(user_id)
        # 返回结果
        return result


# 设置用户状态
@method_decorator(check_login, name='put')
class UserStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:user:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置用户状态服务方法
        result = services.UserStatus(request)
        # 返回结果
        return result


# 重置密码
@method_decorator(check_login, name='put')
class UserResetPwdView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:user:resetPwd',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置用户状态服务方法
        result = services.UserResetPwd(request)
        # 返回结果
        return result
