from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','img']
        labels ={'title':'Title','description':'Description','img':'Upload an Image'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'w-full'}),
            'description':forms.Textarea(attrs={'class':'w-full'}),
            'img':forms.FileInput(attrs={'class':'file-input file-input-bordered file-input-success w-full'}),
        }