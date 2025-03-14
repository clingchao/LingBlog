from django.shortcuts import redirect, render, get_object_or_404
from .models import Post,Category
from .forms import CommentForm
from django.db.models import Q

def detail(request, category_slug,slug):
    # 获取文章对象，如果不存在则返回 404
    post = get_object_or_404(Post, slug=slug)

    # 处理表单提交
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 创建评论对象但不保存到数据库(此时保存post是空的)
            comment = form.save(commit=False)
            # 将评论与文章关联
            comment.post = post
            # 保存评论到数据库
            comment.save()
            # 重定向到文章详情页
            return redirect('post_detail', slug=slug)
    else:
        # 如果是 GET 请求，创建一个空表单
        form = CommentForm()

    # 渲染模板并传递上下文数据
    return render(request, 'blog/detail.html', {'post': post,'form':form})


def category(request,slug):
    category = get_object_or_404(Category,slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request,'blog/category.html',{'category':category,'posts':posts})

def search(request):
    # 获取用户查找词
    query = request.GET.get('query','')
    # 模糊查询，使用Q
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query)|Q(intro__icontains=query)|Q(body__icontains=query))
    
    return render(request,'blog/search.html',{'posts':posts,'query':query})