from django.urls import path

from fitjang import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('exercise/', views.exercise, name='exercise'),
]
