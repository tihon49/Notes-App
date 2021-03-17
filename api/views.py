from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.permissions import IsNoteOwner
from django.contrib.auth.models import User

from app.models import Note, Product
from api.serializers import NotesListSerializer, NoteDetailSerializer


class NotesListApiView(generics.ListCreateAPIView):
    """отображение всех заметок (GET) и создание новой заметки (POST)"""

    queryset = Note.objects.all()
    serializer_class = NotesListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """получаем заметки конкретного юзера"""

        # авторизованый юзер
        user = User.objects.get(username=self.request.user)
        query = Note.objects.filter(owner=user)
        return  query


class NoteDetailApiView(generics.RetrieveAPIView):
    """детальное отображение заметки"""

    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer
    permission_classes = [IsAuthenticated, IsNoteOwner]
