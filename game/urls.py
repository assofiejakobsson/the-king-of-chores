from django.urls import path
from .views import complete_task, game_view, game_create
from game import views


app_name = 'game'

urlpatterns = [
    path('game/', game_view, name='game'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('create/', game_create, name='game_create'),
]
