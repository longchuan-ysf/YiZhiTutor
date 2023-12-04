import json
import logging

from django.core.paginator import Paginator

from application.constants import NOTICE_SOURCE_LIST
from application.notice import forms
from application.notice.models import Notice
from config.env import IMAGE_URL
from constant.constants import PAGE_LIMIT
from utils import R, regular

from utils.utils import saveEditContent, uid


# 查询通知公告分页数据
def NoticeList(request):
    # 页码
    page = int(request.GET.get("page", 1))
    # 每页数
    limit = int(request.GET.get("limit", PAGE_LIMIT))
    # 实例化查询对象
    query = Notice.objects.filter(is_delete=False)
    # 通知公告标题
    title = request.GET.get('title')
    if title:
        query = query.filter(title__contains=title)
    # 通知来源：1官方平台 2开源中国 3CSDN官方 4新浪微博
    source = request.GET.get('source')
    if source:
        query = query.filter(source=source)
    # 通知状态：1-正常 2-停用
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
    notice_list = paginator.page(page)
    # 实例化结果
    result = []
    # 遍历数据源
    if len(notice_list) > 0:
        for item in notice_list:
            data = {
                'id': item.id,
                'title': item.title,
                'source': item.source,
                'source_name': NOTICE_SOURCE_LIST.get(item.source),
                'url': item.url,
                'status': item.status,
                'is_top': item.is_top,
                'content': item.content,
                'click': item.click,
                'create_time': str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None,
                'update_time': str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None,
            }
            result.append(data)
    # 返回结果
    return R.ok(data=result, count=count)


# 根据通知ID查询详情
def NoticeDetail(notice_id):
    # 根据ID查询通知公告
    notice = Notice.objects.filter(is_delete=False, id=notice_id).first()
    # 查询结果判空
    if not notice:
        return None

    # 处理富文本信息
    content = notice.content.replace("[IMG_URL]", IMAGE_URL)

    # 声明结构体
    data = {
        'id': notice.id,
        'title': notice.title,
        'source': notice.source,
        'source_name': NOTICE_SOURCE_LIST.get(notice.source),
        'url': notice.url,
        'status': notice.status,
        'is_top': notice.is_top,
        'content': content,
        'click': notice.click,
    }
    # 返回结果
    return data


# 添加通知公告
def NoticeAdd(request):
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
    form = forms.NoticeForm(dict_data)
    if form.is_valid():
        # 通知公告名称
        title = form.cleaned_data.get('title')
        # 通知来源
        source = form.cleaned_data.get('source')
        # 外部链接
        url = form.cleaned_data.get('url')
        # 通知状态
        status = form.cleaned_data.get('status')
        # 是否置顶
        is_top = form.cleaned_data.get('is_top')
        # 通知内容
        content = form.cleaned_data.get('content')
        # 点击率
        click = form.cleaned_data.get('click')

        # 处理富文本内容
        content = saveEditContent(content, title, "notice")

        # 创建数据
        Notice.objects.create(
            title=title,
            source=source,
            url=url,
            status=status,
            is_top=is_top,
            content=content,
            click=click,
            create_user=uid(request)
        )
        # 返回结果
        return R.ok(msg="创建成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)


# 更新通知公告
def NoticeUpdate(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
        # 通知公告ID
        notice_id = dict_data.get('id')
        # 通知公告ID判空
        if not notice_id or int(notice_id) <= 0:
            return R.failed("通知公告ID不能为空")
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.NoticeForm(dict_data)
    if form.is_valid():
        # 通知公告名称
        title = form.cleaned_data.get('title')
        # 通知来源
        source = form.cleaned_data.get('source')
        # 外部链接
        url = form.cleaned_data.get('url')
        # 通知状态
        status = form.cleaned_data.get('status')
        # 是否置顶
        is_top = form.cleaned_data.get('is_top')
        # 通知内容
        content = form.cleaned_data.get('content')
        # 点击率
        click = form.cleaned_data.get('click')
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)

    # 根据ID查询通知公告
    notice = Notice.objects.only('id').filter(id=notice_id, is_delete=False).first()
    # 查询结果判断
    if not notice:
        return R.failed("通知公告不存在")

    # 处理富文本内容
    content = saveEditContent(content, title, "notice")

    # 对象赋值
    notice.title = title
    notice.source = source
    notice.url = url
    notice.status = status
    notice.is_top = is_top
    notice.content = content
    notice.click = click
    notice.update_user = uid(request)

    # 更新数据
    notice.save()
    # 返回结果
    return R.ok(msg="更新成功")


# 删除通知公告
def NoticeDelete(notice_id):
    # 记录ID为空判断
    if not notice_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = notice_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for id in list:
            # 根据ID查询记录
            notice = Notice.objects.only('id').filter(id=int(id), is_delete=False).first()
            # 查询结果判空
            if not notice:
                return R.failed("通知公告不存在")
            # 设置删除标识
            notice.is_delete = True
            # 更新记录
            notice.save()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))
