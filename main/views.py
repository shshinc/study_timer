from django.shortcuts import render,redirect
from .models import Post

def index(request):
    return render(request, 'index.html')

def after(request):
    goal = request.POST.get('goal')
    context = {'goal': goal,}
    return render(request, 'after.html', context)