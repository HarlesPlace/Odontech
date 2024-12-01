from django.urls import path
from . import views

app_name = 'pacientes'
urlpatterns = [
    path('<int:pk>/', views.DetailCliente.as_view(), name='detailCliente'),
    path('update/<int:pk>/', views.UpdateCliente.as_view(), name='updateCliente'),
]