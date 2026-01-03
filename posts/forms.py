from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        label="Blog Post Title",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder':'Enter the title of your blog post...'
        })
    )

    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'placeholder':'Write your blogpost here...',
            'row':8
        })
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content']