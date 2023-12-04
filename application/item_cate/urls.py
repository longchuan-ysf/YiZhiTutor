from django.urls import path

from application.item_cate import views

# 栏目模块路由
urlpatterns = [
    # 站点列表页
    path('index', views.ItemCateView.as_view()),
    # 查询站点分页数据
    path('list', views.ItemCateListView.as_view()),
    # 查询站点详情
    path('edit/<int:item_id>', views.ItemCateDetailView.as_view()),
    # 添加站点
    path('add', views.ItemCateAddView.as_view()),
    # 更新站点
    path('update', views.ItemCateUpdateView.as_view()),
    # 删除站点
    path('delete/<str:item_id>', views.ItemCateDeleteView.as_view()),
    # 获取栏目树结构
    path('getCateTreeList/<int:item_id>', views.ItemCateTreeView.as_view()),
]
