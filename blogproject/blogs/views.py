from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from django.utils import timezone
from django.contrib import messages


class HomeView(LoginRequiredMixin, ListView):
    model = blog
    template_name = 'blogs/index.html'
    context_object_name = 'blog_entries'
    ordering = ['-date']
    paginate_by = 3


def BlogView(request, id):
    Username = request.user
    blogdetail = get_object_or_404(blog, id=id)
    return render(request, 'blogs/blog_detail.html', {'object':blogdetail, 'Username':Username})


@login_required
def CreateBlog(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            form.instance.author = request.user
            name = request.user
            model_instance.save()
            return redirect('/')

    else:
        form = UploadForm()
    return render(request, 'blogs/create_blog.html', {'form': form})


def EditBlog(request,id):
    template = 'blogs/create_blog.html'
    Blog = get_object_or_404(blog, pk=id)

    if request.method == 'POST':
        form = UploadForm(request.POST, instance=Blog)

        try:
            if form.is_valid():
                form.save()
                return redirect('/')

        except Exception as e:
            messages.warning(request, 'Your post was not saved due to an error: { }'.format(e))

    else:
        form = UploadForm(instance=Blog)

    context={
        'form' : form,
        'Blog' : Blog
    }
    return render(request, template, context)


def DeleteBlog(request, id):
    template = 'blogs/create_blog.html'
    Blog = get_object_or_404(blog, pk=id)

    try:
        if request.method == 'POST':
            form = UploadForm(request.POST, instance=Blog)
            Blog.delete()
            return redirect('/')
        else:
            form = UploadForm(instance=Blog)
    except Exception as e:
            messages.warning(request, 'Your post was not deleted due to an error: { }'.format(e))

    context = {
        'form': form,
        'blog': Blog,
    }
    return render(request, template, context)



