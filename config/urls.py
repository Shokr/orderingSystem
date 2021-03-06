"""
* orderingSystem URL Configuration
"""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ordering System API",
        default_version='v1.0',
        description="Paymob ordering System API Docs.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="muhammed@shokr.works"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# OpenApi URLS
urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
]
