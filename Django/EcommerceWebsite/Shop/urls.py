from django.urls import path
from matplotlib.rcsetup import validate_nseq_int

from . import views

urlpatterns = [
    path('', views.index, name='shopIndex'),
    path('login/', views.login, name='loginPage'),
    path('signup/', views.signup, name='signupPage'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('productDetails/<int:p_id>/', views.product_details, name='productDetails'),
]
