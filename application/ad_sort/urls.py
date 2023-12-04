from django.urls import path

from application.ad_sort import views

# 广告位路由
urlpatterns = [
    # 广告位列表页
    path('index', views.AdSortView.as_view()),
    # 查询广告位分页列表
    path('list', views.AdSortListView.as_view()),
    # 查询广告位详情
    path('edit/<int:adsort_id>', views.AdSortDetailView.as_view()),
    # 添加广告位
    path('add', views.AdSortAddView.as_view()),
    # 更新广告位
    path('update', views.AdSortUpdateView.as_view()),
    # 删除广告位
    path('delete/<str:adsort_id>', views.AdSortDeleteView.as_view()),
]
