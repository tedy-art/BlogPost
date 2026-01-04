from django import forms
from unicodedata import category

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

    image = forms.ImageField(
        label="Upload an image",
        required=False,
        widget=forms.ClearableFileInput()
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        label="Select Category",
        widget=forms.Select()
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        label="Select Tags",
        widget=forms.SelectMultiple()
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image', 'category', 'tags']