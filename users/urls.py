from django.urls import path
from users.views import UserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('users/login', TokenObtainPairView.as_view()),
    
    path('users', UserView.as_view()),
    path('users/<str:pk>', UserDetailView.as_view()),
]