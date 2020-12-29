from django.shortcuts import render, redirect
from blog.models import Post, PostLike


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
    num_of_like = 0
    current_user = request.user
    post = Post.objects.get(pk=pk)
    likes = PostLike.objects.all()

    for like in likes:
        if (like.user.username == current_user.username
            and like.post.title == post.title):
            # need to pass num_of_like to redirect. 
            return redirect("blog:post-detail", pk=pk)
        elif like.user.username != current_user.username:
            # add user and the post to database/class PostLike 
            added_likes = PostLike.objects.all()
            for added_like in added_likes:
                if added_like.post.title == post.title:
                    num_of_like += 1
    context = {
        "num_of_like": num_of_like,
        "post": post
    }
    return render(request, "blog/post_detail.html", context)

