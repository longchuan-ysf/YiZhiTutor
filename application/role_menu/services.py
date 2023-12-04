import json
import logging

from application.menu.models import Menu
from application.role_menu import forms

from application.role_menu.models import RoleMenu

from utils import R, regular


# 根据角色ID查询菜单列表
def getRoleMenuList(role_id):
    # 获取全部菜单列表
    menuList = Menu.objects.filter(is_delete=False, status=1).order_by("sort").values()
    if len(menuList) == 0:
        return None
    # 根据角色ID查询角色菜单关系数据
    role_menu = RoleMenu.objects.filter(role_id=role_id).values()
    # 菜单ID集合
    idList = []
    # 遍历角色菜单数据源
    if role_menu:
        for v in role_menu:
            # 加入数组
            idList.append(v['menu_id'])

    # 实例化菜单列表
    list = []
    # 遍历菜单数据
    for menu in menuList:
        # 菜单ID
        menu_id = menu['id']
        data = {
            'id': menu_id,
            'name': menu['name'],
            'open': True,
            'pId': menu['pid'],
        }
        if menu_id in idList:
            data['checked'] = True
        # 加入数组
        list.append(data)
    # 返回结果
    return list


# 保存角色菜单数据
def save(request):
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
    form = forms.RoleMenuForm(dict_data)
    if form.is_valid():
        # 角色ID
        role_id = form.cleaned_data.get('role_id')
        # 菜单ID
        menuIds = form.cleaned_data.get('menu_id')

        # 删除当前角色ID相关菜单权限
        RoleMenu.objects.filter(role_id=role_id).delete()

        # 处理菜单数据
        if menuIds != "":
            menuIdList = menuIds.split(',')
            # 遍历菜单ID数据源
            if len(menuIdList) > 0:
                for menu_id in menuIdList:
                    if menu_id == "":
                        continue
                    # 创建角色菜单数据
                    RoleMenu.objects.create(
                        role_id=role_id,
                        menu_id=menu_id
                    )
        # 返回结果
        return R.ok()
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)
