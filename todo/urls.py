from django.urls import path
from .views import todo_list, create_todo, todo_delete, todo_update, todo_guest_complete

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', create_todo, name='create_todo'),
    path('update/<int:pk>/', todo_update, name='todo_update'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
    path('guest_complete/<int:guest_id>/', todo_guest_complete, name='todo_guest_complete'),
]

""" urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
] """
