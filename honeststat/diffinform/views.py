from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import numpy as np
np.random.seed(1)
import pandas as pd

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
#     graph_inf = Buildgraph.objects.all()
#     x1=[]
#     y1=[]
#     for g in graph_inf:
#         x1.append(g.name_product)
#         y1.append(g.cost)
#     plot_div = plot([Scatter(x=x1, y=y1,
#                 mode='lines', name='test',
#                 opacity=0.8, marker_color='green')],
#                 output_type='div')
#     context = {
#     'plot_div': plot_div,
#     'title': 'Графики статистических зависимостей',
#     }
#     return render(request, "diffinform/graph.html", context=context)

# def show_graph(request):
#     N = 100
#     x = np.random.rand(N)
#     y = np.random.rand(N)
#     colors = np.random.rand(N)
#     sz = np.random.rand(N) * 30
#     fig = go.Figure()
#     fig.add_trace(go.Scatter(
#         x=x,
#         y=y,
#         mode="markers",
#         marker=go.scatter.Marker(
#             size=sz,
#             color=colors,
#             opacity=0.6,
#             colorscale="Viridis"
#         )
#     ))
#     graph = fig.to_html(full_html=False, default_height=500, default_width=700)
#     context = {
#         'graph': graph,
#         'title': 'Графики статистических зависимостей',
#     }
#     return render(request, "diffinform/graph.html", context=context)

def show_graph(request):
    graph_inf = Buildgraph.objects.all()
    x1=[]
    y1=[]
    y2=[]
    frames1=[]
    for g in graph_inf:
        x1.append(g.name_product)
        y1.append(g.cost)
        y2.append((g.cost*2))
        frames1.append(go.Frame(data=[go.Scatter(x=x1, y=y1)]))
    # date =
    layout = go.Layout(title="Какой-то индекс", xaxis={'title': 'x1', 'titlefont.color': 'red'}, yaxis={'title': 'x2'},
                       legend={"visible":True})
    fig = go.Figure(layout=layout)
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Scatter(x=x1, y=y1, name='Первая'), 1, 1)
    fig.frames = frames1
    fig.add_trace(go.Scatter(x=x1, y=(y2), name='Вторая'), 1, 2)
    fig.update_layout(hovermode="x", updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])],)
    # fig.update_traces(hoverinfo="x+y")


    graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
    context = {
        'graph': graph,
        'title': 'Графики статистических зависимостей',
        }
    return render(request, "diffinform/graph.html", context=context)





def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
