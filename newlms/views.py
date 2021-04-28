from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from account.models import Account
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from account.models import Account
from class_.models import Class
from newlms.code import randomcode
from teacher.models import Teacher


# home page
def home(request):
    return render(request, 'login.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST.get('email')
        p = request.POST['password']
        user = authenticate(email=u, password=p)
        if user is not None:
            login(request, user)
            if request.user.is_manager:
                return redirect('manager_view')
            elif request.user.is_teacher:
                return redirect('teacher_view')
            elif request.user.is_student:
                return redirect('student_view')
            else:
                pass
        else:
            messages.error(request, 'Enter the valid username and password')
            return redirect('signin')


def changepassword(request):
    if request.method == 'GET':
        return render(request, 'changepassword.html')
    else:
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            user = Account.objects.get(id=request.user.id)
            user.password = make_password(p1)
            user.is_firstLogin = False
            user.save()
            return redirect('signin')
        else:
            messages.add_message(request,messages.ERROR, 'password does not match')
            return redirect('change_password')


def signout(request):
    logout(request)
    return redirect('signin')
