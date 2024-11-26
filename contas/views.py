from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class RegisterUserView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'contas/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('passei')
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('contas:login')
        else:
            messages.error(request, "Erro ao registrar o usuário. Verifique os dados.")
        return render(request, 'contas/register.html', {'form': form})
    

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm() 
        return render(request, 'contas/login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                # Redirecionamento baseado no tipo de usuário
                '''Por enquanto, o login leva para página de perfil. 
                   Eventualmente levará para página esperada.

                if user.tipo_usuario == 'admin':
                    return redirect('contas:admin_home')  
                elif user.tipo_usuario == 'dentist':
                    return redirect('contas:dentist_home')
                elif user.tipo_usuario == 'client':
                    return redirect('contas:client_home') 
                elif user.tipo_usuario == 'secretary':
                    return redirect('contas:secretary_home')
                '''
                return redirect('contas:profile')
            else:
                messages.error(request, "Credenciais inválidas. Tente novamente.")
        return render(request, 'contas/login.html', {'form': form})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('contas:login')


@login_required
def user_profile(request):
    return render(request, 'contas/profile.html', {'user': request.user})