from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):  
    posts = Post.objects.filter(yayinlama_tarihi__lte=timezone.now()).order_by('yayinlama_tarihi')   
    return render(request, 'blog/post_list.html', { 'posts': posts})
