import django_filters

from ..models import Pilot


class PilotFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Pilot
        fields = {
            'name': ['icontains', ],
        }
