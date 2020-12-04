from django.urls import path
from . import views



app_name = 'home'

urlpatterns = [
    path('',views.home , name='home' ),
    path('manager',views.manager,name='manager'),
    path('manager/order',views.order,name="order"),

]