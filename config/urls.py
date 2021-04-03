import debug_toolbar
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('manage/', admin.site.urls),

    # Auth API endpoints
    path('api/auth/', include('rest_auth.urls')),

    # Debug toolbar endpoints
    path('__debug__/', include(debug_toolbar.urls)),

    # Default API endpoints
    path('api/space_rangers/', include('space_rangers.api.urls')),

    # Bulk API endpoints
    path('api/space_rangers_bulk/', include('space_rangers.bulk_api.urls')),

    # Bulk API endpoints
    path('', include('api_docs.urls')),
]
