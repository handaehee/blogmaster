from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.newBoard, name='newBoard'),
    path('board/', views.board_view, name='boardview'),
    path('<int:pk>', views.board, name='boardone'),
]