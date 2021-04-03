from django.urls import re_path

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
