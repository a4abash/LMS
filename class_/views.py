from django.shortcuts import render, redirect
from account.models import Account
from class_.models import Class
from newlms.code import randomcode
from teacher.models import Teacher


def addclass(request):
    if request.method == 'GET':
        a = Account.objects.get(id=request.user.id)
        b = Teacher.objects.get(user_id=request.user.id)
        c = Class.objects.get(teacher_id=request.user.id)
        print(request.user.id)
        context = {
            'user': a,
            'klass': c
        }
        return render(request, 'teacher/dashboard.html', context)
    else:
        cname = request.POST.get('classname')
        sec = request.POST.get('secname')
        sub = request.POST.get('subname')
        user = Account.objects.get(id=request.user.id)
        class_ = Class(name=cname, section=sec, subject=sub, code=randomcode(), teacher_id=user.teacher.id)
        class_.save()
        return redirect('teacher_view')
