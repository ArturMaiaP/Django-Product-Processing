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
    path('products/new', productsView.new_product, name='new_products'),
    #Get all products and their respective classifications
    path('products', productsView.products, name='products'),
    # Get product by Id
    path('products/<int:id>',productsView.get_product, name='edit_products'),

    #Add new rule
    path('rules/new', rulesView.new_rule, name='new_rules'),
    #Get all rules
    path('rules', rulesView.rules, name='rules'),
    #Edit rule by Id
    path('rules/<int:id>', rulesView.edit_rule, name='edit_rules')
]

