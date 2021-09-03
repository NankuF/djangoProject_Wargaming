from django.urls import path
from .views import upload_file, file_read

app_name = 'table'

urlpatterns = [
    path('', upload_file, name='index'),
    path('file_info/', file_read, name='file_read')
]
