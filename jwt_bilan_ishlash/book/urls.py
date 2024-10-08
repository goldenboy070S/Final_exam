from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('category', CategoryViewSet),
router.register('product', ProductViewSet)
router.register('comment', CommentViewSet)
router.register('order', OrderViewSet)

urlpatterns = router.urls