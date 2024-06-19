# main/views.py
# main/views.py
from django.shortcuts import render

def home(request):
    context = {
        'message': 'Bienvenue sur notre site !'
    }
    return render(request, 'main/home.html', context)
