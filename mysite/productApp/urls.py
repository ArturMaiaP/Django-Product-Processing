from django.urls import path

from . import processViews
from . import productsView
from . import rulesView

urlpatterns = [
    path('index', processViews.index, name='index'),
    path('', processViews.index, name='index'),
    path('process', processViews.process, name='process'),
    path('products/new', productsView.products_new, name='products_new'),
    path('products', productsView.products, name='products'),
    path('rules/new', rulesView.rules_new, name='rules_new'),
    path('rules', rulesView.rules, name='rules'),
]