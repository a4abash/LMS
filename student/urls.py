from django.urls import path
from . import views

urlpatterns = [
    path('student', views.student_view, name='student_view'),
    path('search', views.search, name='search'),
    path('join/<int:id>', views.join, name='join')
]