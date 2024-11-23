from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from pacientes.models import Cliente
from funcionarios.models import Dentista

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password',
                  'confirm_password'
        ]

        labels = {'first_name':"Nome",
                'last_name':"Sobrenome",
                'email':"Email", 
                'password':"Senha",
                'confirm_password':"Confirmar senha"
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        
    def save(form,commit=True):
        user=super().save(commit=False) 
        user.tipo_usuario= 'client'
        user.username = user.email
        user.set_password(form.cleaned_data.get("password"))
        if commit: 
            user.save()
            Cliente.objects.create(usuario=user,nome=(f'{user.first_name} {user.last_name}'))
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

class UserDentistsRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password',
                  'confirm_password'
        ]

        labels = {'first_name':"Nome",
                'last_name':"Sobrenome",
                'email':"Email", 
                'password':"Senha",
                'confirm_password':"Confirmar senha"
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        
    def save(form,commit=True):
        dentistaUser=super().save(commit=False) 
        dentistaUser.tipo_usuario= 'dentist'
        dentistaUser.username = dentistaUser.email
        dentistaUser.set_password(form.cleaned_data.get("password"))
        if commit: 
            dentistaUser.save()
            Dentista.objects.create(usuario=dentistaUser,nome=(f'{dentistaUser.first_name} {dentistaUser.last_name}'))
        return dentistaUser