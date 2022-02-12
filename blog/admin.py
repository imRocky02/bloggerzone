from django.contrib import admin
from blog.models import Tag, Post

# Register your models here.

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display =["id","title", "created_at", "modified_at"]
    list_filter = ('created_at', 'modified_at', 'title','tags',)


admin.site.register(Post, PostAdmin)

