from django.shortcuts import render
from .models import Post

# Create your views here.
def homeview(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})