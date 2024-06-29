from django.urls import path
from . import views
from .views import article_list

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/delete/<int:article_id>/', views.article_delete, name='article_delete'),
    path('article/update/<int:article_id>/', views.article_update, name='article_update'), 
    path('chatbot/', views.chatbot_view, name='chatbot'),
]



