from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('produit/ajouter/', views.produit_create, name='produit_create'),
    path('produit/<int:pk>/modifier/', views.produit_update, name='produit_update'),
    path('produit/<int:pk>/supprimer/', views.produit_delete, name='produit_delete'),
    path('login/', views.login_view, name='login'),
]
