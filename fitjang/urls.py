from django.urls import path
from fitjang import views

urlpatterns = [
    path('', views.home_page, name='home'),
]
