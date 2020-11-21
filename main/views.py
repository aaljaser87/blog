from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import PostForm
# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World STUDENTS, you Made it YAAAAY!!')

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'post_list.html', {'posts': posts })

 
def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = Author.objects.get(name='arwa')
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()

	return render(request, 'post_edit.html', {'form': form})
