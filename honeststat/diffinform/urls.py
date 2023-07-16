from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('cats/<slug:cat>/', categories),
]