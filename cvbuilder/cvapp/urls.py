from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cv/create/', views.create_cv, name='create_cv'),
    path('cv/<int:pk>/edit/', views.edit_cv, name='edit_cv'),
    path('cv/<int:pk>/delete/', views.delete_cv, name='delete_cv'),
    path('cv/<int:pk>/preview/', views.preview_cv, name='preview_cv'),
]

