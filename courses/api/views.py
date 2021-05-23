from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer
from django.shortcuts import get_object_or_404

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer