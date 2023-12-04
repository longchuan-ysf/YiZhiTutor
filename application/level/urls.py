from django.urls import path  # 导入路径相关配置

from application.level import views

# 职级模块路由
urlpatterns = [
    # 职级列表页
    path('index', views.LevelView.as_view()),
    # 查询职级分页数据
    path('list', views.LevelListView.as_view()),
    # 根据ID查询职级详情
    path('edit/<int:level_id>', views.LevelDetailView.as_view()),
    # 添加职级
    path('add', views.LevelAddView.as_view()),
    # 更新职级
    path('update', views.LevelUpdateView.as_view()),
    # 根据ID删除职级
    path('delete/<str:level_id>', views.LevelDeleteView.as_view()),
    # 设置状态
    path('status', views.LevelStatusView.as_view()),
    # 导入职级数据
    path('import', views.LevelImportView.as_view()),
    # 导出职级数据
    path('export', views.LevelExportView.as_view())
]
