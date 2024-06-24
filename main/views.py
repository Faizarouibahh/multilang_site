from django.shortcuts import render, get_object_or_404
from .models import Article


def home(request):
    return render(request, 'main/home.html')  # Assurez-vous que le chemin du template est correct


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/article_detail.html', {'article': article})
