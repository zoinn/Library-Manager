from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibraryAppView, MemberAppView

router = DefaultRouter()
#router.register(r'library', LibraryAppView)
#router.register(r'member', MemberAppView)

urlpatterns = [
    path('', include(router.urls)),
    path('library/', LibraryAppView.as_view(), name='library_list'),
    path('member/', MemberAppView.as_view(), name='members_list'),
]
