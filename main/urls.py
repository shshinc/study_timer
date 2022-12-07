from django.urls import path
from .views import *
import main.views

urlpatterns = [
    path('', index, name='index'),
    path('', main.views.post, name='post'),
]

