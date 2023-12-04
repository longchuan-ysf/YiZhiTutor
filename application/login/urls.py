from django.urls import path  # 导入路径相关配置

from application.login import views

# 登录模块路由
urlpatterns = [
    # 登录页
    path('login', views.LoginView.as_view()),
    # 验证码
    path('captcha', views.CaptchaView.as_view()),
]
