from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import User
from django.contrib.auth.decorators import login_required
from .forms import RawSearch
from django.http import Http404

@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    