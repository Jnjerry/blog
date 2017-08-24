from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
        class Meta:
         model = Post
         fields = ('title', 'content','image')
       # title=forms.CharField(max_length=200)
       # content=forms.CharField(required=True)
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
