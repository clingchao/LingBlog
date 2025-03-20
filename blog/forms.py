from django import forms

from .models import Comment

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')


from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())  # 关键：接收状态值

    class Meta:
        model = Post
        fields = ['title', 'slug', 'intro', 'body', 'category', 'status']  # 包含所有字段