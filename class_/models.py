from django.db import models
from teacher.models import Teacher
from student.models import Student
from account.models import Account
# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=3, null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    code = models.CharField(max_length=10, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Join(models.Model):
    clas = models.ForeignKey(Class,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name

    class Meta:
        unique_together = ['clas', 'student']


class Stream(models.Model):
    discussion = models.TextField()
    file = models.FileField(blank=True, null=True)
    cls = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.cls.name
