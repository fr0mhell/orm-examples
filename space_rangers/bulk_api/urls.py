from rest_framework_bulk.routes import BulkRouter
from . import views

router = BulkRouter()
router.register('pilots', views.PilotBulkViewSet)
router.register('spaceships', views.SpaceshipBulkViewSet)

urlpatterns = router.urls
