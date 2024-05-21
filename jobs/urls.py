from django.urls import path
from .views import *

urlpatterns = [
    path('jobs/', jobs, {'pk': None}, name='jobs'),
    path('jobs/<str:pk>', job, name='job'),
    path('createJob', createJob, name='createJob'),
    path('updateJob/<str:pk>', updateJob, name='updateJob'),
    path('deleteJob/<str:pk>', deleteJob, name='deleteJob'),
    path('createNote/<str:jobId>', createNote, {'noteId': None}, name='createNote'),
    path('createNote/<str:jobId>/<str:noteId>', createNote, name='updateNote'),
    path('deleteNote/<str:pk>', deleteNote, name='deleteNote'),
]