from django.urls import path
from .views import *

urlpatterns = [
    path('home/signup/', signup, name='signup'),
]