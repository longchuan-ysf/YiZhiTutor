from django.urls import path  # 导入路径相关配置

from application.user import views

# 用户模块路由
urlpatterns = [
    # 用户列表页
    path('index', views.UserView.as_view()),
    # 查询用户分页列表
    path('list', views.UserListView.as_view()),
    # 查询用户详情
    path('edit/<int:user_id>', views.UserDetailView.as_view()),
    # 添加用户
    path('add', views.UserAddView.as_view()),
    # 更新用户
    path('update', views.UserUpdateView.as_view()),
    # 删除用户
    path('delete/<str:user_id>', views.UserDeleteView.as_view()),
    # 设置状态
    path('status', views.UserStatusView.as_view()),
    # 重置密码
    path('resetPwd', views.UserResetPwdView.as_view())
]
