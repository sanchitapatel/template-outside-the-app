from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'app/home.html')
def home(request):
    return HttpResponse("Welcome to home page")