from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from pacientes.models import Cliente
from funcionarios.models import Dentista
from django.contrib.auth.models import Group, Permission

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
            try:
                user_group = Group.objects.get(name="cliente")
            except Group.DoesNotExist:
                user_group = Group(name="cliente")
                user_group.save()
                user_group.permissions.set([Permission.objects.get(codename=c) for c in ["add_user", "change_user", "view_user", "view_clinica", "add_consulta", "change_consulta", "view_consulta", "view_exame", "view_pedido", "view_dentista", "change_cliente", "view_cliente","view_procedimento",]])
            user.groups.add(user_group)
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
            try:
                user_group = Group.objects.get(name="dentista")
            except Group.DoesNotExist:
                user_group = Group(name="dentista")
                user_group.save()
                user_group.permissions.set([Permission.objects.get(codename=c) for c in ["add_user", "change_user", "view_user", "view_clinica", "add_consulta", "change_consulta", "view_consulta","delete_consulta","add_restricao","change_restricao","delete_restricao","view_restricao", "view_exame","add_exame","change_exame","delete_exame", "view_pedido","add_pedido","change_pedido","delete_pedido", "view_dentista","change_dentista", "change_cliente", "view_cliente","view_procedimento","view_secretario","add_procedimento","change_procedimento","delete_procedimento",]])
            dentistaUser.groups.add(user_group)
        return dentistaUser