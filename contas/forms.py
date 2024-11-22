from django import forms
from django.contrib.auth import get_user_model
from pacientes.models import Cliente

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
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
        if commit: 
            user.save()
            Cliente.objects.create(usuario=user,nome=(f'{user.first_name} {user.last_name}'))
        return user