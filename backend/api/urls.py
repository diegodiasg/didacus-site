from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StaticPageViewSet, ProjectViewSet,
    CategoryViewSet, TagViewSet,
    PostViewSet, ContactMessageViewSet
)

router = DefaultRouter()
router.register(r"staticpages", StaticPageViewSet)
router.register(r"projects",    ProjectViewSet)
router.register(r"categories",  CategoryViewSet)
router.register(r"tags",        TagViewSet)
router.register(r"posts",       PostViewSet)
router.register(r"contacts",    ContactMessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
