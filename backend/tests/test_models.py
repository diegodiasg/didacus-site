# backend/tests/test_models.py
import pytest
from core.models import Project

@pytest.mark.django_db
def test_criar_e_str_de_project():
    proj = Project.objects.create(
        title="Teste",
        slug="teste",
        description="Descrição",
        is_published=True
    )
    assert str(proj) == "Teste"
    assert proj.is_published
