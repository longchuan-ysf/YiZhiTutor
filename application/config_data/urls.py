from django.urls import path

from application.config_data import views

# 配置项模块路由
urlpatterns = [
    # 查询配置项分页列表
    path('list', views.ConfigDataListView.as_view()),
    # 查询配置项详情
    path('edit/<int:config_id>', views.ConfigDataDetailView.as_view()),
    # 添加配置项
    path('add', views.ConfigDataAddView.as_view()),
    # 更新配置项
    path('update', views.ConfigDataUpdateView.as_view()),
    # 删除配置项
    path('delete/<str:config_id>', views.ConfigDataDeleteView.as_view()),
    # 设置状态
    path('status', views.ConfigDataStatusView.as_view()),
]
