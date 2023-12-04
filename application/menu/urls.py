from django.urls import path  # 导入路径相关配置

from application.menu import views

# 菜单模块路由
urlpatterns = [
    # 菜单列表页
    path('index', views.MenuView.as_view()),
    # 查询菜单分页列表
    path('list', views.MenuListView.as_view()),
    # 查询菜单详情
    path('edit/<int:menu_id>', views.MenuDetailView.as_view()),
    # 添加菜单
    path('add', views.MenuAddView.as_view()),
    # 更新菜单
    path('update', views.MenuUpdateView.as_view()),
    # 删除菜单
    path('delete/<str:menu_id>', views.MenuDeleteView.as_view()),
]
