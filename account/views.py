# Create your views here.
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('passwordCheck')
        email = request.POST.get('email')
        
        response = {}
        users = User(
            username = username,
            password = password,
            email = email
        )
        users.save()
        return render(request, 'signup.html')