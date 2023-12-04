from django.urls import path

from application.link import views

# 栏目模块路由
urlpatterns = [
    # 友链列表页
    path('index', views.LinkView.as_view()),
    # 查询友链分页数据
    path('list', views.LinkListView.as_view()),
    # 查询友链详情
    path('edit/<int:link_id>', views.LinkDetailView.as_view()),
    # 添加友链
    path('add', views.LinkAddView.as_view()),
    # 更新友链
    path('update', views.LinkUpdateView.as_view()),
    # 删除友链
    path('delete/<str:link_id>', views.LinkDeleteView.as_view()),
    # 设置状态
    path('status', views.LinkStatusView.as_view()),
]
