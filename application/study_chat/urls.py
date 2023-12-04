from django.urls import path

from application.study_chat import views

# 角色菜单模块路由
urlpatterns = [
    # 获取角色菜单数据
    path('index', views.ChatIndexView.as_view()),
    path('submit', views.ChatSubmitView.as_view()),


]
