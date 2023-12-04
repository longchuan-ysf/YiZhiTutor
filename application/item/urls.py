from django.urls import path

from application.item import views

# 站点模块路由
urlpatterns = [
    # 站点列表页
    path('index', views.ItemView.as_view()),
    # 查询站点分页数据
    path('list', views.ItemListView.as_view()),
    # 查询站点详情
    path('edit/<int:item_id>', views.ItemDetailView.as_view()),
    # 添加站点
    path('add', views.ItemAddView.as_view()),
    # 更新站点
    path('update', views.ItemUpdateView.as_view()),
    # 删除站点
    path('delete/<str:item_id>', views.ItemDeleteView.as_view()),
]
