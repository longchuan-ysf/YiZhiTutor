from django.urls import path  # 导入路径相关配置

from application.index import views

# 登录模块路由
urlpatterns = [
    # 登录页
    path('', views.IndexView.as_view()),
    path('index', views.IndexView.as_view()),
    # 欢迎页
    path('main', views.MainView.as_view()),
    # 个人中心
    path('userInfo', views.UserInfoView.as_view()),
    # 更新密码
    path('updatePwd', views.UpdatePwdView.as_view()),
    # 验证码
    path('logout', views.LogoutView.as_view()),
]
