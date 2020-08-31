from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'red01/login.html')

def home(request):
    return HttpResponse("Hello, Django!")