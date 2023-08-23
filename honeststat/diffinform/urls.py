from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path('', cache_page(60)(ArticlesHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', ArticlesCategory.as_view(), name='category'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
    # path('graph/', show_graph, name='graph'),
    path('graph/', Graph.as_view(), name='graph'),
]