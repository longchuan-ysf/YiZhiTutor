from django.urls import path

from application.role_menu import views

# 角色菜单模块路由
urlpatterns = [
    # 获取角色菜单数据
    path('index/<int:role_id>', views.RoleMenuView.as_view()),
    # 保存角色菜单数据
    path('save', views.RoleMenuSaveView.as_view()),
]
