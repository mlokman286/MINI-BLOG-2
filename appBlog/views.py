from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import LoginForm, PostForm, SingupForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# ------HOME Page------
def home(request):
    posts = Post.objects.all()
    return render(request,"home.html",{'posts':posts})

def postinfo(request,id):
    post = Post.objects.get(id = id)
    return render(request,'postdetails.html',{'post':post})
# ------Contact Page------ 
def contact(request):
    return render(request,"contact.html")

# ------Dashboard Page------
def dashboard(request):
    posts = Post.objects.all()
    return render(request,"dashboard.html",{'posts':posts})

# -------Add Post in Dashboard-------
def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully add a post')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid title or descriptions or image file.')
            return redirect('addpost')
    else:
        form = PostForm()
        return render(request,"addpost.html",{'form':form})
# -------Update Dashboard-------
def updatePost(request,id):
    if request.method == 'POST':
        pk = Post.objects.get(id=id)
        form = PostForm(request.POST,instance=pk)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully update the post')
        return redirect('dashboard')
    else:
        pk = Post.objects.get(id=id)
        form = PostForm(instance=pk)
        return render(request,'updatepost.html',{'form':form})

def deletePost(request,id):
    pk = Post.objects.get(id=id)
    pk.delete()
    return redirect('dashboard')
# ------About Page------
def about(request):
    return render(request,"about.html")

# ------Sign Up Page------
def signupPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form=SingupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Congrates🎉🎉You have succesfully become a Author')
                return redirect('login')
            else:
                messages.error(request,'There is a invalid fields')
                return redirect('signup')
        else:
            form = SingupForm()
            return render(request,"signup.html",{'form':form})
    else:
        return redirect('home')

# ------Log In Page------
def loginPage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user:
                    login(request,user)
                    name =user.first_name +' '+ user.last_name
                    print(name)
                    messages.success(request,"Welcome MR {}".format(name))
                    return redirect('home')
            else:
                messages.error(request,'Invalid username or password')
                return redirect('login')
        form = LoginForm()
        return render(request,"login.html",{'form':form})
    else:
        return redirect('home')

# ------Log out Function------
def logout_page(request):
    logout(request)
    return redirect('login')