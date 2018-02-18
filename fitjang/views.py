from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def add_data(request):
    return render(request, 'add_data.html')

def show(request):
    return render(request, 'show.html')
