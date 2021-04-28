from django.urls import path
from . import views

urlpatterns = [
    path('class', views.addclass, name='addclass')
]