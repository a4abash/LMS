from django.urls import path
from . import views

urlpatterns = [
    path('manager', views.manager_view, name='manager_view'),
    path('managerstd', views.manager_stdview, name='manager_stdview'),
    path('managerteach', views.manager_teachview, name='manager_teachview'),
]