from django.urls import path  # 导入路径相关配置

from application.member import views

# 会员模块路由
urlpatterns = [
    # 用户列表页
    path('index', views.MemberView.as_view()),
    # 查询用户分页列表
    path('list', views.MemberListView.as_view()),
    # 查询用户详情
    path('edit/<int:member_id>', views.MemberDetailView.as_view()),
    # 添加用户
    path('add', views.MemberAddView.as_view()),
    # 更新用户
    path('update', views.MemberUpdateView.as_view()),
    # 删除用户
    path('delete/<str:member_id>', views.MemberDeleteView.as_view()),
    # 设置状态
    path('status', views.MemberStatusView.as_view())
]
