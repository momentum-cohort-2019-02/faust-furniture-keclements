from django.db import models

# Create your models here.

User = get_user_model()

class Product(models.Model):
	EXCELLENT = 'ED'

	PRODCUT_CONDITIONS = (
		(EXCELLENT, 'Excelent'),
		(VERY)
	)

	"""Contains information related to the Product for sale"""
	product_name = models.CharField(max_length=100, unique=True, help_text="Enter product name")
	product_description = models.CharField(max_length=250, blank=True, null=True)
	price = models.IntegerField(max_length=10, blank=True, null=True, help_text="Enter integer price")
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	condition = models
	# class Meta:
	# 	ordering =['-my_field_name'] 

	def __str__(self):
		return self.name


class ProductCategory(models.Model):
	""