from django.contrib import admin
from .models import StaticPage, Project, Category, Tag, Post, ContactMessage


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    """Admin para páginas estáticas."""
    # Campos exibidos na lista de páginas estáticas
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    # Gera automaticamente o slug a partir do título
    prepopulated_fields = {'slug': ('title',)}
    # Campos apenas leitura (campos timestamp)
    readonly_fields = ('created_at', 'updated_at')
    # Pesquisa por título e conteúdo
    search_fields = ('title', 'content')
    # Filtros laterais por data de criação e atualização
    list_filter = ('created_at', 'updated_at')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin para projetos."""
    list_display = ('title', 'slug', 'is_published', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'description', 'url')
    list_filter = ('is_published', 'created_at', 'updated_at')
    # Ações personalizadas para publicar/despublicar projetos
    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        """Marca os projetos selecionados como publicados."""
        count = queryset.update(is_published=True)
        self.message_user(request, f"{count} projeto(s) marcados como publicados.")
    make_published.short_description = "Marcar como publicados"

    def make_unpublished(self, request, queryset):
        """Marca os projetos selecionados como não publicados."""
        count = queryset.update(is_published=False)
        self.message_user(request, f"{count} projeto(s) marcados como não publicados.")
    make_unpublished.short_description = "Marcar como não publicados"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin para categorias."""
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin para tags."""
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin para posts de blog."""
    list_display = ('title', 'slug', 'is_published', 'published_at', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'published_at', 'categories', 'tags', 'created_at')
    # Permite selecionar categorias e tags de forma intuitiva
    filter_horizontal = ('categories', 'tags')
    actions = ['make_published', 'make_unpublished']

    def make_published(self, request, queryset):
        """Marca os posts selecionados como publicados."""
        count = queryset.update(is_published=True)
        self.message_user(request, f"{count} post(s) marcados como publicados.")
    make_published.short_description = "Marcar como publicados"

    def make_unpublished(self, request, queryset):
        """Marca os posts selecionados como não publicados."""
        count = queryset.update(is_published=False)
        self.message_user(request, f"{count} post(s) marcados como não publicados.")
    make_unpublished.short_description = "Marcar como não publicados"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin para mensagens de contato."""
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    # Campos que não devem ser editados diretamente
    readonly_fields = ('created_at', 'updated_at', 'name', 'email', 'subject', 'message')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    actions = ['mark_as_read', 'mark_as_unread']

    def mark_as_read(self, request, queryset):
        """Marca as mensagens selecionadas como lidas."""
        count = queryset.update(is_read=True)
        self.message_user(request, f"{count} mensagem(ns) marcadas como lidas.")
    mark_as_read.short_description = "Marcar como lidas"

    def mark_as_unread(self, request, queryset):
        """Marca as mensagens selecionadas como não lidas."""
        count = queryset.update(is_read=False)
        self.message_user(request, f"{count} mensagem(ns) marcadas como não lidas.")
    mark_as_unread.short_description = "Marcar como não lidas"