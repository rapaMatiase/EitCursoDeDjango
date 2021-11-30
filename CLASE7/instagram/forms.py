from django.forms import ModelForm
from .models import Comment, Profile

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'