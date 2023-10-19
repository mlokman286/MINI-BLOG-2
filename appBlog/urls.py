from django.urls import path
from appBlog import views


urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:id>',views.postinfo,name='post'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('addpost',views.addPost,name='addpost'),
    path('updatepost/<int:id>',views.updatePost,name='updatepost'),
    path('delete/<int:id>',views.deletePost,name='delete'),
    path('signup',views.signupPage,name='signup'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logout_page,name='logout'),
]
