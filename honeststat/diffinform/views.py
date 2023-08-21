from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .utils import *
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


class ArticlesHome(DataMixin, ListView):
    model = Articles
    template_name = 'diffinform/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context = dict(list(context.items()) + list(c_def.items()))
        # context['menu'] = menu                # реализовано через tags
        return context

    def get_queryset(self):
        return Articles.objects.filter(is_published=True)

# @login_required                                        декоратор ограничивает доступ не авторизованных пользователей
def about(request):
    contact_list = Articles.objects.all()
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'diffinform/about.html', {'page_obj': page_obj, 'menu': menu, 'title': 'О сайте'})

class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'diffinform/addpage.html'
    extra_context = {'title': 'Добавление статьи'}
    success_url = reverse_lazy('home')                   #Иначе работает метод get_absolute_url
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")
        return dict(list(context.items()) + list(c_def.items()))

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

class ShowPost(DataMixin, DetailView):
    model = Articles
    template_name = 'diffinform/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['post'])
        return dict(list(context.items()) + list(c_def.items()))

class ArticlesCategory(DataMixin, ListView):
    model = Articles
    template_name = 'diffinform/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Articles.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

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

# def show_graph(request):
#     graph_inf = Buildgraph.objects.all()
#     x1=[]
#     y1=[]
#     y2=[]
#     frames1=[]
#     for g in graph_inf:
#         x1.append(g.date)
#         y1.append(g.cost)
#         y2.append((g.cost*2))
#         frames1.append(go.Frame(data=[go.Scatter(x=x1, y=y1)]))
#     layout = go.Layout(title="Какой-то индекс", xaxis={'title': 'x1', 'titlefont.color': 'red'}, yaxis={'title': 'x2'},
#                        legend={"visible":True})
#     fig = go.Figure(layout=layout)
#     fig = make_subplots(rows=1, cols=2)
#     fig.add_trace(go.Scatter(x=x1, y=y1, name='Первая'), 1, 1)
#     fig.frames = frames1
#     fig.add_trace(go.Scatter(x=x1, y=(y2), name='Вторая'), 1, 2)
#     fig.update_layout(hovermode="x", updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])],)
#
#     graph = fig.to_html(full_html=False, default_height=600, default_width=1000)
#     context = {
#         'graph': graph,
#         'title': 'Графики статистических зависимостей',
#         }
    # return render(request, "diffinform/graph.html", context=context)

class Graph(DataMixin, ListView):
    model = Buildgraph
    template_name = 'diffinform/graph.html'
    extra_context = {'title': 'Построение графиков'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Построение графиков")
        graph_inf = Buildgraph.objects.all()
        x1 = []
        y1 = []
        y2 = []
        frames1 = []
        for g in graph_inf:
            x1.append(g.date)
            y1.append(g.cost)
            y2.append((g.cost * 2))
            frames1.append(go.Frame(data=[go.Scatter(x=x1, y=y1)]))
        layout = go.Layout(title="Какой-то индекс", xaxis={'title': 'x1', 'titlefont.color': 'red'},
                           yaxis={'title': 'x2'},
                           legend={"visible": True})
        fig = go.Figure(layout=layout)
        fig = make_subplots(rows=1, cols=2)
        fig.add_trace(go.Scatter(x=x1, y=y1, name='Первая'), 1, 1)
        fig.frames = frames1
        fig.add_trace(go.Scatter(x=x1, y=(y2), name='Вторая'), 1, 2)
        fig.update_layout(hovermode="x", updatemenus=[
            dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])], )
        context['graph'] = fig.to_html()
        return context

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'diffinform/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
