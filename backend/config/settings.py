import environ
from pathlib import Path

# ==== leitura do .env ==== 
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(env_file=Path(__file__).resolve().parent.parent / ".env")

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações básicas
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Aplicações instaladas
INSTALLED_APPS = [
    # pacotes de terceiros
    "corsheaders",
    "rest_framework",

    # apps padrão do Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    'drf_spectacular',

    # apps do projeto
    "core",
    "api",
]

# Middlewares
MIDDLEWARE = [
    # CORS deve vir antes de CommonMiddleware
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
  'default': env.db_url('DATABASE_URL', default='postgres://django:changeme@db:5432/didacus')
}


# Validação de senhas
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internacionalização\ nLANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Configurações adicionais
# Permite requisições de qualquer origem (apenas em dev)
CORS_ALLOW_ALL_ORIGINS = True

# Configuração do Django REST Framework (exemplo básico)
# no topo, depois de definir DEBUG e importações…

if DEBUG:
    DEFAULT_RENDERER_CLASSES = [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ]
else:
    DEFAULT_RENDERER_CLASSES = [
        "rest_framework.renderers.JSONRenderer",
    ]

REST_FRAMEWORK = {
    # Autenticação JWT
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # Permissões: GET livre, POST/PUT/DELETE requer token
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),

    # Renderers: inclui HTML apenas em DEBUG
    "DEFAULT_RENDERER_CLASSES": DEFAULT_RENDERER_CLASSES,

    # Schema automático (Spectacular)
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

    # Filtros, busca e ordenação
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],

    # Paginação por página
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}



SPECTACULAR_SETTINGS = {
    'TITLE': 'API Didacus Site',
    'DESCRIPTION': 'Documentação automática da API do site Didacus.',
    'VERSION': '1.0.0',
    # se quiser separar tags por app:
    'SCHEMA_PATH_PREFIX': r'/api/',
    # opções extras…
}


# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'