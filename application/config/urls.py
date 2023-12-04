from django.urls import path

from application.config import views

# 配置模块路由
urlpatterns = [
    # 配置列表页
    path('index', views.ConfigView.as_view()),
    # 查询配置分页列表
    path('list', views.ConfigListView.as_view()),
    # 查询配置详情
    path('edit/<int:config_id>', views.ConfigDetailView.as_view()),
    # 添加配置
    path('add', views.ConfigAddView.as_view()),
    # 更新配置
    path('update', views.ConfigUpdateView.as_view()),
    # 删除配置
    path('delete/<str:config_id>', views.ConfigDeleteView.as_view()),
]
