import json
import logging

from application.menu import forms
from application.menu.models import Menu

from utils import R, regular

# 获取菜单数据
from utils.utils import uid


def MenuList(request):
    # 实例化查询对象
    query = Menu.objects.filter(is_delete=False)
    # 菜单名称
    name = request.GET.get('name')
    if name:
        # 菜单名称模糊查询
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
                'icon': item.icon,
                'url': item.url,
                'pid': item.pid,
                'type': item.type,
                'permission': item.permission,
                'status': item.status,
                'target': item.target,
                'sort': item.sort,
                'note': item.note,
                'create_time': str(item.create_time.strftime('%Y-%m-%d %H:%M:%S')) if item.create_time else None,
                'update_time': str(item.update_time.strftime('%Y-%m-%d %H:%M:%S')) if item.update_time else None,
            }
            result.append(data)
    # 返回结果
    return R.ok(data=result)


# 根据ID查询菜单详情
def MenuDetail(menu_id):
    # 根据ID查询菜单
    menu = Menu.objects.filter(id=menu_id, is_delete=False).first()
    # 查询结果判空
    if not menu:
        return None
    # 实例化结构体
    data = {
        'id': menu.id,
        'name': menu.name,
        'icon': menu.icon,
        'url': menu.url,
        'pid': menu.pid,
        'type': menu.type,
        'permission': menu.permission,
        'status': menu.status,
        'target': menu.target,
        'sort': menu.sort,
        'note': menu.note,
    }
    # 返回结果
    return data


# 添加菜单
def MenuAdd(request):
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
    form = forms.MenuForm(data=dict_data)
    if form.is_valid():
        # 菜单名称
        name = form.cleaned_data.get('name')
        # 菜单图标
        icon = form.cleaned_data.get('icon')
        # 菜单URL
        url = form.cleaned_data.get('url')
        # 上级ID
        pid = form.cleaned_data.get('pid')
        # 菜单类型
        type = form.cleaned_data.get('type')
        # 权限节点
        permission = form.cleaned_data.get('permission')
        # 状态
        status = form.cleaned_data.get('status')
        # 打开方式
        target = form.cleaned_data.get('target')
        # 菜单排序
        sort = form.cleaned_data.get('sort')
        # 备注
        note = form.cleaned_data.get('note')
        # 权限节点
        func = form.cleaned_data.get('func')
        # 创建数据
        menu = Menu.objects.create(
            name=name,
            icon=icon,
            url=url,
            pid=pid if pid else 0,
            type=type,
            permission=permission,
            status=status,
            target=target,
            sort=sort,
            note=note,
            create_user=uid(request)
        )

        # 保存节点数据
        setPermission(type, func, name, url, menu.id, uid(request))

        # 返回结果
        return R.ok(msg="创建成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)


# 更新菜单
def MenuUpdate(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数判空
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
        # 菜单ID
        menu_id = dict_data.get('id')
        # 菜单ID判空
        if not menu_id:
            return R.failed("菜单ID不能为空")
    except Exception as e:
        logging.info("参数错误：\n{}", format(e))
        return R.failed("参数错误")

    # 表单验证
    form = forms.MenuForm(dict_data)
    if form.is_valid():
        # 菜单名称
        name = form.cleaned_data.get('name')
        # 菜单图标
        icon = form.cleaned_data.get('icon')
        # 菜单URL
        url = form.cleaned_data.get('url')
        # 上级ID
        pid = form.cleaned_data.get('pid')
        # 菜单类型
        type = form.cleaned_data.get('type')
        # 权限节点
        permission = form.cleaned_data.get('permission')
        # 状态
        status = form.cleaned_data.get('status')
        # 打开方式
        target = form.cleaned_data.get('target')
        # 菜单排序
        sort = form.cleaned_data.get('sort')
        # 备注
        note = form.cleaned_data.get('note')
        # 权限节点
        func = form.cleaned_data.get('func')
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)

    # 根据ID查询菜单
    menu = Menu.objects.only('id').filter(id=menu_id, is_delete=False).first()
    # 查询结果判空
    if not menu:
        return R.failed("菜单不存在")

    # 对象赋值
    menu.name = name
    menu.icon = icon
    menu.url = url
    menu.pid = pid
    menu.type = type
    menu.permission = permission
    menu.status = status
    menu.target = target
    menu.sort = sort
    menu.note = note
    menu.update_user = uid(request)
    # 更新数据
    menu.save()

    # 保存节点数据
    setPermission(type, func, name, url, menu.id, uid(request))

    # 返回结果
    return R.ok(msg="更新成功")


# 删除菜单
def MenuDelete(menu_id):
    # 记录ID为空判断
    if not menu_id:
        return R.failed("记录ID不存在")
    # 分裂字符串
    list = menu_id.split(',')
    # 计数器
    count = 0
    # 遍历数据源
    if len(list) > 0:
        for id in list:
            # 根据ID查询记录
            menu = Menu.objects.only('id').filter(id=int(id), is_delete=False).first()
            # 查询结果判空
            if not menu:
                return R.failed("菜单不存在")
            # 设置删除标识
            menu.is_delete = True
            # 更新记录
            menu.save()
            # 计数器+1
            count += 1
    # 返回结果
    return R.ok(msg="本次共删除{0}条数据".format(count))


# 保存节点数据
def setPermission(menuType, funcIds, name, url, parentId, userId):
    # 参数判空
    if menuType != 0 or funcIds == "" or url == "":
        return
    # 删除现有节点
    Menu.objects.filter(is_delete=False, pid=parentId).delete()
    # 模块名称
    moduleTitle = name.replace("管理", "")
    # 请求URL处理
    urlArr = url.split('/')
    if len(urlArr) < 3:
        return
    # 模块名
    moduleName = urlArr[len(urlArr) - 2]
    # 节点处理
    checkedList = funcIds.split(',')
    # 遍历数据源
    for v in checkedList:
        # 实例化菜单对象
        entity = Menu()
        # 节点值
        value = int(v)
        if value == 1:
            # 查询
            entity.name = "查询" + moduleTitle
            entity.url = "/" + moduleName + "/list"
            entity.permission = "sys:" + moduleName + ":list"
        elif value == 5:
            # 添加
            entity.name = "添加" + moduleTitle
            entity.url = "/" + moduleName + "/add"
            entity.permission = "sys:" + moduleName + ":add"
        elif value == 10:
            # 修改
            entity.name = "修改" + moduleTitle
            entity.url = "/" + moduleName + "/update"
            entity.permission = "sys:" + moduleName + ":update"
        elif value == 15:
            # 删除
            entity.name = "删除" + moduleTitle
            entity.url = "/" + moduleName + "/delete"
            entity.permission = "sys:" + moduleName + ":delete"
        elif value == 20:
            # 详情
            entity.name = moduleTitle + "详情"
            entity.url = "/" + moduleName + "/detail"
            entity.permission = "sys:" + moduleName + ":detail"
        elif value == 25:
            # 设置状态
            entity.name = "设置状态"
            entity.url = "/" + moduleName + "/status"
            entity.permission = "sys:" + moduleName + ":status"
        elif value == 30:
            # 批量删除
            entity.name = "批量删除"
            entity.url = "/" + moduleName + "/dall"
            entity.permission = "sys:" + moduleName + ":dall"
        elif value == 35:
            # 添加子级
            entity.name = "添加子级"
            entity.url = "/" + moduleName + "/addz"
            entity.permission = "sys:" + moduleName + ":addz"
        elif value == 40:
            # 全部展开
            entity.name = "全部展开"
            entity.url = "/" + moduleName + "/expand"
            entity.permission = "sys:" + moduleName + ":expand"
        elif value == 45:
            # 全部折叠
            entity.name = "全部折叠"
            entity.url = "/" + moduleName + "/collapse"
            entity.permission = "sys:" + moduleName + ":collapse"
        elif value == 50:
            # 导出数据
            entity.name = "导出" + moduleTitle
            entity.url = "/" + moduleName + "/export"
            entity.permission = "sys:" + moduleName + ":export"
        elif value == 55:
            # 导入数据
            entity.name = "导入" + moduleTitle
            entity.url = "/" + moduleName + "/import"
            entity.permission = "sys:" + moduleName + ":import"
        elif value == 60:
            # 分配权限
            entity.name = "分配权限"
            entity.url = "/" + moduleName + "/permission"
            entity.permission = "sys:" + moduleName + ":permission"
        elif value == 65:
            # 重置密码
            entity.name = "重置密码"
            entity.url = "/" + moduleName + "/resetPwd"
            entity.permission = "sys:" + moduleName + ":resetPwd"

        # 设置默认值
        entity.pid = parentId
        entity.type = 1
        entity.status = 1
        entity.target = 1
        entity.sort = value
        entity.create_user = userId
        # 插入数据
        entity.save()


# 获取用户权限节点
def GetPermissionsList(user_id):
    sql = 'SELECT m.* FROM django_menu AS m '
    sql += 'INNER JOIN django_role_menu AS rm ON m.id=rm.menu_id '
    sql += 'INNER JOIN django_user_role AS ur ON ur.role_id=rm.role_id '
    sql += 'WHERE ur.user_id=%s AND (m.type=1 OR (m.type=0 AND m.permission!="")) AND m.`status`=1 AND m.is_delete=0'
    list = Menu.objects.raw(sql, [user_id])
    permission_list = []
    if list:
        for item in list:
            permission_list.append(item.permission)
    # 返回结果
    return permission_list


# 根据用户ID查询菜单列表
def GetPermissionMenuList(user_id):
    if user_id == 1:
        # 超级管理员
        # 查询全部菜单列表
        list = Menu.objects.filter(is_delete=False, status=1, type=0).order_by("sort")
        menu_list = GetTreeList(list)
        return menu_list
    else:
        # 其他用户
        sql = 'SELECT m.* FROM django_menu AS m '
        sql += 'INNER JOIN django_role_menu AS rm ON m.id=rm.menu_id '
        sql += 'INNER JOIN django_user_role AS ur ON ur.role_id=rm.role_id '
        sql += 'WHERE ur.user_id=%s AND m.type=0 AND m.`status`=1 AND m.is_delete=0 '
        sql += 'ORDER BY m.sort ASC;'
        list = Menu.objects.raw(sql, [user_id])
        menu_list = GetTreeList(list)
        return menu_list


# 根据数据源获取树状结构
def GetTreeList(list):
    # 实例化数组
    menu_list = []
    if list:
        for item in list:
            data = {
                'id': item.id,
                'name': item.name,
                'icon': item.icon,
                'url': item.url,
                'pid': item.pid,
                'type': item.type,
                'permission': item.permission,
                'target': item.target,
            }
            menu_list.append(data)
    # 处理数据源为树状结构
    result = get_tree(menu_list, 0)
    # 返回结果
    return result


# 获取树状结构,当树的层级较深时，递归就不太适合
def get_tree(data, pid):
    result = []
    for item in data:
        if pid != item["pid"]:
            continue
        # 递归调用
        temp = get_tree(data, item["id"])
        if (len(temp) > 0):
            item["children"] = temp
        else:
            item["children"] = []
        # 加入数组
        result.append(item)
    # 返回结果
    return result


# 获取菜单树状下拉结构
def MakeList():
    # 查询全部菜单列表
    menuList = Menu.objects.filter(is_delete=0, type=0).order_by("sort")
    # 获取树状结构
    list = GetTreeList(menuList)
    # 实例化数组
    menu_list = {}
    # 遍历一级数据源
    for val in list:
        menu_list[val['id']] = val['name']
        # 遍历二级数据源
        for v in val['children']:
            menu_list[v['id']] = "|--" + v['name']
            # 遍历三级数据源
            for vt in v['children']:
                menu_list[vt['id']] = "|--|--" + vt['name']
    # 返回结果
    return menu_list
