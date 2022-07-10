from django.urls import path
from hello import views # 导入hello 的所有视图函数

# 添加子路由条目
urlpatterns = [
    path("sayhello/",views.sayhello),
    path("UID",views.var_uid),

    path("class_deco/",views.Things.as_view()),

    path("give_cookie/",views.give_cookie),

    path("read_cookie/",views.read_cookie),

    path("remove_cookie/",views.remove_cookie),

    path("remove_session/",views.remove_session),

    path("read_session/",views.read_session),

    path("add_session_data/",views.add_session_data),
]