from . import views
from django.urls import path
app_name='credentials'

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('form/',views.form,name='form'),
    path('logout/',views.logout,name='logout'),
    path('newpage/',views.newpage,name='newpage'),
    path('loginbutton/',views.loginbutton,name='loginbutton'),
    path('new/',views.new,name='new'),
]