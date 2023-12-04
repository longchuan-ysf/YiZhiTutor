import json
import logging

from django.core.paginator import Paginator

from application.constants import GENDER_LIST, MEMBER_SOURCE_LIST
from application.member import forms
from application.member.models import Member
from application.member_level.models import MemberLevel
from constant.constants import PAGE_LIMIT
from utils import R, regular
from utils.utils import getImageURL, saveImage, uid


# 查询会员分页数据
def MemberList(request):
    # 页码
    page = int(request.GET.get("page", 1))
    # 每页数
    limit = int(request.GET.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = Member.objects.filter(is_delete=False)
    # 会员名
    username = request.GET.get('username')
    if username:
        query = query.filter(username__contains=username)
    # 注册来源：1-网站注册 2-客户端注册 3-小程序注册 4-手机站注册 5-后台添加
    source = request.GET.get('source')
    if source:
        query = query.filter(source=source)
    # 性别
    gender = request.GET.get('gender')
    if gender:
        query = query.filter(gender=gender)
    # 会员状态
    status = request.GET.get('status')
    if status:
        query = query.filter(status=status)
    # 排序
    query = query.order_by("id")
    # 设置分页
    paginator = Paginator(query, limit)
    # 记录总数
    count = paginator.count
    # 分页查询
    member_list = paginator.page(page)
    # 实例化结果
    result = []
    # 遍历数据源
    if len(member_list) > 0:
        # 查看会员等级列表
        memberLevelList = MemberLevel.objects.filter(is_delete=False).values()
        member_level_list = {}
        if memberLevelList:
            for member_level in memberLevelList:
                member_level_list[member_level['id']] = member_level['name']

        # 遍历会员数据源
        for item in member_list:
            data = {
                'id': item.id,
                'realname': item.realname,
                'nickname': item.nickname,
                'gender': item.gender,
                'gender_name': GENDER_LIST.get(item.gender),
                'avatar': getImageURL(item.avatar) if item.avatar else "",
                'birthday': item.birthday,
                'email': item.email,
                'member_level_name': member_level_list.get(item.member_level) if member_level_list else "",
                'source': item.source,
                'source_name': MEMBER_SOURCE_LIST.get(item.source),
                'username': item.username,
                'status': item.status,
                'create_time': str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else "",
                'update_time': str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else "",
            }
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据ID查看会员详情
def MemberDetail(member_id):
    # 根据ID查询会员
    member = Member.objects.filter(is_delete=False, id=member_id).first()
    # 查询结果判空
    if not member:
        return None
    # 声明结构体
    data = {
        'id': member.id,
        'realname': member.realname,
        'nickname': member.nickname,
        'gender': member.gender,
        'avatar': getImageURL(member.avatar) if member.avatar else "",
        'birthday': str(member.birthday),
        'email': member.email,
        'username': member.username,
        'province_code': member.province_code,
        'city_code': member.city_code,
        'district_code': member.district_code,
        'address': member.address,
        'intro': member.intro,
        'signature': member.signature,
        'source': member.source,
        'status': member.status,
    }
    # 返回结果
    return data


# 添加会员
def MemberAdd(request):
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
    form = forms.MemberForm(dict_data)
    if form.is_valid():
        # 会员姓名
        realname = form.cleaned_data.get('realname')
        # 会员昵称
        nickname = form.cleaned_data.get('nickname')
        # 性别
        gender = form.cleaned_data.get('gender')
        # 头像
        avatar = form.cleaned_data.get('avatar')
        if avatar:
            avatar = saveImage(avatar, "user")
        # 邮箱
        email = form.cleaned_data.get('email')
        # 出生日期
        birthday = form.cleaned_data.get('birthday')
        # 省份编码
        province_code = form.cleaned_data.get('province_code')
        # 城市编码
        city_code = form.cleaned_data.get('city_code')
        # 县区编码
        district_code = form.cleaned_data.get('district_code')
        # 详细地址
        address = form.cleaned_data.get('address')
        # 会员名
        username = form.cleaned_data.get('username')
        # 个人简介
        intro = form.cleaned_data.get('intro')
        # 个人签名
        signature = form.cleaned_data.get('signature')
        # 注册来源
        source = form.cleaned_data.get('source')
        # 状态
        status = form.cleaned_data.get('status')

        # 创建数据
        Member.objects.create(
            realname=realname,
            nickname=nickname,
            gender=gender,
            avatar=avatar,
            email=email,
            birthday=birthday,
            province_code=province_code,
            city_code=city_code,
            district_code=district_code,
            address=address,
            username=username,
            intro=intro,
            signature=signature,
            source=source,
            status=status,
            create_user=uid(request)
        )
        # 返回结果
        return R.ok(msg="创建成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)


# 更新会员
def MemberUpdate(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
        # 会员ID
        member_id = dict_data.get('id')
        # 会员ID判空
        if not member_id or int(member_id) <= 0:
            return R.failed("会员ID不能为空")
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.MemberForm(dict_data)
    if form.is_valid():
        # 会员姓名
        realname = form.cleaned_data.get('realname')
        # 会员昵称
        nickname = form.cleaned_data.get('nickname')
        # 性别
        gender = form.cleaned_data.get('gender')
        # 头像
        avatar = form.cleaned_data.get('avatar')
        if avatar:
            avatar = saveImage(avatar, "user")
        # 邮箱
        email = form.cleaned_data.get('email')
        # 出生日期
        birthday = form.cleaned_data.get('birthday')
        # 省份编码
        province_code = form.cleaned_data.get('province_code')
        # 城市编码
        city_code = form.cleaned_data.get('city_code')
        # 县区编码
        district_code = form.cleaned_data.get('district_code')
        # 详细地址
        address = form.cleaned_data.get('address')
        # 会员名
        username = form.cleaned_data.get('username')
        # 个人简介
        intro = form.cleaned_data.get('intro')
        # 个人签名
        signature = form.cleaned_data.get('signature')
        # 注册来源
        source = form.cleaned_data.get('source')
        # 状态
        status = form.cleaned_data.get('status')
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)

    # 根据ID查询会员
    member = Member.objects.only('id').filter(id=member_id, is_delete=False).first()
    # 查询结果判断
    if not member:
        return R.failed("会员不存在")

    # 对象赋值
    member.realname = realname
    member.nickname = nickname
    member.gender = gender
    member.email = email
    member.birthday = birthday
    member.province_code = province_code
    member.city_code = city_code
    member.district_code = district_code
    member.address = address
    member.username = username
    member.intro = intro
    member.signature = signature
    member.source = source
    member.status = status
    member.update_user = uid(request)

    # 更新数据
    member.save()
    # 返回结果
    return R.ok(msg="更新成功")


# 删除会员
def MemberDelete(member_id):
    # 记录ID为空判断
    if not member_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = member_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for id in list:
            # 根据ID查询记录
            member = Member.objects.only('id').filter(id=int(id), is_delete=False).first()
            # 查询结果判空
            if not member:
                return R.failed("会员不存在")
            # 设置删除标识
            member.is_delete = True
            # 更新记录
            member.save()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 设置状态
def MemberStatus(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数判空
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}".format(e))
        return R.failed("参数错误")

    # 表单验证
    form = forms.MemberStatusForm(data=dict_data)
    if form.is_valid():
        # 会员ID
        member_id = int(form.cleaned_data.get('id'))
        # 会员状态
        status = int(form.cleaned_data.get("status"))
    else:
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 根据ID查询会员
    member = Member.objects.only('id').filter(id=member_id, is_delete=False).first()
    # 查询结果判空
    if not member:
        return R.failed("记录不存在")
    # 给对象赋值
    member.status = status
    # 更新记录
    member.save()
    # 返回结果
    return R.ok()
