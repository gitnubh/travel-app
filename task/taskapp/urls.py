from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_content,name='home'),
    path('about/', views.about_content,name='about'),
    path('register/', views.registration,name='register'),
    path('login/', views.login_page,name='login'),
    path('browse/', views.browse_content,name='browse'),
    path('contact/', views.contact_content,name='contact'),
    path('compute/', views.compute_page,name='compute'),
    path('thanks/', views.thanks_content,name='thanks'),
    path('compute/result/',views.result_content,name='result'),
    path('logout/',views.logout_page,name='logout')
]