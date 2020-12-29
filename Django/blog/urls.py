from django.urls import path
from blog.views import (
                        index,
                        post_detail,
                        post_like,
                    )

app_name = "blog"

urlpatterns = [
    path("home/", index, name="home"),
    path("post/<int:pk>/detail/", post_detail, name="post-detail"),
    path("post/<int:pk>/like/", post_like, name="post-like")
]
