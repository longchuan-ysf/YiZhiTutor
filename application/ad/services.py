import json
import logging

from django.core.paginator import Paginator

from application.ad import forms
from application.ad.models import Ad
from application.ad_sort.models import AdSort
from application.constants import AD_TYPE_LIST
from config.env import IMAGE_URL
from constant.constants import PAGE_LIMIT
from utils import R, regular
from utils.utils import getImageURL, saveImage, saveEditContent, uid


# 查询广告分页数据
def AdList(request):
    # 页码
    page = int(request.GET.get("page", 1))
    # 每页数
    limit = int(request.GET.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = Ad.objects.filter(is_delete=False)
    # 广告标题
    title = request.GET.get('title')
    if title:
        query = query.filter(title__contains=title)
    # 广告类型：1图片 2文字 3视频 4推荐
    type = request.GET.get('type')
    if type:
        query = query.filter(type=type)
    # 广告状态
    status = request.GET.get('status')
    if status:
        query = query.filter(status=status)
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
            # 根据广告ID查询信息
            ad_sort = AdSort.objects.filter(is_delete=False, id=item.sort_id).first()
            data = {
                'id': item.id,
                'title': item.title,
                'sort_id': item.sort_id,
                'sort_desc': ad_sort.name + "=>" + str(ad_sort.loc_id) if ad_sort else None,
                'type': item.type,
                'type_name': AD_TYPE_LIST.get(item.type),
                'cover': getImageURL(item.cover) if item.cover else None,
                'url': item.url,
                'width': item.width,
                'height': item.height,
                'start_time': str(item.start_time.strftime('%Y-%m-%d %H:%M:%S')) if item.start_time else None,
                'end_time': str(item.end_time.strftime('%Y-%m-%d %H:%M:%S')) if item.end_time else None,
                'click': item.click,
                'status': item.status,
                'sort': item.sort,
                'note': item.note,
                'create_time': str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None,
                'update_time': str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None,
            }
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据广告ID查询详情
def AdDetail(ad_id):
    # 根据广告ID查询信息
    ad = Ad.objects.filter(is_delete=False, id=ad_id).first()
    # 查询结果为空判断
    if not ad:
        return None

    # 处理富文本信息
    content = ad.content.replace("[IMG_URL]", IMAGE_URL)

    # 声明结构体
    data = {
        'id': ad.id,
        'title': ad.title,
        'sort_id': ad.sort_id,
        'cover': getImageURL(ad.cover) if ad.cover else "",
        'type': ad.type,
        'type_name': AD_TYPE_LIST.get(ad.type),
        'url': ad.url,
        'width': ad.width,
        'height': ad.height,
        'start_time': str(ad.start_time.strftime('%Y-%m-%d %H:%M:%S')) if ad.start_time else None,
        'end_time': str(ad.end_time.strftime('%Y-%m-%d %H:%M:%S')) if ad.end_time else None,
        'click': ad.click,
        'status': ad.status,
        'note': ad.note,
        'sort': ad.sort,
        'content': content
    }
    # 返回结果
    return data


# 添加广告
def AdAdd(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}".format(e))
        return R.failed("参数错误")

    # 表单验证
    form = forms.AdForm(data=dict_data)
    if form.is_valid():
        # 广告标题
        title = form.cleaned_data.get("title")
        # 广告ID
        sort_id = int(form.cleaned_data.get('sort_id'))
        # 广告URL
        url = form.cleaned_data.get('url')
        # 广告类型：1图片 2文字 3视频 4推荐
        type = form.cleaned_data.get('type')
        # 广告封面
        cover = form.cleaned_data.get('cover')
        if type == 1 and cover:
            cover = saveImage(cover, "ad")
        else:
            cover = None
        # 广告宽度
        width = int(form.cleaned_data.get('width'))
        # 广告高度
        height = int(form.cleaned_data.get('height'))
        # 广告开始时间
        start_time = form.cleaned_data.get("start_time")
        # 广告结束时间
        end_time = form.cleaned_data.get("end_time")
        # 广告状态
        status = form.cleaned_data.get('status')
        # 广告排序
        sort = form.cleaned_data.get('sort')
        # 广告备注
        note = form.cleaned_data.get('note')
        # 广告富文本内容
        content = form.cleaned_data.get('content')

        # 处理富文本内容
        content = saveEditContent(content, title, "ad")

        # 创建数据
        Ad.objects.create(
            title=title,
            sort_id=sort_id,
            type=type,
            cover=cover,
            url=url,
            width=width,
            height=height,
            start_time=start_time,
            end_time=end_time,
            status=status,
            sort=sort,
            note=note,
            content=content,
            create_user=uid(request)
        )
        # 返回结果
        return R.ok(msg="添加成功")
    else:
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)


# 更新广告
def AdUpdate(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
        # 广告ID
        ad_id = dict_data.get('id')
        # 广告ID判空
        if not ad_id or int(ad_id) <= 0:
            return R.failed("广告ID不能为空")
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.AdForm(dict_data)
    if form.is_valid():
        # 广告标题
        title = form.cleaned_data.get("title")
        # 广告位ID
        sort_id = form.cleaned_data.get('sort_id')
        # 广告URL
        url = form.cleaned_data.get('url')
        # 广告类型：1图片 2文字 3视频 4推荐
        type = form.cleaned_data.get('type')
        # 广告封面
        cover = form.cleaned_data.get('cover')
        if type == 1 and cover:
            cover = saveImage(cover, "ad")
        else:
            cover = None
        # 广告宽度
        width = int(form.cleaned_data.get('width'))
        # 广告高度
        height = int(form.cleaned_data.get('height'))
        # 广告开始时间
        start_time = form.cleaned_data.get("start_time")
        # 广告结束时间
        end_time = form.cleaned_data.get("end_time")
        # 广告状态
        status = form.cleaned_data.get('status')
        # 广告排序
        sort = form.cleaned_data.get('sort')
        # 广告备注
        note = form.cleaned_data.get('note')
        # 广告富文本内容
        content = form.cleaned_data.get('content')
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)

    # 根据ID查询广告
    ad = Ad.objects.only('id').filter(id=ad_id, is_delete=False).first()
    # 查询结果判断
    if not ad:
        return R.failed("广告不存在")

    # 处理富文本内容
    content = saveEditContent(content, title, "ad")

    # 对象赋值
    ad.title = title
    ad.sort_id = sort_id
    ad.url = url
    ad.type = type
    ad.cover = cover
    ad.width = width
    ad.height = height
    ad.start_time = start_time
    ad.end_time = end_time
    ad.status = status
    ad.sort = sort
    ad.note = note
    ad.content = content
    ad.update_user = uid(request)

    # 更新数据
    ad.save()
    # 返回结果
    return R.ok(msg="更新成功")


# 删除广告
def AdDelete(ad_id):
    # 记录ID为空判断
    if not ad_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = ad_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for id in list:
            # 根据ID查询记录
            ad = Ad.objects.only('id').filter(id=int(id), is_delete=False).first()
            # 查询结果判空
            if not ad:
                return R.failed("广告位不存在")
            # 设置删除标识
            ad.is_delete = True
            # 更新记录
            ad.save()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 设置状态
def AdStatus(request):
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
    form = forms.AdStatusForm(data=dict_data)
    if form.is_valid():
        # 广告ID
        id = int(form.cleaned_data.get('id'))
        # 广告状态
        status = int(form.cleaned_data.get("status"))
    else:
        # 获取错误描述
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(msg=err_msg)

    # 根据ID查询广告
    ad = Ad.objects.only('id').filter(id=id, is_delete=False).first()
    # 查询结果判空
    if not ad:
        return R.failed("记录不存在")
    # 给对象赋值
    ad.status = status
    # 更新记录
    ad.save()
    # 返回结果
    return R.ok()
