from django.shortcuts import render, redirect
from blog.models import Post

def index(request):
    posts = Post.objects.all()
    latest_post = Post.objects.all()[0:4]
    context = {
        "posts": posts,
        "latest_post": latest_post
    }
    return render(request, "blog/index.html", context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

def post_like(request, pk):
    user = request.user
    likes = Post
    print(user)
    return redirect("blog:post-detail", pk=pk)


