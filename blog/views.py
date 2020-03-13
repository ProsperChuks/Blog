from django.shortcuts import render as r
from django.http import HttpResponseRedirect, HttpResponse as hr
from .models import posts, comment as cmm
from .forms import *
from rest_framework import viewsets
from .serializer import postSerializer
from .models import posts

class postViewSet(viewsets.ModelViewSet):
    queryset = posts.objects.all()
    serializer_class = postSerializer

# Create your views here.
def hero(request):
    post = posts.objects.all()[:10]
    context = {
        'title':'Blog Application',
        'post' : post
    }
    return r(request, 'blog/index.html', context)

def post(request, id):
    post = posts.objects.get(id=id)
    form = contactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']

    form = commentForm()
    context = {
        'post' : post,
        'form' : form,
        'comment' : 'Comments'
    }
    return r(request, 'blog/post.html', context)

def about(request):
    return r(request, 'blog/about.html')

def contact(request):

    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

    form = contactForm()
    return r(request, 'blog/contact.html', {'form':form})

def coment(request):
    return hr("<h1>validated</h1>")
