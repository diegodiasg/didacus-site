# backend/api/viewsets.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from rest_framework.filters import SearchFilter, OrderingFilter

from core.models import (
    StaticPage, Project,
    Category, Tag, Post,
    ContactMessage
)
from .serializers import (
    StaticPageSerializer, ProjectSerializer,
    CategorySerializer, TagSerializer,
    PostSerializer, ContactMessageSerializer
)

# --------------------------------------------------
# 1) StaticPage: só leitura, lookup por slug
# --------------------------------------------------
class StaticPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer
    lookup_field = "slug"

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["slug", "title"]
    search_fields    = ["title", "content"]
    ordering_fields  = ["created_at", "updated_at", "title"]
    ordering         = ["title"]


# --------------------------------------------------
# 2) Project: CRUD completo, apenas is_published=True
# --------------------------------------------------
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_published=True)
    serializer_class = ProjectSerializer
    lookup_field = "slug"

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["slug", "is_published"]
    search_fields    = ["title", "description"]
    ordering_fields  = ["created_at", "updated_at", "title"]
    ordering         = ["-created_at"]


# --------------------------------------------------
# 3) Category: só leitura, lookup por slug
# --------------------------------------------------
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["slug", "name"]
    search_fields    = ["name"]
    ordering_fields  = ["name"]
    ordering         = ["name"]


# --------------------------------------------------
# 4) Tag: só leitura, lookup por slug
# --------------------------------------------------
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "slug"

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["slug", "name"]
    search_fields    = ["name"]
    ordering_fields  = ["name"]
    ordering         = ["name"]


# --------------------------------------------------
# 5) Post: CRUD completo, apenas is_published=True
#    usando FilterSet para categoria e tag
# --------------------------------------------------
class PostFilter(FilterSet):
    category = CharFilter(field_name="categories__slug", lookup_expr="exact")
    tag      = CharFilter(field_name="tags__slug",       lookup_expr="exact")

    class Meta:
        model  = Post
        fields = ["slug", "is_published", "category", "tag"]


class PostViewSet(viewsets.ModelViewSet):
    queryset         = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    lookup_field     = "slug"

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields    = ["title", "excerpt", "content"]
    ordering_fields  = ["created_at", "updated_at", "title"]
    ordering         = ["-created_at"]


# --------------------------------------------------
# 6) ContactMessage: CRUD completo (normalmente só POST)
# --------------------------------------------------
class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset         = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["email", "created_at"]
    search_fields    = ["name", "email", "message"]
    ordering_fields  = ["created_at"]
    ordering         = ["-created_at"]
