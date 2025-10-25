from django.shortcuts import render, get_object_or_404
from .models import Post, Page

# Create your views here.

def home(request):
    return render(request, 'main/home.html', context={"title": "Home"})


def post(request, post_name):
    post = get_object_or_404(Post, title=post_name)
    post_name = post.title
    page = get_object_or_404(Page.objects.filter(post=post))
    page_content = page.content
    print(page_content)
    return render(request, 'main/post.html', context={"title": post_name, "content": page_content})