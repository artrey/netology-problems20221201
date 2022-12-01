from django.db.models import Q
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from notes.models import Note
from notes.serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.select_related('user')
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_anonymous:
            qs = qs.filter(is_private=False)
        else:
            qs = qs.filter(Q(is_private=False) | Q(user=self.request.user))
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
