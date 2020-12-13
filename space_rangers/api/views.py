from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .. import models
from . import serializers


class PilotViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.Pilot.objects.all()
    serializer_class = serializers.PilotSerializer


class SpaceshipViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.Spaceship.objects.all()
    serializer_class = serializers.SpaceshipSerializer
