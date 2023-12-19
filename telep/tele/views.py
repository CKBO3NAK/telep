from tkinter import Image

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView, UpdateView, DetailView

from django.views.generic import TemplateView
from .models import *


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import PostForm
from .models import Images

def some_view(request):
   return render(None, 'pageNotFound.html')
def post(request):
    if request.method == 'POST':
        print(request.FILES)
        images = request.FILES.getlist('pro-image')
        print(images)
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.save()
            for image in images:
                Images.objects.create(
                    post = post_form,
                    image = image,
                )

            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect(f"/{post_form.pk}")
        else:
            print(postForm.errors)
    else:
        postForm = PostForm()
    return render(request, 'test.html',
                  {'postForm': postForm})


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'test.html', {'form': form, 'img_obj': img_obj})

    else:
        form = ImageForm()
        return render(request, 'test.html', {'form': form})




class ShowArticle(DetailView):
    model = Article
    template_name = "ShowArticle.html"

    def get_context_data(self, **kwargs):
        context = super(ShowArticle, self).get_context_data(**kwargs)

        context['article'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['imgs'] = Images.objects.all().filter(post=self.kwargs['pk'])

        return context

def adminka(request):
    return redirect('/home')

def home(request):
    return HttpResponse("<h1>Home page</h1> <p> <a href='/admin'>Админка только для админов</a>")

def telegraph(request):
    return render(request, 'Telegraph.html')

def test(request):
    return render(request, 'test.html')
@csrf_exempt
def check(request):
    return JsonResponse({})
def pageNotFound(request, exception):
    return render(request, 'pageNotFound.html')


def pageNotFound500(exception):
    return redirect('/pageNotFound')

