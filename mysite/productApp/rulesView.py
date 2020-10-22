from django.template import loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import RuleForm
from .models import Rule
from .models import Product
from .models import Classification

def rules(request):
    template = loader.get_template('productApp/rules/rules.html')
    rules = Rule.objects.all()
    context = {'rules_list': rules}
    return HttpResponse(template.render(context, request))

def new_rule(request):
    template = loader.get_template('productApp/rules/add_rule.html')

    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            obj, created = Rule.objects.get_or_create(field = request.POST.get('field'),
                                                      value = request.POST.get('value'))
            obj.save()

            # If a new rule is added, the products should be reprocessed
            if created:
                Product.objects.all().update(processado = False)
                Classification.objects.all().delete()

            return HttpResponseRedirect('/productApp/rules')
        else:
            error = "<h2> Form invalid. Please, try again!</h2>"
            return HttpResponse(error)

    else:
        form = RuleForm()

    return HttpResponse(template.render({'form': form}, request))

def edit_rule(request, id):
    template = loader.get_template('productApp/rules/edit_rule.html')
    rule = get_object_or_404(Rule, pk=id)
    context = {'rule': rule}

    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            rule.field =  request.POST.get('field')
            rule.value =  request.POST.get('value')
            rule.save()

            #If a rule is changed, the products should be reprocessed
            Product.objects.all().update(processado=False)
            Classification.objects.all().delete()

            return HttpResponseRedirect('/productApp/rules')
        else:
            error = "<h2> Form invalid. Please, try again!</h2>"
            return HttpResponse(error)

    return HttpResponse(template.render(context, request))
