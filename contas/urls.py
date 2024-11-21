from django.urls import path
from .views import *
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', user_profile, name='profile'),
    path('signup/', views.signup, name='signup'),
]
