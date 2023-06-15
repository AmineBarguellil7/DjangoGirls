from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

def ListPost(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Blog/affiche.html', {'p': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Blog/post_detail.html', {'post': post})    
