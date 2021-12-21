from django import forms
from django.forms import widgets 

from .models import Comment


class CommentCreateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        "name": "comment", 
        "cols": "58",
        "rows": "7",
        "tabindex": "4",
        "class": "sm-form-control"
    }))
    
    class Meta:
        model = Comment
        fields = ['text']

