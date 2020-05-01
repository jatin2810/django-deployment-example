from django.urls import path
from register_app import views


app_name="register_app"

urlpatterns=[
    path("register/",views.register,name='register'),
    path("login/",views.user_login,name='user_login'),
]
