from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('query/', views.query, name='query'),
    path('resources/', views.resources, name='resources'),
    path('about/', views.about, name='about'),
    path('save-message/', views.save_message, name='save_message'),
]
