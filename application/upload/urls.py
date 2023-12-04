from django.urls import path  # 导入路径相关配置

from application.upload import views

# 文件上传路由
urlpatterns = [
    # 上传图片
    path('uploadImage', views.uploadImage.as_view()),
    # 上传富文本图片
    path('uploadEditImage', views.uploadEditImage.as_view()),
]
