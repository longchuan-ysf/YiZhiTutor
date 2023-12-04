from django.urls import path  # 导入路径相关配置

from application.position import views

# 岗位模块路由
urlpatterns = [
    # 岗位列表页
    path('index', views.PositionView.as_view()),
    # 查询岗位分页列表
    path('list', views.PositionListView.as_view()),
    # 查询岗位详情
    path('edit/<int:position_id>', views.PositionDetailView.as_view()),
    # 添加岗位
    path('add', views.PositionAddView.as_view()),
    # 更新岗位
    path('update', views.PositionUpdateView.as_view()),
    # 删除岗位
    path('delete/<str:position_id>', views.PositionDeleteView.as_view()),
    # 设置状态
    path('status', views.PositionStatusView.as_view())
]
