from rest_framework.routers import DefaultRouter
from .views import Daily_costViewSet

router = DefaultRouter()

router.register('daily_costs', Daily_costViewSet)

urlpatterns = router.urls