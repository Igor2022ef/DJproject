from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Главная страница приложения.")

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')