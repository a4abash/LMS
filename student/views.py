from django.shortcuts import render, redirect
from class_.models import Class, Join
from student.models import Student
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def student_view(request):
    if request.user.is_firstLogin:
        return redirect('change_password')

    else:
        return render(request, 'student/dashboard.html')


def search(request):
    key = request.GET.get('key')
    clas = Class.objects.filter(Q(name__contains=key) | Q(code=key))
    all_join_id = Join.objects.filter(student_id=getCurrentlyLogInStudentId(request.user.id)).only('clas_id')
    class_id = [c.clas_id for c in all_join_id]
    context = {
        'class': clas,
        'class_id': class_id
    }
    return render(request, 'student/search.html', context)


def join(request, id):
    j = Join(clas_id=id, student_id=getCurrentlyLogInStudentId(request.user.id))
    j.save()
    messages.add_message(request, messages.SUCCESS, 'join request sent')
    return redirect('student_view')


def getCurrentlyLogInStudentId(id):
    s = Student.objects.get(user_id=id)
    return s.id