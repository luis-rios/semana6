from rest_framework.routers import DefaultRouter
from tags.views import TagViewSet
router = DefaultRouter()
router.register(r'viewset', TagViewSet)
urlpatterns = router.urls
