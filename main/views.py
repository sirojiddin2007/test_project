from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *


def index_view (request):
    active_category = Category.objects.get(is_active=True)
    context = {
        'banner': Banner.objects.all().order_by('-id')[:3],
        'info': Info.objects.last(),
        'about': About.objects.last(),
        'services': Service.objects.all().order_by('-id')[:3],
        'meal': Meal.objects.all().order_by('-id')[:6],
        'menu1': Meal.objects.all().order_by('-id')[6:10],
        'menu2': Meal.objects.all().order_by('-id')[10:14],
        'client': Client.objects.all().order_by('-id')[:4],
        'categories':Category.objects.all().order_by('-id')[:4],
        'test': Testimonial.objects.all().order_by('-id')[:4],
        'blog':Block.objects.all().order_by('-id')[:3],
        'active_meal':Meal.objects.filter(category=active_category).order_by('-id')[:3]
    }
    return render(request,"index.html", context)


def filter_meal_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'banner': Banner.objects.all().order_by('-id')[:3],
        'info': Info.objects.last(),
        'about': About.objects.last(),
        'services': Service.objects.all().order_by('-id')[:3],
        'meal': Meal.objects.all().order_by('-id')[:6],
        'menu1': Meal.objects.all().order_by('-id')[6:10],
        'menu2': Meal.objects.all().order_by('-id')[10:14],
        'client': Client.objects.all().order_by('-id')[:4],
        'categories': Category.objects.all().order_by('-id')[:4],
        'test': Testimonial.objects.all().order_by('-id')[:4],
        'block':Block.objects.all().order_by('-id')[:3],
        'filter_meal':Meal.objects.filter(category=category)
    }
    return render(request,"index.html", context)


def menu_view(request):
    return render(request,'menu.html')


def service_view(request):
    return render(request,'services.html')


def blog_view(request):
    return render(request,'blog.html')


def about_view(request):
    return render(request,'about.html')


def blog_single_view(request):
    return render(request,'blog-single.html')


def contact_view(request):
    return render(request,'contact.html')


def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request,usr)
            return redirect('index_url')
    return render(request, 'log-in.html')


def signup_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('index_url')
    return render(request,'sign_up.html')


def logout_view(request):
    logout(request)
    return redirect('login_url')


def myprofile_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'myprofile.html', context)