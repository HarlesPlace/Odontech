from django.urls import path
from . import views

app_name = 'procedimentos'
urlpatterns = [
    path('', views.ListProcedimento.as_view(), name='indexProcedimento'),
    path('<int:pk>/', views.DetailProcedimento.as_view(), name='detailProcedimento'),
    path('update/<int:pk>/', views.UpdateProcedimento.as_view(), name='updateProcedimento'),
    path('delete/<int:pk>/', views.DeleteProcedimento.as_view(), name='deleteProcedimento'),
    path('create/', views.CreateProcedimento.as_view(), name='createProcedimento'),
    path('search/', views.searchProcedimento, name='searchProcedimento'),
]