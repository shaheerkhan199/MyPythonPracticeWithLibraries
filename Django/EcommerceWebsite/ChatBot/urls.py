from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ChatBotIndex'),
    path('ChatWindow', views.render_chat_window, name='ChatWindow'),
    path('giveResponse', views.get_bot_response, name='ChatBot_Response')
]
