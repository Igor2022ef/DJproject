from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    posts = Articles.objects.all()
    return render(request, 'diffinform/index.html', {'posts': posts,'menu': menu,'title': 'Главная страница'})

def about(request):
    return render(request, 'diffinform/about.html', {'title': 'О сайте'})

# def categories(request, cat):
#     if (request.GET):
#         print(request.GET)
#     return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")

# def archive(request, year):
#     if (int(year) > 2020):
#         return redirect('/')
#     return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
