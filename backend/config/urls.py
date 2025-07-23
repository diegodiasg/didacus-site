# backend/config/urls.py

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,      # já importado
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    # estáticos e mídia
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)

    # documentação OpenAPI/Swagger
    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
          "api/docs/",
          SpectacularSwaggerView.as_view(url_name="schema"),
          name="swagger-ui"
        ),
        # se quiser ReDoc também:
        path(
          "api/redoc/",
          SpectacularRedocView.as_view(url_name="schema"),
          name="redoc-ui"
        ),
    ]
