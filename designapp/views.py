from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'design.html')
def home(request):
    return render(request,'home.html')
def archived(request):
    return render(request,'archived.html')
def a(request):
    return render(request,'archive.html')
def swipe(request):
    return render(request,'swipe.html')
def swipearchive(request):
    return render(request,'swipearchive.html')
