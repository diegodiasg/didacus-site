from rest_framework import serializers
from core.models import (
    StaticPage, Project,
    Category, Tag, Post,
    ContactMessage
)

class StaticPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticPage
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "title", "slug",
            "description", "image",
            "url", "is_published",
            "created_at", "updated_at",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]


class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    tags       = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id", "title", "slug",
            "content", "published_at",
            "is_published", "categories",
            "tags", "created_at", "updated_at",
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            "id", "name", "email",
            "subject", "message",
            "is_read", "created_at",
            "updated_at",
        ]