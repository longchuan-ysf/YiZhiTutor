from django.urls import path

from application.city import views

# 部门模块路由
urlpatterns = [
    # 部门列表页
    path('index', views.CityView.as_view()),
    # 查询部门分页数据
    path('list', views.CityListView.as_view()),
    # 查询部门详情
    path('edit/<int:city_id>', views.CityDetailView.as_view()),
    # 添加部门
    path('add', views.CityAddView.as_view()),
    # 更新部门
    path('update', views.CityUpdateView.as_view()),
    # 删除部门
    path('delete/<str:city_id>', views.CityDeleteView.as_view()),
    # 根据上级ID获取子级城市
    path('getChildList/<str:city_code>', views.CityChildView.as_view()),
]
