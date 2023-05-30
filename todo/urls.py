from django.urls import path
from . views import todo_list, todo_create, todo_delete, todo_update, todo_guest_complete
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
    path('guest/complete/<int:guest_id>/', views.todo_guest_complete, name='todo_guest_complete'),
]


""" urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
] """
