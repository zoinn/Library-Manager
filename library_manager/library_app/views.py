from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Library, Member
from .serializers import LibrarySerializer, MemberSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.generic import ListView
from rest_framework import status

# Create your views here.

class LibraryAppView(ListView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    template_name = 'library.html'
    context_object_name = 'books'

class MemberAppView(ListView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    template_name = 'members.html'
    context_object_name = 'members'

    @action(detail=True, methods=['get'])
    def getbooks(self, request, pk=None):
        member = self.get_object()
        books = Library.objects.filter(book_holder=member)
        serializer = LibrarySerializer(books, many=True)
        return Response(serializer.data)
