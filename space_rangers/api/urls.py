from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('pilots', views.PilotViewSet)
router.register('spaceships', views.SpaceshipViewSet)
router.register('fractions', views.FractionViewSet)

urlpatterns = router.urls
