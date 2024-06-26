from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import JsonResponse
import json
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'main/home.html')  # Assurez-vous que le chemin du template est correct

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/article_detail.html', {'article': article})

@csrf_exempt
def article_list(request):
    articles = Article.objects.all().values('id', 'title', 'content', 'publication_date')  
    articles_list = list(articles) 
    return JsonResponse({'articles': articles_list})

@csrf_exempt
def article_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data['title']
            content = data['content']
            publication_date = parse_datetime(data['publication_date'])
            
            article = Article.objects.create(
                title=title,
                content=content,
                publication_date=publication_date
            )
            return JsonResponse({'message': 'Article created successfully', 'article_id': article.id}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def article_delete(request, article_id):
    if request.method == 'DELETE':
        try:
            article = Article.objects.get(id=article_id)
            article.delete()
            return JsonResponse({'message': 'Article deleted successfully'}, status=200)
        except Article.DoesNotExist:
            return JsonResponse({'error': 'Article not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
@csrf_exempt
def article_update(request, article_id):
    if request.method == 'PUT':
        try:
            article = Article.objects.get(id=article_id)
            data = json.loads(request.body)
            
            if 'title' in data:
                article.title = data['title']
            if 'content' in data:
                article.content = data['content']
            if 'publication_date' in data:
                article.publication_date = parse_datetime(data['publication_date'])

            article.save()

            return JsonResponse({'message': 'Article updated successfully', 'article_id': article.id}, status=200)
        except Article.DoesNotExist:
            return JsonResponse({'error': 'Article not found. Create it first.'}, status=404)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)