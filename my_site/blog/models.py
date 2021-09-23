from django.db import models
from django.urls import reverse


class Author(models.Model):
    """A class to represent post authors."""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def get_full_name(self):
        """Return the full name of the author."""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """Return the string representation of the model."""
        return self.get_full_name()


class Tag(models.Model):
    """A class to represent tags of blog posts."""
    caption = models.CharField(max_length=255)

    def __str__(self):
        """Return the string representation of the model."""
        return self.caption


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

    def get_absolute_url(self):
        """Return the absolute url of a blog post."""
        return reverse("post-detail-page", args=[self.slug])

    def __str__(self):
        """Return the string representation of the model."""
        return self.title
