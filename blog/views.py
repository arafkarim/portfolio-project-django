from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', { 'blogs': blogs })

def detail(request, blod_id):
    detail = get_object_or_404(Blog, pk=blod_id)
    return render(request, 'blog/detail.html', { 'detail': detail })
