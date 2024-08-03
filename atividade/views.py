from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,"index.html" )

def guilherme(request):
    return render(request, "guilherme.html")