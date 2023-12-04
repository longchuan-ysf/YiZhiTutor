from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from application.constants import DEPT_TYPE_LIST
from application.dept import services
from config.env import DEBUG
from middleware.login_middleware import check_login

from middleware.permission_middleware import PermissionRequired

# 渲染部门首页
from utils import R


# 部门首页
@method_decorator(check_login, name='get')
class DeptView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dept:index",)

    # 接收GET请求
    def get(self, request):
        # 渲染HTML模板
        return render(request, "dept/index.html")


# 查询部门分页数据
@method_decorator(check_login, name='get')
class DeptListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dept:list",)

    # 接收GET请求
    def get(self, request):
        # 调用查询部门分页服务方法
        result = services.DeptList(request)
        # 返回结果
        return result


# 查询部门详情
@method_decorator(check_login, name='get')
class DeptDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dept:detail",)

    # 接收GET请求
    def get(self, request, dept_id):
        # 调用查询部门详情服务方法
        data = services.DeptDetail(dept_id)
        # 上级ID
        pid = request.GET.get('pid')
        if pid and len(pid.strip()) > 0:
            data = {'pid': int(pid)}
        # 渲染模板并绑定参数
        content = {
            'data': data,
            'typeList': DEPT_TYPE_LIST
        }
        return render(request, "dept/edit.html", content)


# 查询部门详情
@method_decorator(check_login, name='post')
class DeptAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dept:add",)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加部门服务方法
        result = services.DeptAdd(request)
        # 返回结果
        return result


# 更新部门
@method_decorator(check_login, name='put')
class DeptUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dept:update",)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新部门服务方法
        result = services.DeptUpdate(request)
        # 返回结果
        return result


# 删除部门
@method_decorator(check_login, name='delete')
class DeptDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ("sys:dept:delete",)

    # 接收DELETE请求
    def delete(self, request, dept_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除部门服务方法
        result = services.DeptDelete(dept_id)
        # 返回结果
        return result
