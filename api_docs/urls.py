from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import schema_view
from django.urls import re_path


urlpatterns = [
   re_path(
       r'^swagger/$',
       schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui',
   ),
   re_path(
       r'^redoc/$',
       schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc',
   ),
]
