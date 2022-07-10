"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# 路由导航
from django.contrib import admin
from django.urls import path,include,re_path

# 路由总表
urlpatterns = [
    path('admin/', admin.site.urls),

    # 创建前往sales的路由
    path('sales/',include('sales.urls')),

    # 创建前往hello的路由
    path('hello/',include('hello.urls')),

    # 创建前往hello的动态路由(遇到符合   以u开头，后接8个数的url   都分发到 hello)
    re_path('^u\d{8}/',include('hello.urls'))
]
