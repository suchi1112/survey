from django.urls import path
from . import views

urlpatterns = [

    path('',views.register,name='register'),
    path('add_survey',views.add_survey,name='add_survey'),
    path('index',views.index,name='index'),
    path('thank',views.thank,name='thank'),
    ]