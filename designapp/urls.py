from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('archived',views.archived,name='archived'),
    path('a',views.a,name='a'),
    path('swipe',views.swipe,name='swipe'),
        path('swipearchive',views.swipearchive,name='swipearchive'),





]