from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .. import models
from . import serializers, paginators


class PilotViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.Pilot.objects.all().select_related(
        'race',
    ).prefetch_related(
        'spaceships',
        'fractions',
    )
    serializer_class = serializers.PilotSerializer
    pagination_class = paginators.SmallPagePagination


class SpaceshipViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.Spaceship.objects.all().select_related(
        'pilot',
        'pilot__race',
    )
    serializer_class = serializers.SpaceshipSerializer
