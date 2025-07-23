# backend/tests/test_views.py
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.models import Project

@pytest.mark.django_db
def test_listar_projects_api():
    # cria 2 projetos publicados e 1 não-publicado
    Project.objects.create(title="A", slug="a", description="", is_published=True)
    Project.objects.create(title="B", slug="b", description="", is_published=True)
    Project.objects.create(title="C", slug="c", description="", is_published=False)

    client = APIClient()
    resp = client.get(reverse("project-list"))  # nome gerado pelo router
    assert resp.status_code == 200
    results = resp.json()["results"]
    # só aparecem os 2 publicados
    titles = {p["title"] for p in results}
    assert titles == {"A","B"}
