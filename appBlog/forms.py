from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User


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
class SingupForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'w-full input','placeholder':'Type a password'}))
    password2 = forms.CharField(label='Confrom Password (again)',widget=forms.PasswordInput(attrs={'class':'w-full input','placeholder':'Retype the same password'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets ={
            'username':forms.TextInput(attrs={'class':'w-full input','placeholder':'Type unique username'}),
            'first_name':forms.TextInput(attrs={'class':'w-full input','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'w-full input','placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'w-full input','placeholder':'Valid Email'}),            
        }
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus":True,'class':'w-full input','placeholder':'Type correct username'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'w-full input','placeholder':'Type correct password'}))
    