from django.urls import path, include
from api.views import *

urlpatterns = [
    path('', NotesListApiView.as_view(), name='notes_api_view'),
    path('<int:pk>/', NoteDetailApiView.as_view(), name='note_api_detail'),
]
