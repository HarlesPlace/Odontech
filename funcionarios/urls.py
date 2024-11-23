from django.urls import path
from . import views

app_name = 'funcionarios'
urlpatterns = [
    path('dentista/', views.ListDentista.as_view(), name='indexDentista'),
    path('dentista/<int:pk>/', views.DetailDentista.as_view(), name='detailDentista'),
    #path('search/', views.search_post, name='search'),
    path('dentista/update/<int:pk>/', views.UpdateDentista.as_view(), name='updateDentista'),
    path('dentista/delete/<int:pk>/', views.DeleteDentista.as_view(), name='deleteDentista'),
    path('dentista/create/', views.CreateUserDentista.as_view(), name='createUserDentista'),
    #path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment'),
    #path('category/', views.categoryListView.as_view(), name='categoryList'),
    #path('cetegory/<int:pk>/', views.categoryDetailView.as_view(), name='categoryDetail'),
]