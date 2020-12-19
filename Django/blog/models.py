from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to="post_images")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.post_image.path)
        if img.width > 600 and img.height > 600:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.post_image.path)

    class Meta:
        ordering = ["-date_posted"]


# class PostLike(models.Model):
#     post_name = models.ForeignKey(Post, on_delete=models.CASCADE)
#     likes = models.ManyToManyField(User)

#     def __str__(self):
#         return self.likes.count()

