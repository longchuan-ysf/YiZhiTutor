from django.shortcuts import render

# Create your views here.

from django.utils.decorators import method_decorator
from django.views import View

from application.city import services
from application.constants import CITY_LEVEL_LIST
from config.env import DEBUG
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

from utils import R


# 渲染城市首页
@method_decorator(check_login, name='get')
class CityView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:city:index',)

    # 接收GET请求
    def get(self, request):
        # 以下代码刷数据使用，可以直接删除
        # provinceList = City2.objects.filter(level_code=0).values()
        # for province in provinceList:
        #     pCity = City.objects.create(
        #         name=province['name'],
        #         city_code=province['city_code'],
        #         area_code=province['area_code'],
        #         parent_code=province['parent_code'],
        #         level=province['level_code'] + 1,
        #         zip_code=province['zip_code'],
        #         short_name=province['short_name'],
        #         full_name=province['merger_name'],
        #         pinyin=province['pinyin'],
        #         lng=province['lng'],
        #         lat=province['lat'],
        #         pid=0,
        #     )
        #     # 查询城市列表
        #     cityList = City2.objects.filter(level_code=1, parent_code=province['area_code']).values()
        #     for city in cityList:
        #         cCity = City.objects.create(
        #             name=city['name'],
        #             city_code=city['city_code'],
        #             area_code=city['area_code'],
        #             parent_code=city['parent_code'],
        #             level=city['level_code'] + 1,
        #             zip_code=city['zip_code'],
        #             short_name=city['short_name'],
        #             full_name=city['merger_name'],
        #             pinyin=city['pinyin'],
        #             lng=city['lng'],
        #             lat=city['lat'],
        #             pid=pCity.id,
        #         )
        #         # 查询县区列表
        #         areaList = City2.objects.filter(level_code=2, parent_code=city['area_code']).values()
        #         for area in areaList:
        #             dCity = City.objects.create(
        #                 name=area['name'],
        #                 city_code=area['city_code'],
        #                 area_code=area['area_code'],
        #                 parent_code=area['parent_code'],
        #                 level=area['level_code'] + 1,
        #                 zip_code=area['zip_code'],
        #                 short_name=area['short_name'],
        #                 full_name=area['merger_name'],
        #                 pinyin=area['pinyin'],
        #                 lng=area['lng'],
        #                 lat=area['lat'],
        #                 pid=cCity.id,
        #             )

        # 渲染HTML模板
        return render(request, "city/index.html")


# 查询城市分页数据
@method_decorator(check_login, name='get')
class CityListView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:city:list',)

    # 接收GET请求
    def get(self, request):
        # 调用查询城市分页数据
        result = services.CityList(request)
        # 返回结果
        return result


# 查询城市详情
@method_decorator(check_login, name='get')
class CityDetailView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:city:detail',)

    # 接收GET请求
    def get(self, request, city_id):
        # 调用查询城市详情方法
        data = services.CityDetail(city_id)
        # 模板参数
        content = {
            'levelList': CITY_LEVEL_LIST,
            'data': data
        }
        # 渲染模板并绑定参数
        return render(request, 'city/edit.html', content)


# 添加城市
@method_decorator(check_login, name='post')
class CityAddView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:city:add',)

    # 接收POST请求
    def post(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用添加城市方法
        result = services.CityAdd(request)
        # 返回结果
        return result


# 更新城市
@method_decorator(check_login, name='put')
class CityUpdateView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:city:update',)

    # 接收PUT请求
    def put(self, request):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用更新城市方法
        result = services.CityUpdate(request)
        # 返回结果
        return result


# 删除城市
@method_decorator(check_login, name='delete')
class CityDeleteView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:city:delete',)

    # 接收delete请求
    def delete(self, request, city_id):
        if DEBUG:
            return R.failed("演示环境，暂无操作权限")
        # 调用删除城市方法
        result = services.CityDelete(city_id)
        # 返回结果
        return result


# 根据上级ID获取子级城市
@method_decorator(check_login, name='get')
class CityChildView(PermissionRequired, View):
    # 方法权限标识
    permission_required = ('sys:city:child',)

    # 接收GET请求
    def get(self, request, city_code):
        # 调用查询城市详情方法
        data = services.getChildList(city_code)
        # 返回结果
        return R.ok(data)
