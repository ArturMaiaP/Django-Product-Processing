from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('products/new', views.products_new, name='products_new'),
    path('products', views.products, name='products'),
    path('process', views.process, name= 'process')
]