from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import ProductForm
from .models import Product
from .models import Classification

def new_product(request):
    template = loader.get_template('productApp/products/add_product.html')
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            obj, created = Product.objects.get_or_create(cor = request.POST.get('cor'),
                                                         tipo=request.POST.get('tipo'),
                                                         codigo_gtin=request.POST.get('codigo_gtin'))
            obj.save()
            return HttpResponseRedirect('/productApp/products')
        else:
            error = "<h2> Form invalid. Please, try again!</h2>"
            return HttpResponse(error)
    else:
        form = ProductForm()

    return HttpResponse(template.render({'form': form}, request))

def products(request):
    template = loader.get_template('productApp/products/products.html')
    products = Product.objects.all()
    classifications = Classification.objects.all()

    context = {'products_list': products, 'classification_list': classifications}
    return HttpResponse(template.render(context, request))

def get_product(request, id):
    template = loader.get_template('productApp/products/get_product.html')
    product = get_object_or_404(Product, pk=id)

    classifications = Classification.objects.filter(product = id)

    context = {'product': product, 'classification_list': classifications}
    return HttpResponse(template.render(context, request))
