from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='developer.index'),
    path('files', views.database_files, name='developer.files'),]