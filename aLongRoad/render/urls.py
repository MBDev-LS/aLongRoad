from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('v2/', views.index2_view, name='index2'),
    path('v2/road/', views.road_batch_view, name='road_batch'),
]
