from django import forms
from .models import Comment, Post
from django.utils.translation import gettext as _


class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels ={
            'name':_('name'),
            'email':_('email'),
            'body':_('body'),
        }


class PostCreateForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField( widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ['title', 'content']

        labels ={
            'Title':_('Title'),
            'Content':_('Content')
        }
