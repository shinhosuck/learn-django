from django.urls import path
from blog.views import (
                        index,
                        post_detail,
                    )

app_name = "blog"

urlpatterns = [
    path("home/", index, name="home"),
    path("post/<int:pk>/detail/", post_detail, name="post-detail")
    # path("<int:user_pk>/<int:post_pk>/", likes, name="post-like")
]
