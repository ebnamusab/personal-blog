from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About, ContactSettings, Blog


def home(request):
    blog = Blog.objects.all()
    slides = blog[0:3] 
    # print('slides', slides )
    five_blogs = blog[3:8]
    context = {
        'slides': slides,
        'five_blogs': five_blogs
    }
    return render(request, 'index.html', context)

def about_page(request):
    about = About.objects.last()
    print('test about', about.titlle)

    context = {
        'about': about
    }
    return render(request, 'about.html', context)



def contact_us(request):
    contact = ContactSettings.objects.last()

    context = {
        'contact': contact
    }
    return render(request, 'contact.html', context)


def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)

def blog_detail(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        'blog': blog
    }
    return render(request, 'single.html', context)

