from django.urls import path
from .views import todo_complete, todo_list, todo_create, todo_delete, todo_view, todo_update, update_completed_by, todo_guest_complete, todo_completed_update, todo_completed_delete

app_name = 'todo'

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name='todo_create'),
    path('update_completed_by/<int:todo_id>/', update_completed_by, name='update_completed_by'),
    path('complete/<int:pk>/', todo_complete, name='todo_complete'),
    path('view/<int:pk>/', todo_view, name='todo_view'),
    path('update/<int:pk>/', todo_update, name='todo_update'),
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),
    path('completed_update/<int:pk>/', todo_completed_update, name='todo_completed_update'),
    path('completed_delete/<int:pk>/', todo_completed_delete, name='todo_completed_delete'),
]

""" urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:pk>/', views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', views.todo_delete, name='todo_delete'),
] """
