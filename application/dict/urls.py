from django.urls import path

from application.dict import views

# 字典模块路由
urlpatterns = [
    # 字典列表页
    path('index', views.DictView.as_view()),
    # 查询字典分页列表
    path('list', views.DictListView.as_view()),
    # 查询字典详情
    path('edit/<int:dict_id>', views.DictDetailView.as_view()),
    # 添加字典
    path('add', views.DictAddView.as_view()),
    # 更新字典
    path('update', views.DictUpdateView.as_view()),
    # 删除字典
    path('delete/<str:dict_id>', views.DictDeleteView.as_view()),
]
