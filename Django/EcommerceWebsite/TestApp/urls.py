from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='shopIndex'),
    # path('login/', views.login, name='loginPage'),
    # path('signup/', views.signup, name='signupPage'),
    path('hello/', views.index, name='testHello'),
    path('contact/', views.contact, name='contact'),
    path('showValue/', views.printValues, name='value'),
]
