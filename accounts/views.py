from django.shortcuts import render, redirect

from django.contrib.auth.models import User 
from django.contrib import auth #계정권한

def signup(request):    #회원가입절차완료하는 함수 만들기
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])#계정생성
            auth.login(request, user)  #회원가입 후 자동으로 로그인
            return redirect('home') #home으로 돌아가라
    return render(request, 'signup.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) #db에 실제로 존재하는지 확인시키는 함수
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')