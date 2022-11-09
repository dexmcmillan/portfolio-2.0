from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, JobViewSet, TagViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
