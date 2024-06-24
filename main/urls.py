from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ajouter une vue d'accueil si elle n'existe pas
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]




