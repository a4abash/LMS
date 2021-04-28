from django.urls import path
from . import views

urlpatterns = [
    path('teacher', views.teacher_view, name='teacher_view'),
    path('class/<int:id>', views.classView, name='classView'),
    path('join/<int:id>',views.joinAccept,name='join_accept')
]