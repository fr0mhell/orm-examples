from rest_framework_bulk.routes import BulkRouter

from . import views

router = BulkRouter()
router.register('pilots', views.PilotBulkViewSet, basename='pilots-bulk')
router.register('spaceships', views.SpaceshipBulkViewSet, basename='spaceships-bulk')

urlpatterns = router.urls
