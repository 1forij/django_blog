from django.urls import path
from user_auth import views

urlpatterns = [
    path('login/',views.to_login,name='login'),
    #     path('login/',views.To_login.as_xxxx,name='login'),
    path('logout/',views.to_logout),
    path('register/',views.to_register)
]