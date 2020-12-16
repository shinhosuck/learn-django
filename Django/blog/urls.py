from django.urls import path
from blog.views import index

app_name = "blog"

urlpatterns = [
    path("home/", index, name="home"),

]
