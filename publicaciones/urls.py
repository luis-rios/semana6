from rest_framework.routers import DefaultRouter

from publicaciones.views import PublicacionViewSets

router = DefaultRouter()
router.register(r'viewset', PublicacionViewSets)
urlpatterns = router.urls
