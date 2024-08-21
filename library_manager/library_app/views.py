from django.shortcuts import redirect, render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Library, Member
from .serializers import LibrarySerializer, MemberSerializer
from rest_framework.decorators import action
from django.views.generic import ListView
from rest_framework.response import Response
from django.views.generic import TemplateView


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

class LoginView(TemplateView):
    template_name = 'login.html'
    def dispatch(self, request, *args, **kwargs):
        auth = JWTAuthentication()
        try:
            auth.authenticate(request)
        except AuthenticationFailed:
            return render(request, 'login.html', {"error": "You need to log in."})
        return super().dispatch(request, *args, **kwargs)

def redirect_to_login(request):
    return redirect('/login/')