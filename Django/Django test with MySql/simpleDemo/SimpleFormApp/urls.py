from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('form/', views.index, name="simpleTest"),
    path('submitData/', views.saveData, name="SaveData"),
]
