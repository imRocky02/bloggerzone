from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.expressions import Value
from django.db.models.fields import SlugField
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
User = settings.AUTH_USER_MODEL

class Tag(models.Model):
    Value = models.CharField(max_length=100)

    def __str__(self):
        return self.Value

class Post(models.Model):
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
        ('ARCHIVED','Archived')
    )




    title = models.CharField(max_length=125)
    content = RichTextField(blank=True)
    Summary = models.TextField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=125)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name="posts")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='DRAFT')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk, "slug":self.slug})

    
    class Meta:
        ordering = ["-created_at"]


        

    