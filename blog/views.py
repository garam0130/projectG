from django.shortcuts import render, redirect
from django.http import Http404
from blog.models import Post

def index(request):
    return render(request, 'blog/main.html', {})
