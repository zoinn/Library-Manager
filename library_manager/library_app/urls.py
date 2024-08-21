from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from .views import LibraryAppView, MemberAppView, LoginView, redirect_to_login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
#router.register(r'library', LibraryAppView)
#router.register(r'member', MemberAppView)

urlpatterns = [
    path('', redirect_to_login, name='root_redirect'),
    path('library/', LibraryAppView.as_view(), name='library'),
    path('member/', MemberAppView.as_view(), name='member'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
