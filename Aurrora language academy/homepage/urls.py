from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listening/', views.listening, name='listening'),
    path('reading/', views.reading, name='reading'),
    path('writing/', views.writing, name='writing'),
    path('speaking/', views.speaking, name='speaking'),
    path('mock/', views.mock, name='mock'),
    path('login/', views.login, name='login'),
]