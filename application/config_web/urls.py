from django.urls import path

from application.config_web import views

# 网站配置模块路由
urlpatterns = [
    # 首页
    path('index', views.ConfigWebView.as_view()),
]
