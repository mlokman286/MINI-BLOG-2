from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']
        labels ={'title':'Title','description':'Description'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'w-full'}),
            'description':forms.Textarea(attrs={'class':'w-full'}),
        }