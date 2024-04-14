from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
 return render(request,'home1.html')

def mem(request):
 return render(request,'membership.html')
 
def index(request):
 return render(request,'home0.html') 


def signup(request):
 return render(request,'signup.html') 

def forgot(request):
 return render(request,'forgot.html')

def profile(request):
 return render(request,'profile.html') 
 


