from django.urls import path
from . import views


urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('user', views.AuthUserAPIView.as_view(), name='user'),
    path('update', views.UpdateUserAPIView.as_view(), name='user-update'),
    ]
