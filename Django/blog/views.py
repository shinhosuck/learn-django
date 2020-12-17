from django.shortcuts import render
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    latest_post = Post.objects.all()[0:3]
    context = {
        "posts": posts,
        "latest_post": latest_post
    }
    return render(request, "blog/index.html", context)


