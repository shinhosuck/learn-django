from django.urls import path
from blog.views import (
                        index,
                        post_detail,
                        post_like,
                        create_post,
                    )

app_name = "blog"

urlpatterns = [
    path("home/", index, name="home"),
    path("new/post/", create_post, name="create-post"),
    path("post/<int:pk>/detail/", post_detail, name="post-detail"),
    path("post/<int:pk>/like/", post_like, name="post-like")
]
