from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout, login_required
from django.views import View
from django.contrib import messages
from .forms import UserRegistrationForm

User = get_user_model()

class RegisterUserView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário registrado com sucesso!")
            return redirect('accounts:login')
        else:
            messages.error(request, "Erro ao registrar o usuário. Verifique os dados.")
        return render(request, 'accounts/register.html', {'form': form})
    

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('home')  # Substitua pelo nome da view principal
        else:
            messages.error(request, "Credenciais inválidas. Tente novamente.")
        return render(request, 'accounts/login.html')
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

