from django.urls import path

from . import views

urlpatterns = [
    path('result', views.index, name='index'),
    path('filelist', views.get_files, name='index'),
    path('getData', views.get_data, name='api'),
   
]