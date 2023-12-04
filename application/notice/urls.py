from django.urls import path  # 导入路径相关配置

from application.notice import views

# 通知公告模块路由
urlpatterns = [
    # 通知公告列表页
    path('index', views.NoticeView.as_view()),
    # 查询通知公告分页列表
    path('list', views.NoticeListView.as_view()),
    # 查询通知公告详情
    path('edit/<int:notice_id>', views.NoticeDetailView.as_view()),
    # 添加通知公告
    path('add', views.NoticeAddView.as_view()),
    # 更新通知公告
    path('update', views.NoticeUpdateView.as_view()),
    # 删除通知公告
    path('delete/<str:notice_id>', views.NoticeDeleteView.as_view()),
]
