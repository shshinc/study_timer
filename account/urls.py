from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]