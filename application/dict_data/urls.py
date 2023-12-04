from django.urls import path

from application.dict_data import views

# 字典项模块路由
urlpatterns = [
    # 查询字典项分页列表
    path('list', views.DictDataListView.as_view()),
    # 查询字典项详情
    path('edit/<int:dict_id>', views.DictDataDetailView.as_view()),
    # 添加字典项
    path('add', views.DictDataAddView.as_view()),
    # 更新字典项
    path('update', views.DictDataUpdateView.as_view()),
    # 删除字典项
    path('delete/<str:dict_id>', views.DictDataDeleteView.as_view()),
]
