from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Главная страница приложения.")

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def archive(request, year):
    if (int(year) > 2020):
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")