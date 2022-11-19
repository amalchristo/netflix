from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')

def movies(request):
    return render(request,'movies.html')

def tvshows(request):
    return render(request,'Tvshows.html')
# Create your views here.
