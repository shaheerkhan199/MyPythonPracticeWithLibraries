from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ChatBotIndex'),
    path('ChatWindow', views.render_chat_window, name='ChatWindow'),
]
