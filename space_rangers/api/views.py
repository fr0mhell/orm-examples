from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, response, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from django_filters.rest_framework import DjangoFilterBackend

from .. import models, tasks
from . import filters, paginators, serializers
from celery.result import AsyncResult


class PilotViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """CRUD API for Pilots."""
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

    # Cache page for the requested url
    @method_decorator(cache_page(60*60*2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['POST'], url_path='dummy-progress')
    def dummy_progress(self, request, *args, **kwargs):
        if seconds := request.data.get('seconds'):
            result = tasks.dummy_progress.delay(seconds)

            return response.Response(
                status=status.HTTP_200_OK,
                data={'task': result.id},
            )

        return response.Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'], url_path='dummy-result')
    def dummy_result(self, request, *args, **kwargs):
        if task_id := request.data.get('task_id'):
            async_result = AsyncResult(task_id)

            return response.Response(
                status=status.HTTP_200_OK,
                data={
                    'status': async_result.state,
                    'info': async_result.info,
                },
            )

        return response.Response(status=status.HTTP_400_BAD_REQUEST)


class SpaceshipViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    """CRUD API for Spaceships."""
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
