from django.shortcuts import render as r
from django.http import HttpResponseRedirect, HttpResponse as hr
from .models import posts
from .forms import NameForm

# Create your views here.
def hero(request):
    post = posts.objects.all()[:10]
    context = {
        'title':'Blog Application',
        'post' : post,
    }
    return r(request, 'blog/index.html', context)

def post(request, id):
    post = posts.objects.get(id=id)
    context = {
        'post' : post
    }
    return r(request, 'blog/post.html', context)

def about(request):
    return r(request, 'blog/about.html')

def contact(request):
    return r(request, 'blog/contact.html')

# Creating a form
def get_name(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        #validating the form
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        # else it generates an empty form
        form = NameForm()
    return r(request, 'blog/post.html', {'form' : form})
