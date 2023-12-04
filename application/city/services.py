import json
import logging

from application.city import forms
from application.city.models import City
from application.constants import CITY_LEVEL_LIST
from utils import R, regular

# 查询城市数据列表
from utils.utils import uid


def CityList(request):
    # 实例化查询对象
    query = City.objects.filter(level__lte=3, is_delete=False)
    # 城市名称
    name = request.GET.get('name')
    if name:
        # 城市名称模糊查询
        query = query.filter(name__contains=name)
    # 查询数据
    list = query.order_by('id').all()

    # 实例化数组对象
    result = []
    # 遍历数据源
    if list:
        for item in list:
            data = {
                'id': item.id,
                'name': item.name,
                'short_name': item.short_name,
                'full_name': item.full_name,
                'pinyin': item.pinyin,
                'level': item.level,
                'level_name': CITY_LEVEL_LIST.get(item.level),
                'pid': item.pid,
                'city_code': item.city_code,
                'area_code': item.area_code,
                'parent_code': item.parent_code,
                'zip_code': item.zip_code,
                'lng': item.lng,
                'lat': item.lat,
                'create_time': str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None,
                'update_time': str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None,
            }
            result.append(data)
    # 返回结果
    return R.ok(data=result)


# 根据城市ID获取详情
def CityDetail(city_id):
    # 根据ID查询城市
    city = City.objects.filter(is_delete=False, id=city_id).first()
    # 查询结果判空
    if not city:
        return None
    # 声明结构体
    data = {
        'id': city.id,
        'name': city.name,
        'city_code': city.city_code,
        'area_code': city.area_code,
        'parent_code': city.parent_code,
        'level': city.level,
        'zip_code': city.zip_code,
        'short_name': city.short_name,
        'pinyin': city.pinyin,
        'lng': city.lng,
        'lat': city.lat,
        'pid': city.pid,
    }
    # 返回结果
    return data


# 添加城市
def CityAdd(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.CityForm(dict_data)
    if form.is_valid():
        # 城市名称
        name = form.cleaned_data.get('name')
        # 城市区号
        city_code = form.cleaned_data.get('city_code')
        # 行政编码
        area_code = form.cleaned_data.get('area_code')
        # 上级行政编码
        parent_code = form.cleaned_data.get('parent_code')
        # 城市级别
        level = int(form.cleaned_data.get('level'))
        # 邮政编码
        zip_code = form.cleaned_data.get('zip_code')
        # 城市简称
        short_name = form.cleaned_data.get('short_name')
        # 城市拼音
        pinyin = form.cleaned_data.get('pinyin')
        # 城市经度
        lng = form.cleaned_data.get('lng')
        # 城市纬度
        lat = form.cleaned_data.get('lat')
        # 上级城市ID
        pid = int(form.cleaned_data.get('pid'))
        # 创建数据
        City.objects.create(
            name=name,
            city_code=city_code,
            area_code=area_code,
            parent_code=parent_code,
            level=level,
            zip_code=zip_code,
            short_name=short_name,
            pinyin=pinyin,
            lng=lng,
            lat=lat,
            pid=pid,
            create_user=uid(request)
        )
        # 返回结果
        return R.ok(msg="创建成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)


# 更新城市
def CityUpdate(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
        # 城市ID
        city_id = dict_data.get('id')
        # 城市ID判空
        if not city_id or int(city_id) <= 0:
            return R.failed("城市ID不能为空")
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.CityForm(dict_data)
    if form.is_valid():
        # 城市名称
        name = form.cleaned_data.get('name')
        # 城市区号
        city_code = form.cleaned_data.get('city_code')
        # 行政编码
        area_code = form.cleaned_data.get('area_code')
        # 上级行政编码
        parent_code = form.cleaned_data.get('parent_code')
        # 城市级别
        level = int(form.cleaned_data.get('level'))
        # 邮政编码
        zip_code = form.cleaned_data.get('zip_code')
        # 城市简称
        short_name = form.cleaned_data.get('short_name')
        # 城市拼音
        pinyin = form.cleaned_data.get('pinyin')
        # 城市经度
        lng = form.cleaned_data.get('lng')
        # 城市纬度
        lat = form.cleaned_data.get('lat')
        # 上级城市ID
        pid = int(form.cleaned_data.get('pid'))
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)

    # 根据ID查询城市
    city = City.objects.only('id').filter(id=city_id, is_delete=False).first()
    # 查询结果判断
    if not city:
        return R.failed("城市不存在")

    # 对象赋值
    city.name = name
    city.city_code = city_code
    city.area_code = area_code
    city.parent_code = parent_code
    city.level = level
    city.zip_code = zip_code
    city.short_name = short_name
    city.pinyin = pinyin
    city.lng = lng
    city.lat = lat
    city.pid = pid
    city.update_user = uid(request)

    # 更新数据
    city.save()
    # 返回结果
    return R.ok(msg="更新成功")


# 删除城市
def CityDelete(city_id):
    # 记录ID为空判断
    if not city_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = city_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for id in list:
            # 根据ID查询记录
            city = City.objects.only('id').filter(id=int(id), is_delete=False).first()
            # 查询结果判空
            if not city:
                return R.failed("城市不存在")
            # 设置删除标识
            city.is_delete = True
            # 更新记录
            city.save()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 根据城市ID获取子级城市
def getChildList(city_code):
    # 查询子级城市
    childList = City.objects.filter(is_delete=False, parent_code=city_code).values()
    # 实例化子级城市对象
    list = []
    # 遍历数据源
    if childList:
        for v in childList:
            item = {
                'area_code': v['area_code'],
                'name': v['name']
            }
            # 加入列表
            list.append(item)
    # 返回结果
    return list
