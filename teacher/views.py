from django.shortcuts import render, redirect, HttpResponseRedirect
from account.models import Account
from .models import Teacher
from class_.models import Class, Join, Stream


# Create your views here.
def teacher_view(request):
    if request.user.is_firstLogin:
        return redirect('change_password')
    else:
        context = {
            'class':Class.objects.filter(teacher_id=getCurrentlyLogInTeacherId(request.user.id))
        }
        return render(request, 'teacher/dashboard.html',context)


def classView(request,id):
    if request.method == 'GET':
        s = Stream.objects.filter(cls_id=id)
        context = {
            'class':Class.objects.get(id=id),
            'join':Join.objects.filter(clas_id=id),
            'stream':s
        }
        return render(request,'teacher/class_details.html',context)
    else:
        d = request.POST.get('discussion')
        file = request.FILES.get('file')
        s = Stream(discussion = d, file=file, cls_id=id)
        s.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def joinAccept(request,id):
    j = Join.objects.get(id=id)
    j.is_approved=True
    j.save()
    return redirect('teacher_view')


def getCurrentlyLogInTeacherId(id):
    t=Teacher.objects.get(user_id=id)
    return t.id