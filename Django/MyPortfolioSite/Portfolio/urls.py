from django.urls import path, include
from . import views
urlpatterns = [
    path('/', views.index, name='indexPage'),
    path('/contact/', views.contact, name='contactPage'),
    path('/about/', views.about, name='aboutPage'),
    path('/resume/', views.resume, name='resumePage'),
    path('/services/', views.services, name='servicesPage'),

]
