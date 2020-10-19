from django.db import models

# Create your models here.

class Product(models.Model):
	cor = models.CharField(max_length=200)
	codigo_gtin = models.CharField(max_length=200)
	tipo = models.CharField(max_length=200)
	processado = models.BooleanField(default = False)

	def add_product(self):
		self.save()

	def __str__(self):
		return "Produto: "+ self.tipo+ ", " + self.cor + ", " + self.codigo_gtin

class Rule(models.Model):
	field = models.CharField(max_length=200)
	value = models.CharField(max_length=200)

	def add_rule(self):
		self.save()

	def __str__(self):
		return "Rule: " + self.field + " AND " + self.value

class Classification(models.Model):

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
	result = models.BooleanField(default=False)

	def add_classification(self,):
		self.save()

