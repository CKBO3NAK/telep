from django import forms
from .models import  Images, Article


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, widget = forms.Textarea ,label="Item Description.")

    class Meta:
        model = Article
        fields = ('title', 'body',)



