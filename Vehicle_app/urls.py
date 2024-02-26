from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('input/', views.inputform, name='inputform'),
    path('details/', views.details, name='details'),
]
