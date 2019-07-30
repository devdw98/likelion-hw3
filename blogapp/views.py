from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋
    blog_list = Blog.objects.all() #블로그 모든글 대상으로
    paginator = Paginator(blog_list, 3) #블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page') #request된 페이지가 뭔지 알아내고 (request페이지를 변수에 담아냄)
    posts = paginator.get_page(page) #request된 페이지를 얻어온 뒤 return 해준다
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id)) 
    #위의 모든 것 다 처리 후에 url로 넘기세요

def blogpost(request):
    #1. 입력된 내용 처리하는 기능 -> POST
    #2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html',{'form':form})