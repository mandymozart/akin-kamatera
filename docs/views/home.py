# docs/views/home.py

from django.shortcuts import render

def HomeView(request):
    message = "Hello, World!"
    return render(request, 'templates/docs/home.html', {'message': message})