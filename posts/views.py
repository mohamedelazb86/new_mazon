from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts= Post.objects.all()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/posts/')
    else:
        form=PostForm()
    context={
        'posts':posts,
        'form':form
    }
    return render (request,'posts/post_list.html',context)
def post_detail(request,slug):
    post=Post.objects.get(slug=slug)

    context={
        'post':post
    }
    return render(request,'posts/post_detail.html',context)

def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/posts/')
    else:
        form=PostForm()

    return render(request,'posts/create_post.html',{'form':form})

def update_post(request,slug):
    post=Post.objects.get(slug=slug)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user

            myform.save()
            return redirect('/posts/')
    else:
        form=PostForm(instance=post)
    return render(request,'posts/update_post.html',{'form':form})

def delete_post(request,slug):
    post=Post.objects.get(slug=slug)
    post.delete()
    return redirect('/posts/')