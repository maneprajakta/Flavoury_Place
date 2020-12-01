from django.shortcuts import render,redirect
from meals.models import Meals , Category
from blog.models import Post
from aboutus.models import Why_Choose_Us ,AboutUs,Chef
# Create your views here.


def home(request):

    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()


    
    context = {
        'meals' : meals ,
        'meal_list' : meal_list ,
        'categories' : categories ,
        'posts' : posts ,
        'latest_post' : latest_post ,
        'why_choose_us' : why_choose_us , 
    }

    return render(request , 'home/index.html' , context)

def manager(request):
    return render(request , 'home/manager.html')

def about_us(request):
    obj = AboutUs.objects.all()
    context = {'about_us':obj}
    return render(request , 'home/about_us.html',context)

def updateAboutus(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        old_title = request.POST['old_title']
        obj = AboutUs.objects.get(title=old_title)
        obj.title = title
        obj.content = content
        obj.save()
    return redirect('/manager/')

def updateChef(request):
    if request.method == 'POST':
        name = request.POST['name']
        title = request.POST['title']
        bio = request.POST['bio']
        image = request.POST['image']
        old_name = request.POST['old_name']
        obj = Chef.objects.get(name=old_name)
        obj.name = name
        obj.title = title
        obj.bio = bio
        obj.image = image
        obj.save()
    return redirect('/manager')


def chef(request):
    obj = Chef.objects.all()
    context = {'chef':obj}
    return render(request , 'home/chef.html',context)

def order(request):
    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    context = {
        'meals' : meals ,
        'meal_list' : meal_list ,
        'categories' : categories 
    }
    return render(request , 'home/order.html',context)