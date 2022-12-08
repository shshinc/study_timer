from django.shortcuts import render

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
        username = request.POST.get('username', '미서')
        password = request.POST.get('password', True)
        re_password = request.POST.get('passwordCheck', True)
 
        response = {}
        if not (username and password and re_password):
            response['error'] = '모든 값을 입력하세요.'
        if not username:
            response['error'] = '이름을 입력하세요.'
        if not password:
            response['error'] = '비밀번호를 입력하세요.'
        if password != re_password:
            response['error'] = '비밀번호를 확인하세요.'
        else:
            users = User(
                username = username,
                password = password
            )
            users.save()
        return render(request, 'signup.html', response)