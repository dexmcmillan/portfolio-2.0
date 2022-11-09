from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # re_path(r'^projects/.*', FilteredViewSet.as_view({'get': 'list'})),
]
