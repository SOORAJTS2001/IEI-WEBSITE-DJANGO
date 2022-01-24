from .views import admin_page, home, register,admin_login,test,error_400,error_403,error_404,error_500
from django.urls import path,include
handler404 = 'WEBSITE.views.error_404'
handler500 = 'WEBSITE.views.error_500'
handler403 = 'WEBSITE.views.error_403'
handler400 = 'WEBSITE.views.error_400'
urlpatterns = [
    path('',home,name="index"),
    path('register/',register,name="register"),
    path('admin-login/',admin_login,name="admin-login"),
    path('admin-page/',admin_page,name="admin-page"),
    path('test/',test,name='test')
]
