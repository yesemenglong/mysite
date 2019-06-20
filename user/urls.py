from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('user_info', views.user_info, name='user_info'),
    path('login/', views.login_view, name='login'),
    path('login_for_modal', views.login_for_model, name='login_for_modal'),
    path('register/', views.register, name='register'),
    path('change_nickname/', views.change_nickname, name='change_nickname'),
    path('bind_email/', views.bind_email, name='bind_email'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password')
]
