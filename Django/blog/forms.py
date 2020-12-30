from blog.models import Post 
from django import forms


class CreatePost(forms.ModelForm):

    class Meta:
        model = Post 
        fields = [
            "title",
            "post_image",
            "content"
        ]