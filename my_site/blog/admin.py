from django.contrib import admin

from .models import Author, Tag, Post


class PostAdmin(admin.ModelAdmin):
    """A class to control how posts should apear in admin pannel."""
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "tags")
    list_display = ("title", "author")


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
