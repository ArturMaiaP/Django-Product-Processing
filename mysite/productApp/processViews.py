from django.template import loader
from django.http import HttpResponse

from .service.engine import *
from .models import Classification
from .models import Rule


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


