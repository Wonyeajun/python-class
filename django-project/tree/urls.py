from django.urls import path
from . import views

app_name = 'tree'

urlpatterns = [
    path('', views.tree_view, name='tree_view_default'),
    path('<int:page>/', views.tree_view, name='tree_view'),
    path('<int:tree_id>/fruit/create/', views.fruit_create, name='fruit_create'),
]