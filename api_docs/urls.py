from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import schema_view

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
