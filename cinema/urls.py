from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('user_login', views.user_login, name='user_login'),
    path('login_page', views.login_page, name='login_page'),
]