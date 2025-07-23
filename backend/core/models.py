from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SEOMixin(models.Model):
    seo_title = models.CharField("Título SEO", max_length=70, blank=True)
    seo_description = models.CharField("Descrição SEO", max_length=160, blank=True)

    class Meta:
        abstract = True

class StaticPage(TimeStampedModel, SEOMixin):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField("Conteúdo em HTML/Markdown")

    def __str__(self):
        return self.title

class Project(TimeStampedModel, SEOMixin):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True)
    description = models.TextField()
    image       = models.ImageField(upload_to="projects/")
    url         = models.URLField(blank=True)  # link para demo ou repo
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(TimeStampedModel, SEOMixin):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(unique=True)
    content     = models.TextField()
    published_at = models.DateTimeField(null=True, blank=True)
    categories  = models.ManyToManyField(Category, related_name="posts")
    tags        = models.ManyToManyField(Tag, related_name="posts")
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ContactMessage(TimeStampedModel):
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} – {self.subject}"
