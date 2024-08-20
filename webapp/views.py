from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.




def home(request):
    return HttpResponse("<center><h1>Welcome to First Django deployment on Vercel")


