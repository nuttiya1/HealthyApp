from django.urls import path

from fitjang import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('show/', views.show, name='show'),
]
