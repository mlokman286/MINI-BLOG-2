from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import PostForm
from .models import Post

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
    return render(request,"signup.html")

# ------Log In Page------
def loginPage(request):
    return render(request,"login.html")

# ------Log out Function------
def logout(request):
        pass