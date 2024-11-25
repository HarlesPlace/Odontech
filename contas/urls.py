from django.urls import path
from .views import *
from . import views

app_name = 'contas'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.user_profile, name='profile'),
]
