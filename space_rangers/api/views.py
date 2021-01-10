from rest_framework import mixins, response, status
from rest_framework.viewsets import GenericViewSet
from .. import models
from . import serializers, paginators, filters
from .generic.views import BaseViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action


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
    permission_classes = (
        IsAuthenticated,
    )
    filter_class = filters.PilotFilter


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
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    ordering_fields = (
        'name',
        'ship_class',
        'speed',
        'pilot__name',
    )
    filter_fields = (
        'ship_class',
        'speed',
        'pilot__name',
    )
    search_fields = (
        'name',
        'pilot__name',
    )
    permission_classes = (
        AllowAny,
    )

    @action(detail=True, methods=['POST'], url_name='heal-it')
    def heal(self, request, pk):
        """Heal selected ship"""
        ship = self.get_object()
        ship.heal()
        serializer = self.get_serializer(ship)
        return response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )


class FractionViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """Read-only API for Fractions."""
    queryset = models.Fraction.objects.all()
    serializer_class = serializers.FractionSerializer
