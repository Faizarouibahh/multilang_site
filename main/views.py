from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, HttpResponse
import json
from django.utils.dateparse import parse_datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import activate, get_language
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Article
from django.contrib.auth.forms import UserCreationForm

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles') 
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            if username and password:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return JsonResponse({'redirect_url': '/articles/'}, status=200)
                else:
                    return JsonResponse({'error': 'Invalid username or password.'}, status=401)
            else:
                return JsonResponse({'error': 'Username or password missing in JSON data.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

    
def logout(request):
    auth_logout(request)
    return redirect('home')

def home(request):
    return render(request, 'main/home.html')

def article_list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'main/article_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/article_detail.html', {'article': article})

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

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '')

        response_message = f"Vous avez dit : {message}. Je suis un simple chatbot !"
        return JsonResponse({'response': response_message})
    else:
        return render(request, 'main/chatbot.html')

def set_language(request):
    language = request.GET.get('language', 'en')
    next_url = request.GET.get('next', '/')

    activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language

    return redirect(next_url)
