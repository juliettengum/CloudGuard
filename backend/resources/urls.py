

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CloudResourceViewSet

router = DefaultRouter()
router.register(
    "resources",
    CloudResourceViewSet,
    basename="cloud-resource",
)

urlpatterns = [
    path("", include(router.urls)),
]
