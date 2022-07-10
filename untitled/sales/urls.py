from django.urls import path,re_path
from sales import views

# sales的路由子表
urlpatterns = [
    path('orders/',views.list_orders),     # http//:localhost/sales/orders

    path('customers/',views.list_customers),

    path('select_customers_byPhoneNumber/',views.select_list_customers_byPhoneNumber),

    path('test/',views.db_test),

    re_path(r'^customers/(?P<id>\d{8})',views.get_info_from_url),

    path('search/',views.obtain_from_GET),

    path('hackbar/', views.obtain_from_POST),

    path('json/',views.obtain_from_json),

    path('',views.show_template_index),

    path('excellent/',views.show_excellent_staff),

    path('curd/',views.Curd.as_view()),
    
]