from django.shortcuts import get_object_or_404, render

from .models import Post


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", context={
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", context={
        "all_posts": all_posts
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", context={
        "post": post,
        "post_tags": post.tags.all()
    })
