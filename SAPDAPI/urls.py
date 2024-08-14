from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="sapd API",
        default_version='v1',
        description="Sistema de apoio a pessoas desaparecidas API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bennedito01@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/posts/', include("posts.urls")),
    path('api/facial/', include('facial_recognition.urls')),
    path('api/emergency/', include('emergency_contact.urls')),


    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
