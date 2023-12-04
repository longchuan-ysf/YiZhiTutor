from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

import application.menu.services

from utils import R


# 鉴权中间件
class PermissionRequired(PermissionRequiredMixin):

    def has_permission(self):
        # 获取方法节点权限标识
        permissions = self.get_permission_required()
        # 用户ID
        user_id = self.request.session.get('user_id')
        if user_id != 1:
            # 获取用户权限节点
            permission_list = application.menu.services.GetPermissionsList(user_id)
            for permission in permissions:
                if permission not in permission_list:
                    # 无节点权限，禁止放行
                    return False
        # 直接放行
        return True

    # 没有权限时候的报错回调
    def handle_no_permission(self):
        if self.request.path.find('index') != -1:
            return render(self.request, '403.html')
        else:
            return R.failed("暂无操作权限")
