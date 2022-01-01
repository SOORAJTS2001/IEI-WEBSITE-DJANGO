from .views import admin_page, home, register,admin_login,test
from django.urls import path,include
urlpatterns = [
    path('',home,name="index"),
    path('register/',register,name="register"),
    path('admin-login/',admin_login,name="admin-login"),
    path('admin-page/',admin_page,name="admin-page"),
    path('test/',test,name='test'),
]
