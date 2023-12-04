from django.urls import path

from application.role import views

# 角色模块路由
urlpatterns = [
    # 角色列表页
    path('index', views.RoleView.as_view()),
    # 查询角色分页数据
    path('list', views.RoleListView.as_view()),
    # 根据ID查询角色详情
    path('edit/<int:role_id>', views.RoleDetailView.as_view()),
    # 添加角色
    path('add', views.RoleAddView.as_view()),
    # 更新角色
    path('update', views.RoleUpdateView.as_view()),
    # 根据ID删除角色
    path('delete/<str:role_id>', views.RoleDeleteView.as_view()),
    # 设置状态
    path('status', views.RoleStatusView.as_view()),
]
