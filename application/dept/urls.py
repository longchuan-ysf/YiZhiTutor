from django.urls import path

from application.dept import views

# 部门模块路由
urlpatterns = [
    # 部门列表页
    path('index', views.DeptView.as_view()),
    # 查询部门分页数据
    path('list', views.DeptListView.as_view()),
    # 查询部门详情
    path('edit/<int:dept_id>', views.DeptDetailView.as_view()),
    # 添加部门
    path('add', views.DeptAddView.as_view()),
    # 更新部门
    path('update', views.DeptUpdateView.as_view()),
    # 删除部门
    path('delete/<str:dept_id>', views.DeptDeleteView.as_view())
]
