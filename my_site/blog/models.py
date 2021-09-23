from django.db import models


class Author(models.Model):
    """A class to represent post authors."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)


class Tag(models.Model):
    """A class to represent tags of blog posts."""
    caption = models.CharField(max_length=255)


class Post(models.Model):
    """A class to represent blog posts."""
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(db_index=True)
    date = models.DateField()
    image = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
