from django.urls import path

from application.ad import views

# 广告路由
urlpatterns = [
    # 广告列表页
    path('index', views.AdView.as_view()),
    # 查询广告分页列表
    path('list', views.AdListView.as_view()),
    # 查询广告详情
    path('edit/<int:ad_id>', views.AdDetailView.as_view()),
    # 添加广告
    path('add', views.AdAddView.as_view()),
    # 更新广告
    path('update', views.AdUpdateView.as_view()),
    # 删除广告
    path('delete/<str:ad_id>', views.AdDeleteView.as_view()),
    # 设置状态
    path('status', views.AdStatusView.as_view()),
]
