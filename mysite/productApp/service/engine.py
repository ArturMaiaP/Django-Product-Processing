from ..models import Product
from ..models import Rule
from ..models import Classification

class Engine():

    def processProducts(self):
        rules = Rule.objects.all()
        products = Product.objects.all()

        for prod in products:
            if (not prod.processado):
                for rule in rules:

                    if (rule.field == "tipo"):
                        if (rule.value == prod.tipo):
                            classification = Classification(product=prod, rule=rule, result=True)
                            classification.add_classification()
                        else:
                            classification = classification = Classification(product=prod, rule=rule, result=False)
                            classification.add_classification()

                    if (rule.field == "cor"):
                        if (rule.value == prod.cor):
                            classification = Classification(product=prod, rule=rule, result=True)
                            classification.add_classification()
                        else:
                            classification = classification = Classification(product=prod, rule=rule, result=False)
                            classification.add_classification()

                    if (rule.field == "codigo_gtin"):
                        if (rule.value == prod.codigo_gtin):
                            classification = Classification(product=prod, rule=rule, result=True)
                            classification.add_classification()
                        else:
                            classification = classification = Classification(product=prod, rule=rule, result=False)
                            classification.add_classification()

                prod.processado = True
                prod.save()


