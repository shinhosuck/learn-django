from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from blog.forms import CreatePost
from blog.models import Post, Topic



def landing_page(request):
    return render(request, "blog/landing_page.html", {})


@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        form.instance.author = request.user
        if form.is_valid():
            post = form.save()
            messages.success(request, "New post has been created by user {}".format(request.user))
            return redirect("blog:post-detail", post.pk)
    else:
        form = CreatePost(request.POST)
    return render(request, "blog/create_post.html", {"form": form})


def index(request):
    posts = []
    topics = Topic.objects.all()
    for topic in topics:
        posts += topic.post_set.all()[0:4]
    context = {
        "posts": posts,
        "topics": topics
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


def post_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, "blog/category.html", {"topic": topic})


def my_posts(request, pk):
    topics = Topic.objects.all()
    user = get_object_or_404(User, pk=pk)
    posts = user.post_set.all()
    context = {
        "posts": posts,
        "topics": topics
    }
    return render(request, "blog/my_posts.html", context)