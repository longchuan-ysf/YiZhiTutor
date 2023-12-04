import json
import logging

from application.dept import forms
from application.dept.models import Dept
from utils import R, regular

# 查询部门分页数据
from utils.utils import uid


def DeptList(request):
    # 实例化查询对象
    query = Dept.objects.filter(is_delete=False)
    # 部门名称
    name = request.GET.get('name')
    if name:
        # 部门名称模糊查询
        query = query.filter(name__contains=name)
    # 查询数据
    list = query.order_by('sort').all()

    # 实例化数组对象
    result = []
    # 遍历数据源
    if list:
        for item in list:
            data = {
                'id': item.id,
                'name': item.name,
                'code': item.code,
                'type': item.type,
                'pid': item.pid,
                'sort': item.sort,
                'note': item.note,
                'create_time': str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None,
                'update_time': str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None,
            }
            result.append(data)
    # 返回结果
    return R.ok(data=result)


# 根据ID查询部门
def DeptDetail(dept_id):
    # 根据ID查询部门
    dept = Dept.objects.filter(id=dept_id, is_delete=False).first()
    # 查询结果判空
    if not dept:
        return None
    # 实例化结构体
    data = {
        'id': dept.id,
        'name': dept.name,
        'code': dept.code,
        'type': dept.type,
        'pid': dept.pid,
        'sort': dept.sort,
        'note': dept.note
    }
    # 返回结果
    return data


# 添加部门
def DeptAdd(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数判空
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")

    # 表单验证
    form = forms.DeptForm(data=dict_data)
    if form.is_valid():
        # 部门名称
        name = form.cleaned_data.get('name')
        # 部门编码
        code = form.cleaned_data.get('code')
        # 部门类型
        type = form.cleaned_data.get('type')
        # 上级部门ID
        pid = form.cleaned_data.get('pid')
        # 部门排序
        sort = form.cleaned_data.get('sort')
        # 备注
        note = form.cleaned_data.get('note')
        # 创建数据
        Dept.objects.create(
            name=name,
            code=code,
            type=type,
            pid=pid,
            sort=sort,
            note=note,
            create_user=uid(request)
        )
        # 返回结果
        return R.ok(msg="创建成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)


# 更新部门
def DeptUpdate(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数判空
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
        # 部门ID
        dept_id = dict_data.get('id')
        # 部门ID判空
        if not dept_id:
            return R.failed("部门ID不能为空")
    except Exception as e:
        logging.info("参数错误：\n{}", format(e))
        return R.failed("参数错误")

    # 表单验证
    form = forms.DeptForm(dict_data)
    if form.is_valid():
        # 部门名称
        name = form.cleaned_data.get('name')
        # 部门编码
        code = form.cleaned_data.get('code')
        # 部门类型
        type = form.cleaned_data.get('type')
        # 部门上级ID
        pid = form.cleaned_data.get('pid')
        # 部门排序
        sort = form.cleaned_data.get('sort')
        # 部门备注
        note = form.cleaned_data.get('note')
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)

    # 根据ID查询部门
    dept = Dept.objects.only('id').filter(id=dept_id, is_delete=False).first()
    # 查询结果判空
    if not dept:
        return R.failed("部门不存在")

    # 对象赋值
    dept.name = name
    dept.code = code
    dept.type = type
    dept.pid = pid
    dept.sort = sort
    dept.note = note
    dept.update_user = uid(request)
    # 更新数据
    dept.save()
    # 返回结果
    return R.ok(msg="更新成功")


# 删除部门
def DeptDelete(dept_id):
    # 记录ID为空判断
    if not dept_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = dept_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for id in list:
            # 根据ID查询记录
            dept = Dept.objects.only('id').filter(id=int(id), is_delete=False).first()
            # 查询结果判空
            if not dept:
                return R.failed("部门不存在")
            # 设置删除标识
            dept.is_delete = True
            # 更新记录
            dept.save()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))
