from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import ProductForm
from .models import Product
from .models import Classification

def products_new(request):
    template = loader.get_template('productApp/products/add_product.html')
    if request.method =='POST':
        form = ProductForm(request.POST)
        print("EntrouAqui")
        if form.is_valid():
            print("FormVAlido")
            obj, created = Product.objects.get_or_create(cor = request.POST.get('cor'),
                                                         tipo=request.POST.get('tipo'),
                                                         codigo_gtin=request.POST.get('codigo_gtin'))
            obj.save()
            return HttpResponseRedirect('/productApp/products')
    else:
        form = ProductForm()

    return HttpResponse(template.render({'form': form}, request))

def products(request):
    template = loader.get_template('productApp/products/products.html')
    products = Product.objects.all()
    classifications = Classification.objects.all()

    context = {'products_list': products, 'classification_list': classifications}
    return HttpResponse(template.render(context, request))