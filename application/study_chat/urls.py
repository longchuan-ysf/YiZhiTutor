from django.urls import path

from application.study_chat import views

# 角色菜单模块路由
urlpatterns = [
    # 获取角色菜单数据
    path('index', views.ChatIndexView.as_view()),
    # 用户提交对话
    path('submit_txt', views.ChatSubmitTxtView.as_view()),
    # 用户切换对话主题
    path('thematic', views.ThematicChangeView.as_view()),
    path('thematic_add', views.ThematicAddView.as_view()),

    # 小业务的处理
    path('ocr_request', views.OCRView.as_view()),


]
