from django.shortcuts import render, redirect
from board.forms import PostForm
from board.models import Post

# Create your views here.
def create(request):
    if request.method == "GET":
        postForm = PostForm()
        context = {'postForm': postForm}
        return render(request, "board/create.html", context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect('/board/read/' + str(post.id))


def list(request):
    posts = Post.objects.all().order_by('-id')
    context = {'posts': posts}
    return render(request, 'board/list.html', context)


def read(request, bid):
    post = Post.objects.get(id=bid)
    context = {'post': post}
    return render(request, 'board/read.html', context)


def delete(request, bid):
    post = Post.objects.get(id=bid)
    post.delete()
    return redirect('/board/list')
