from django.forms import ModelForm
from appLeoClimb.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'