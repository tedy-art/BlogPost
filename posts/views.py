from django.shortcuts import render, redirect
from unicodedata import category

from .forms import BlogForm
from .models import BlogPost

# Create your views here.
def home(request):
    blogs = BlogPost.objects.all().order_by('-created_on')
    blogscount = blogs.count()

    context = {
        'blogs': blogs, 'blogscount': blogscount
    }
    return render(request, 'posts/home.html', context)

def blogposts(request):
    context = {}
    return render(request, 'posts/blogposts.html', context)

def create(request):
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            category = form.cleaned_data['category']

            blog = BlogPost(
                title = title,
                content = content,
                image = image,
                category = category
            )
            blog.save()

            return redirect('blogposts')

    context = {'form': form}
    return render(request, 'posts/create.html', context)


def edit(request, pk):
    blog = BlogPost.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method=='POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'posts/edit.html', context)

def delete(request, pk):
    blog = BlogPost.objects.get(id = pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('home')

    context = {
        'blog': blog
    }
    return render(request, 'posts/delete.html', context)
