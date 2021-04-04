from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from rest_framework_bulk import mixins as bulk_mixins

from .. import models
from ..api import serializers


class PilotBulkViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    bulk_mixins.BulkCreateModelMixin,
    bulk_mixins.BulkUpdateModelMixin,
    bulk_mixins.BulkDestroyModelMixin,
    GenericViewSet,
):
    queryset = models.Pilot.objects.all()
    serializer_class = serializers.PilotSerializer


class SpaceshipBulkViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    bulk_mixins.BulkCreateModelMixin,
    bulk_mixins.BulkUpdateModelMixin,
    bulk_mixins.BulkDestroyModelMixin,
    GenericViewSet,
):
    queryset = models.Spaceship.objects.all()
    serializer_class = serializers.SpaceshipSerializer
