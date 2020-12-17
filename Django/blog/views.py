from django.shortcuts import render
from blog.models import Post


def index(request):
    posts = Post.objects.all()[0:2]
    latest_post = Post.objects.filter().first()
    context = {
        "posts": posts,
        "latest_post": latest_post
    }
    return render(request, "blog/index.html", context)


