# backend/tests/test_serializers.py
import pytest
from core.models import Project
from api.serializers import ProjectSerializer

@pytest.mark.django_db
def test_serializer_retorna_campos_corretos():
    p = Project.objects.create(
        title="X", slug="x", description="Y", is_published=True
    )
    data = ProjectSerializer(p).data
    # deve conter id, title, slug, description, image (None), url (""), is_published
    assert set(data.keys()) >= {"id","title","slug","description","is_published"}
    assert data["title"] == "X"
