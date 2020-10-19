from django.template import loader
from django.http import HttpResponse

from .service.engine import *
from .models import Product
from .models import Rule
from .models import Classification


# Create your views here.
def index(request):
	template = loader.get_template('productApp/index.html')
	return HttpResponse(template.render(None, request))

def process(request):

	engine = Engine()
	engine.processProducts()
	classifications = Classification.objects.all()
	context = {'classification_list': classifications}

	template = loader.get_template('productApp/process.html')
	return HttpResponse(template.render(context, request))

def products_new(request):

	template = loader.get_template('productApp/products/add_product.html')
	return HttpResponse(template.render(None, request))

def products(request):
	template = loader.get_template('productApp/products/products.html')
	products = Product.objects.all()
	classifications = Classification.objects.all()

	context = {'products_list': products, 'classification_list':classifications}
	return HttpResponse(template.render(context, request))

