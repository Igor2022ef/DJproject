from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

from plotly.offline import plot
from plotly.graph_objs import Scatter

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Построить графики", 'url_name': 'graph'},
        {'title': "Войти", 'url_name': 'login'},
]

def index(request):
    posts = Articles.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'diffinform/index.html', context=context)

def about(request):
    return render(request, 'diffinform/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'diffinform/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_slug):
    # post_check = Articles.objects.all()
    # print(post_check)
    post = get_object_or_404(Articles, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'diffinform/post.html', context=context)

def show_category(request, cat_slug):
    posts = Articles.objects.all()
    if len(posts) == 0:
        raise Http404()
    posts1=[]
    for p in posts:
        if p.cat.slug==cat_slug:
            posts1.append(p)
    context = {
        'posts': posts1,
        'title': cat_slug,
        'cat_selected': cat_slug,
    }
    return render(request, 'diffinform/index.html', context=context)

# def show_graph(request):
#     graph_dates = Buildgraph.objects.all()
#     context = {
#         'graph_inform': graph_dates,
#         'title': 'Графики статистических зависимостей',
#     }
#     return render(request, 'diffinform/graph.html', context=context)

def show_graph(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    context = {
    'plot_div': plot_div,
    'title': 'Графики статистических зависимостей',
    }
    return render(request, "diffinform/graph.html", context=context)



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
