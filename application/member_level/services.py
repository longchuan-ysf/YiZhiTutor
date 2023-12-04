import json
import logging

from django.core.paginator import Paginator

from application.member_level import forms
from application.member_level.models import MemberLevel
from constant.constants import PAGE_LIMIT
from utils import R, regular

from utils.utils import uid


# 获取会员等级分页数据
def MemberLevelList(request):
    # 页码
    page = int(request.GET.get("page", 1))
    # 每页数
    limit = int(request.GET.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = MemberLevel.objects.filter(is_delete=False)
    # 会员等级名称模糊筛选
    name = request.GET.get('name')
    if name:
        query = query.filter(name__contains=name)
    # 排序
    query = query.order_by("sort")
    # 设置分页
    paginator = Paginator(query, limit)
    # 记录总数
    count = paginator.count
    # 分页查询
    list = paginator.page(page)
    # 实例化结果
    result = []
    # 遍历数据源
    if len(list) > 0:
        for item in list:
            data = {
                'id': item.id,
                'name': item.name,
                'sort': item.sort,
                'create_time': str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None,
                'update_time': str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None,
            }
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据会员等级ID查询详情
def MemberLevelDetail(member_level_id):
    # 根据ID查询会员等级
    member_level = MemberLevel.objects.filter(is_delete=False, id=member_level_id).first()
    # 查询结果判空
    if not member_level:
        return None
    # 声明结构体
    data = {
        'id': member_level.id,
        'name': member_level.name,
        'sort': member_level.sort,
    }
    # 返回结果
    return data


# 添加会员等级
def MemberLevelAdd(request):
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
    form = forms.MemberLevelForm(dict_data)
    if form.is_valid():
        # 会员等级名称
        name = form.cleaned_data.get('name')
        # 会员等级排序
        sort = form.cleaned_data.get('sort')
        # 创建数据
        MemberLevel.objects.create(
            name=name,
            sort=sort,
            create_user=uid(request)
        )
        # 返回结果
        return R.ok(msg="创建成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)


# 更新会员等级
def MemberLevelUpdate(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
        # 会员等级ID
        member_level_id = dict_data.get('id')
        # 会员等级ID判空
        if not member_level_id or int(member_level_id) <= 0:
            return R.failed("会员等级ID不能为空")
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.MemberLevelForm(dict_data)
    if form.is_valid():
        # 会员等级名称
        name = form.cleaned_data.get('name')
        # 会员等级排序
        sort = int(form.cleaned_data.get('sort'))
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)

    # 根据ID查询会员等级
    member_level = MemberLevel.objects.only('id').filter(id=member_level_id, is_delete=False).first()
    # 查询结果判断
    if not member_level:
        return R.failed("会员等级不存在")

    # 对象赋值
    member_level.name = name
    member_level.sort = sort
    member_level.update_user = uid(request)
    # 更新数据
    member_level.save()
    # 返回结果
    return R.ok(msg="更新成功")


# 删除会员等级
def MemberLevelDelete(member_level_id):
    # 记录ID为空判断
    if not member_level_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = member_level_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for id in list:
            # 根据ID查询记录
            member_level = MemberLevel.objects.only('id').filter(id=int(id), is_delete=False).first()
            # 查询结果判空
            if not member_level:
                return R.failed("会员等级不存在")
            # 设置删除标识
            member_level.is_delete = True
            # 更新记录
            member_level.save()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))
