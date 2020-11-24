from django.shortcuts import render,redirect
from meals.models import Meals , Category
from blog.models import Post
from aboutus.models import Why_Choose_Us ,AboutUs
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