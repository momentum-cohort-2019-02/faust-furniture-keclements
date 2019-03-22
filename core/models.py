from django.db import models

# Create your models here.

#User = get_user_model()

class Product(models.Model):
	# EXCELLENT = 'EX'
	# VERY_GOOD = 'VG'
	# GOOD = 'GD'
	# AVERAGE = 'AV'

	# PRODUCT_CONDITIONS = (
	# 	(EXCELLENT, 'Excelent'),
	# 	(VERY_GOOD, 'Very Good'),
	# 	(GOOD, 'Good'),
	# 	(AVERAGE, 'Average')
	# )

	# """Contains information related to the Product for sale"""
	# product_name = models.CharField(max_length=10, unique=True, help_text="Enter product name")
	# product_description = models.CharField(max_length=250, blank=True, null=True)
	# price = models.IntegerField(blank=True, null=True, help_text="Enter integer price")
	# category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
	# condition = models.CharField(max_length=2, choices=PRODUCT_CONDITIONS)
	# # product_dimention = models.

	# #def product_conditions(self)
	# 	#conditions = [] 

	# def __str__(self):
	# 	return self.product_name

class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('name', )
		verbose_name = 'category'
		verbose_name_plural = 'categories'

		def __str__(self):
			return.self.name



		

