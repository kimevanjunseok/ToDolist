from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('detail/<int:board_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path(r'', views.index, name='index'),
]