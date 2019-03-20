from django.db import models

# Create your models here.
class Product(models.Model):

	# Fields
	product_name = models.CharField(max_length=60, help_text='Enter product field name')
	# product_price = models.IntegerField()
	# condition = 
	
	# Metadata
	class Meta:
		ordering =['-my_field_name'] 
		# will need to fix the ordering it may be diff for project


	__str__(self)
        return self.product_name



