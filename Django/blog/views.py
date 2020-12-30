from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.decorators import login_required
from blog.forms import CreatePost



@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        form.instance.author = request.user
        if form.is_valid():
            post = form.save()
            messages.success(request, "New post has been created by user{}".format(request.user))
            return redirect("blog:post-detail", post.pk)
    else:
        form = CreatePost(request.POST)
    return render(request, "blog/create_post.html", {"form": form})

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

@login_required
def post_like(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)
    users = post.likes.all()
    if user not in users:
        post.likes.add(user)
    else:
        pass
    return redirect("blog:post-detail", pk=pk)


