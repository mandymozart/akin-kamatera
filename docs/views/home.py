# docs/views/home.py

from django.shortcuts import render

def HomeView(request):
    message = "Hello, World!"
    return render(request, 'views/docs/home.html', {'message': message})