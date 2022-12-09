# Create your views here.
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

# Create your views here.
# 회원가입
def signup(request):
    signup_db=User.objects.all()
    
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('passwordCheck')
        email = request.POST.get('email')
        
        response = {}
        
        if signup_db.filter(email = request.POST.get('email')).exists():
            response['error'] = '중복된 email 주소입니다.'
            return render(request, 'signup.html', {'response': response['error']})
        if signup_db.filter(username = request.POST.get('username')).exists():
            response['error'] = '중복된 이름입니다.'
            return render(request, 'signup.html', {'response': response['error']})
        if signup_db.filter(password = request.POST.get('password')).exists():
            response['error'] = '중복된 비밀번호입니다.'
            return render(request, 'signup.html', {'response': response['error']})
        
        users = User(
            username = username,
            password = password,
            email = email
        )
        users.save()
        return render(request, 'login.html')
    
def login(request):
    signin_db=User.objects.all()
    
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(request, email=email, password=password)
        response = {}
        
        if signin_db.filter(email).exists():
            if signin_db.filter(password).exists():
                auth.login(request, user)
                return render(request, 'main')
            else:
                response['error'] = '비밀번호를 확인해주세요'
                return render(request, 'login.html', {'response': response['error']})
        else:
            response['error'] = '메일 주소를 확인해주세요'
            return render(request, 'login.html', {'response': response['error']})