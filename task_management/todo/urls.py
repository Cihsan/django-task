from django.contrib import admin
from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.home,name='todo'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_todo,name='delete_todo'),
    path('edit/<int:id>/', views.edit_todo,name='edit_todo'),
    path('done/<int:id>/', views.done_todo,name='done_todo')
]
