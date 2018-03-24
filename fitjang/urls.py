from django.urls import path

from fitjang import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('delete', views.delete_row_table, name='delete_row_table'),
    path('exercise/', views.exercise, name='exercise'),
    path('exercise/chest', views.chest, name='chest'),
    path('exercise/arms', views.arms, name='arms'),
    path('exercise/shoulder', views.shoulder, name='shoulder'),
    path('exercise/legs', views.legs, name='legs'),
    path('exercise/back', views.back, name='back'),

]
