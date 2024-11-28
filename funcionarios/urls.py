from django.urls import path
from . import views

app_name = 'funcionarios'
urlpatterns = [
    path('dentista/', views.ListDentista.as_view(), name='indexDentista'),
    path('dentista/<int:pk>/', views.DetailDentista.as_view(), name='detailDentista'),
    path('dentista/horario/<int:pk>/', views.CreateRestricaoDentista.as_view(), name='horarioDentista'),
    path('dentista/horario/<int:pk>/delete/', views.DeleteRestricao.as_view(), name='deleteRestricao'),
    path('dentista/update/<int:pk>/', views.UpdateDentista.as_view(), name='updateDentista'),
    path('dentista/delete/<int:pk>/', views.DeleteDentista.as_view(), name='deleteDentista'),
    path('dentista/create/', views.CreateUserDentista.as_view(), name='createUserDentista'),
    path('dentista/search/', views.searchDentista, name='searchDentista'),
    path('secretaria/', views.ListSecretario.as_view(), name='indexSecretario'),
    path('secretaria/<int:pk>/', views.DetailSecretario.as_view(), name='detailSecretario'),
    path('secretaria/update/<int:pk>/', views.UpdateSecretario.as_view(), name='updateSecretario'),
    path('secretaria/delete/<int:pk>/', views.DeleteSecretario.as_view(), name='deleteSecretario'),
    path('secretaria/create/', views.CreateUserSecretario.as_view(), name='createUserSecretario'),
    path('secretaria/search/', views.searchSecretario, name='searchSecretario'),
    #path('search/', views.search_post, name='search'),
    #path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment'),
    #path('category/', views.categoryListView.as_view(), name='categoryList'),
    #path('cetegory/<int:pk>/', views.categoryDetailView.as_view(), name='categoryDetail'),
]