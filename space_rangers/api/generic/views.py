from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class BaseViewSet(GenericViewSet):
    base_filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    extra_filter_backends = None

    def get_filter_backends(self):
        """Allow to customize filter backends.

        Allow to join `base_filter_backends` and `extra_filter_backends`
        and can be overridden in order.

        """
        base_backends = self.base_filter_backends or tuple()
        extra_backends = self.extra_filter_backends or tuple()
        return tuple(base_backends + extra_backends)

    @property
    def filter_backends(self):
        """Allow to dynamically return filter backends."""
        return self.get_filter_backends()
