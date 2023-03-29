from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_user, name='add-user'),
    path('all/', views.view_users, name='view_users'),
    path('update/<int:pk>/', views.update_user, name='update-user'),
    path('user/<int:pk>/delete/', views.delete_user, name='delete-user'),
]