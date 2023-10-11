from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
def index_view(request):
    context = {
        'new': News.objects.last(),
        'news': News.objects.all().order_by('-id')[1:3],
        'news_b': News.objects.all().order_by('-id')[3:5],
        'category':Category.objects.all(),
        'd_miss' : News.objects.all().order_by('-id')[5:8]
    }
    return render(request, 'index.html', context)



def search_view(request):
    title = request.GET.get('search')
    context={
        's_news': News.objects.filter(title__icontains=title),
        'category': Category.objects.all(),
    }
    return render(request, 'seacrh.html', context)


def about_view(request):
    context = {
        'about': About_us.objects.last(),
        'our_teams': Our_team.objects.all().order_by('-id')[:4],
        'category': Category.objects.all(),
    }
    return render(request, 'about-us.html', context)


def contact_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST['email']
        message = request.POST["message"]
        Address.objects.create(
            name=name,
            email=email,
            message=message,
        )
        return redirect('contact_url')
    context = {
    'category': Category.objects.all(),
   }
    return render(request, 'contact.html', context)



def category_view(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'category_news' : News.objects.filter(category=category),
        'category': Category.objects.all(),
    }
    return render(request, 'catagory.html', context)


def single_view(request, pk):
    new = News.objects.get(pk=pk)
    context ={
        'new' : new,
        'category': Category.objects.all(),
    }
    return render(request, 'single-post.html', context)


def create_blog_view(request):
    if request.method == "POST":
        title = request.POST['title']
        img = request.FILES.get('img')
        category = request.POST['category']
        date = request.POST['date']
        text = request.POST['text']
        News.objects.create(
            title=title,
            category_id=category,
            text=text,
            img=img,
            date=date,
        )
        return redirect('index_url')
    context ={
        'category':Category.objects.all()
    }
    return render(request, 'create-blog.html', context)



def update_blog_view(request, pk):
    new = News.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST['title']
        img = request.FILES.get('img')
        category = request.POST['category']
        date = request.POST['date']
        text = request.POST['text']
        new.title = title
        new.category_id = category
        new.date = date
        new.text = text
        if img is not None:
            new.img = img
        new.save()
        return redirect('single_url', new.id)
    context = {
        'category': Category.objects.all(),
        'new':new
    }
    return render(request, 'update-blog.html',context)


def delete_blog_view(request, pk):
    new = News.objects.get(pk=pk)
    new.delete()
    return redirect('index_url')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request,usr)
            return redirect('index_url')
    return render(request, 'log-in.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(
            username=username,
            password=password,
        )
        return redirect('index_url')
    return render(request, 'log-up.html')


def logout_view(request):
    logout(request)
    return redirect('signup_url')


def profile_view(request,pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)



def delete_user_view(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('signup_url')



def edit_user_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST.get('email')
        img = request.POST.get('img')
        bio = request.POST.get('bio')
        old_password = request.POST.get['old_password']
        new_password = request.POST.get['new_password']
        confirm_password = request.POST.get['confirm_password']
        user.username = username
        user.bio = bio
        if img is not None:
            user.photo = img
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return redirect("profile_url", user.pk)
            context={
                'user': user
            }
            return render(request, 'edit-user',context)