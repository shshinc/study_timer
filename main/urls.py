from django.urls import path
from .views import *
import main.views

urlpatterns = [
    path('', index, name='index'),
    path('after/', main.views.after),
    path('after/end/', main.views.image),
]

