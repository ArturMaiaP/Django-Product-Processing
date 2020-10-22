from django.urls import path

from . import processViews
from . import productsView
from . import rulesView
urlpatterns = [
    path('index', processViews.index, name='index'),
    path('', processViews.index, name='index'),

    #Process the products based on the registered rules
    path('process', processViews.process, name='process'),

    #Add new product
    path('products/new', productsView.new_product, name='products_new'),
    #Get all products and their respective classifications
    path('products', productsView.products, name='products'),

    #Add new rule
    path('rules/new', rulesView.new_rule, name='rules_new'),
    #Get all rules
    path('rules', rulesView.rules, name='rules'),
    #Edit rule by id
    path('rules/<int:id>', rulesView.edit_rule, name='rules_edit')
]

