from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Library, Member
from .serializers import LibrarySerializer, MemberSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class LibraryAppView(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class MemberAppView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    @action(detail=True, methods=['get'])
    def getbooks(self, request, pk=None):
        member = self.get_object()
        books = Library.objects.filter(book_holder=member)
        serializer = LibrarySerializer(books, many=True)
        return Response(serializer.data)
