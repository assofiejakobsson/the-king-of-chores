from django.urls import path
from .views import (
    home,
    todo_complete,
    todo_list,
    todo_create,
    todo_delete,
    todo_view,
    todo_update,
    update_completed_by,
    todo_completed_update,
    todo_completed_delete
)


app_name = 'todo'


urlpatterns = [
    # Home page
    path('', home, name='home'),

    # Todo list
    path('list/', todo_list, name='todo_list'),

    # Todo creation
    path('create/', todo_create, name='todo_create'),

    # Update the "completed_by" field of a todo
    path('update_completed_by/<int:todo_id>/', update_completed_by, name='update_completed_by'),

    # Mark a todo as complete
    path('complete/<int:pk>/', todo_complete, name='todo_complete'),

    # View details of a todo
    path('view/<int:pk>/', todo_view, name='todo_view'),

    # Update a todo
    path('update/<int:pk>/', todo_update, name='todo_update'),

    # Delete a todo
    path('delete/<int:pk>/', todo_delete, name='todo_delete'),

    # Update a completed todo
    path('completed_update/<int:pk>/', todo_completed_update, name='todo_completed_update'),

    # Delete a completed todo
    path('completed_delete/<int:pk>/', todo_completed_delete, name='todo_completed_delete'),
]
