from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired
from . import services
from utils import R

# 为全部请求方法添加装饰器
from .models import Level


# 渲染职级首页
@method_decorator(check_login, name='dispatch')
class LevelView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:index',)

    # GET请求渲染HTML模板
    def get(self, request):
        # 使用render渲染方式
        return render(request, 'level/index.html')


# 查询职级分页数据
# 为全部请求方法添加装饰器
@method_decorator(check_login, name='dispatch')
class LevelListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:list',)

    # POST查询分页数据
    def get(self, request):
        # 调用查询职级分页数据服务方法
        result = services.LevelList(request)
        # 返回结果
        return result

    # 异常请求捕捉
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("您当前采用的method是：%s，本视图只支持使用post请求！" % request.method)


# 查询职级详情
@method_decorator(check_login, name='dispatch')
class LevelDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:detail',)

    # GET请求渲染HTML模板
    def get(self, request, level_id):
        # 调用查询职级详情服务方法
        data = services.LevelDetail(level_id)
        # 模板参数
        content = {
            'data': data,
        }
        # 渲染模板并绑定参数
        return render(request, 'level/edit.html', content)


# 添加职级
@method_decorator(check_login, name='dispatch')
class LevelAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:add',)

    # 接收POST网络请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加职级服务
        result = services.LevelAdd(request)
        # 返回结果
        return result


# 更新职级
@method_decorator(check_login, name='dispatch')
class LevelUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:update',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新职级服务方法
        result = services.LevelUpdate(request)
        # 返回结果
        return result


# 删除职级
@method_decorator(check_login, name='dispatch')
class LevelDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:delete',)

    def delete(self, request, level_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除职级服务方法
        result = services.LevelDelete(level_id)
        # 返回结果
        return result


# 设置职级状态
@method_decorator(check_login, name='put')
class LevelStatusView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:status',)

    # PUT请求提交数据
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用设置职级状态服务方法
        result = services.LevelStatus(request)
        # 返回结果
        return result


# 导入Excel(此方法为预留接口，暂未开放)
@method_decorator(check_login, name='post')
class LevelImportView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:import',)

    # 接收POST请求
    def post(self, request):
        # 预留的接口
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        print("导入数据")
        return R.ok()


# 导出Excel(此方法为预留接口，暂未开放)
@method_decorator(check_login, name='get')
class LevelExportView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:level:export',)

    # 接收GET请求
    def get(self, request):
        # 预留的接口
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        print("导出数据")
        return R.ok()
