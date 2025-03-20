from blog.models import Post,Category
from django.shortcuts import render 
from django.http import HttpResponse
def frontpage(request):
    categorys = Category.objects.filter()
    posts = Post.objects.filter(status=Post.ACTIVE)
    print(categorys)
    return render(request,'core/frontpage.html',{'posts':posts,'categorys':categorys})

def about(request):
    return render(request,'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")