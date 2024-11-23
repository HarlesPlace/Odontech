from django.forms import ModelForm
from django import forms
from .models import Dentista,Secretario
from django.contrib.auth import get_user_model
from pacientes.models import Cliente

User = get_user_model()

class UserDentistaRegistrationForm(forms.ModelForm):
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
        userdentista=super().save(commit=False) 
        userdentista.tipo_usuario= 'dentist'
        userdentista.username = userdentista.email
        userdentista.set_password(form.cleaned_data.get("password"))
        if commit: 
            userdentista.save()
            Dentista.objects.create(usuario=userdentista,nome=(f'{userdentista.first_name} {userdentista.last_name}'))
        return userdentista
    
class DentistaForm(ModelForm):
    class Meta:
        model=Dentista
        fields=[
            'nome','cpf',
            'cro', 'especialidade',
            'telefone', 'salario',
            'data_contratacao','clinica',
            'rua','numero_residencial',
            'bairro','cep','cidade','estado',
        ]
        labels=[
            'Nome', 'CPF', 'CRO',
            'Especialidade',
            'Telefone', 'Salário',
            'Data Contratacao','Clínica',
            'Rua','Numero residencial',
            'Bairro','CEP','Cidade','Estado',
        ]

class UserSecretarioRegistrationForm(forms.ModelForm):
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
        usersecretario=super().save(commit=False) 
        usersecretario.tipo_usuario= 'secretary'
        usersecretario.username = usersecretario.email
        usersecretario.set_password(form.cleaned_data.get("password"))
        if commit: 
            usersecretario.save()
            Secretario.objects.create(usuario=usersecretario,nome=(f'{usersecretario.first_name} {usersecretario.last_name}'))
        return usersecretario
    
class SecretarioForm(ModelForm):
    class Meta:
        model=Secretario
        fields=[
            'nome','cpf',
            'telefone', 'salario',
            'data_contratacao','clinica',
            'rua','numero_residencial',
            'bairro','cep','cidade','estado',
        ]
        labels=[
            'Nome', 'CPF', 
            'Telefone', 'Salário',
            'Data Contratacao','Clínica',
            'Rua','Numero residencial',
            'Bairro','CEP','Cidade','Estado',
        ]