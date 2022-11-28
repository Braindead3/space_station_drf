from rest_framework import routers

from .views import StationViewSet

router = routers.SimpleRouter()

router.register(r'stations', StationViewSet)

urlpatterns = router.urls
