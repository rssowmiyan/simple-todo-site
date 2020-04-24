from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    # comes under accounts/
    # bcoz i wanted it do nothing rational here
    path('register/',views.register,name='register'),
    path('currenttodos/',views.currenttodos,name='currenttodos'),
    path('completedtodos/',views.completedtodos,name='completedtodos'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('login/',views.loginuser,name='loginuser'),
]