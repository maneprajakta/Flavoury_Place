from django.urls import path
from . import views



app_name = 'home'

urlpatterns = [
    path('',views.home , name='home' ),
    path('manager',views.manager,name='manager'),
    path('manager/about_us',views.about_us,name="about_us"),
    path('manager/chef',views.about_us,name="about_us"),
    path('manager/why_choose_us',views.about_us,name="about_us"),
    path("manager/updateAboutus",views.updateAboutus, name="updateAboutus"),
]