from django.urls import path, include
from .views import *
from . import views
from funcionarios import urls

app_name = 'contas'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('', LoginView.as_view(), name='login'),
    path('profile/', views.user_profile, name='profile'),

]
