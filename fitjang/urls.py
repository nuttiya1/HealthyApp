from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('adddata/', views.add_data, name='add_data'),
    path('adddata/show/', views.show, name='show'),
]
