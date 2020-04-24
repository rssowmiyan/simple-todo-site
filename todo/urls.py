
from django.contrib import admin
from django.urls import path,include
from getitdone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('getitdone.urls')),
    path('',views.home,name='home'),
    path('create',views.createtodo,name='createtodo'),
    path('todo/<int:todo_pk>',views.viewtodo,name='viewtodo'),
    # pk=primary key,to see a particular blog post <int:todo_pk>
    # the above views unlike other views accepts two parameters
    path('todo/<int:todo_pk>/complete',views.completetodo,name='completetodo'),
    path('todo/<int:todo_pk>/delete',views.deletetodo,name='deletetodo'),

]

