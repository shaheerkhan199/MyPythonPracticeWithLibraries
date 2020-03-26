
from django.urls import path, include
from . import views
urlpatterns = [
    path('/', views.chat, name='chatbottest'),
    path('/chatWindow/', views.index, name='fontend'),
]
