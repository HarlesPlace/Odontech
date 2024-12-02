from django.forms import ModelForm
from django import forms
from .models import Dentista,Secretario
from django.contrib.auth import get_user_model
from consultas.models import Restricao
from django.contrib.auth.models import Group, Permission

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
            try:
                user_group = Group.objects.get(name="dentista")
            except Group.DoesNotExist:
                user_group = Group(name="dentista")
                user_group.save()
                user_group.permissions.set([Permission.objects.get(codename=c) for c in ["add_user", "change_user", "view_user", "view_clinica", "add_consulta", "change_consulta", "view_consulta","delete_consulta","add_restricao","change_restricao","delete_restricao","view_restricao", "view_exame","add_exame","change_exame","delete_exame", "view_pedido","add_pedido","change_pedido","delete_pedido", "view_dentista","change_dentista", "change_cliente", "view_cliente","view_procedimento","view_secretario","add_procedimento","change_procedimento","delete_procedimento",]])
            userdentista.groups.add(user_group)
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
            try:
                user_group = Group.objects.get(name="secretario")
            except Group.DoesNotExist:
                user_group = Group(name="secretario")
                user_group.save()
                user_group.permissions.set([Permission.objects.get(codename=c) for c in ["add_user", "change_user", "view_user", "view_clinica","change_clinica", "add_consulta", "change_consulta", "view_consulta","delete_consulta","add_restricao","change_restricao","delete_restricao","view_restricao", "view_exame","add_exame","change_exame","delete_exame", "view_pedido","delete_pedido", "view_dentista","change_dentista", "change_cliente", "view_cliente","view_procedimento","view_secretario","change_secretario","add_procedimento","change_procedimento","delete_procedimento",]])
            usersecretario.groups.add(user_group)
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

class RestricaoDentistaForm(ModelForm):
    data = forms.DateField(widget=forms.SelectDateWidget)
    hora_inicio = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    hora_fim = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    dentista=forms.HiddenInput
    class Meta:
        model=Restricao
        fields=[
            'data',
            'hora_inicio', 'hora_fim',
        ]
        labels=[
            'Data', 
            'Ínício', 'Término',
        ]

class SelecionarDentistaForm(forms.Form):
    dentista = forms.ModelChoiceField(
        queryset=Dentista.objects.all(),
        label="Selecione o Dentista",
        empty_label="Escolha um dentista",
        widget=forms.Select(attrs={'class': 'form-control'})
    )