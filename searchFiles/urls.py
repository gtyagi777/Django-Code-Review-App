from django.urls import path

from searchFiles import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files/',views.fileList , name = 'fileList'),
    path('files/displayFile/<int:file_id>',views.displayFile , name = 'displayFile'),
]