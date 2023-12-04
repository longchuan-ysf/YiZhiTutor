"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 系统主页
    path('', include('application.index.urls')),
    # 登录页
    path('', include('application.login.urls')),
    # 文件上传
    path('upload/', include('application.upload.urls')),
    # 使用include函数，level.urls为业务模块里的urls包
    # 职级总路由
    path('level/', include('application.level.urls')),
    # 岗位总路由
    path('position/', include('application.position.urls')),
    # 部门总路由
    path('dept/', include('application.dept.urls')),
    # 角色总路由
    path('role/', include('application.role.urls')),
    # 角色菜单总路由
    path('rolemenu/', include('application.role_menu.urls')),
    # 城市总路由
    path('city/', include('application.city.urls')),
    # 站点总路由
    path('item/', include('application.item.urls')),
    # 栏目总路由
    path('itemcate/', include('application.item_cate.urls')),
    # 友链总路由
    path('link/', include('application.link.urls')),
    # 广告位总路由
    path('adsort/', include('application.ad_sort.urls')),
    # 广告总路由
    path('ad/', include('application.ad.urls')),
    # 会员等级总路由
    path('memberlevel/', include('application.member_level.urls')),
    # 会员总路由
    path('member/', include('application.member.urls')),
    # 通知公告总路由
    path('notice/', include('application.notice.urls')),
    # 用户总路由
    path('user/', include('application.user.urls')),
    # 字典总路由
    path('dict/', include('application.dict.urls')),
    # 字典项总路由
    path('dictdata/', include('application.dict_data.urls')),
    # 配置总路由
    path('config/', include('application.config.urls')),
    # 配置项总路由
    path('configdata/', include('application.config_data.urls')),
    # 菜单总路由
    path('menu/', include('application.menu.urls')),
    # 统计总路由
    path('analysis/', include('application.analysis.urls')),
    # 网站配置总路由
    path('configweb/', include('application.config_web.urls')),
    # 问答相关路由
    path('chat/', include('application.study_chat.urls')),
]
