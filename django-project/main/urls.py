#1. Add an import:  from my_app import views
#2. Add a URL to urlpatterns:  path('', views.home, name='home')

from django.urls import path
from main.views import * 

urlpatterns = [
    path('', index, name = 'index'),
    
]