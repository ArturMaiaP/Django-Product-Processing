from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import RuleForm
from .models import Rule

def rules(request):
    template = loader.get_template('productApp/rules/rules.html')
    rules = Rule.objects.all()
    context = {'rules_list': rules}
    return HttpResponse(template.render(context, request))

def rules_new(request):
    template = loader.get_template('productApp/rules/add_rule.html')
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            obj, created = Rule.objects.get_or_create(field = request.POST.get('field'),
                                                      value = request.POST.get('value'))
            obj.save()
            return HttpResponseRedirect('/productApp/rules')

    else:
        form = RuleForm()

    return HttpResponse(template.render({'form': form}, request))
