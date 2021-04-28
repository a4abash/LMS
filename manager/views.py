from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from account.models import Account
from teacher.models import Teacher
from student.models import Student
from newlms.password import getRandomPassword
from django.contrib.auth.hashers import make_password
from newlms.mail import Mail
from django.contrib import messages

# Create your views here.


def manager_view(request):
    return render(request, 'manager/dashboard.html')


def manager_stdview(request):
    if request.method == 'GET':
        return render(request, 'manager/stddashboard.html')
    else:
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = getRandomPassword()
        user = Account(email=email, password=make_password(password), is_student=True, is_manager=False)
        user.save()
        msg = f'{name}, Your Account is created successfully, to log into your account \n please use \n email: {email} \n password : {password}'
        Mail(subject='Account Created', message=msg, recipient_list=[email])
        student = Student(name=name, user_id=user.id)
        student.save()
        messages.success(request, "Account created successfully please do check your email")
        return redirect('manager_stdview')



def manager_teachview(request):
    if request.method == 'GET':
        return render(request, 'manager/teachdashboard.html')
    else:
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = getRandomPassword()
        user = Account(email=email, password=make_password(password), is_teacher=True, is_manager=False)
        user.save()
        msg = f'{name}, Your Account is created successfully, to log into your account \n please use \n email: {email} \n password : {password}'
        Mail(subject='Account Created', message=msg, recipient_list=[email])
        teacher = Teacher(name=name, user_id=user.id)
        teacher.save()
        messages.success(request, "Account created successfully please do check your email")
        return redirect('manager_teachview')


