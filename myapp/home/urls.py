from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('delete/<int:board_pk>/', views.delete, name='delete'),
    path('update/<int:board_pk>/', views.update, name='update'),
    path('detail/<int:board_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path(r'', views.index, name='index'),
]