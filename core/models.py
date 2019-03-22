from autoslug import AutoSlugField

from django.db import models

# Create your models here.

#User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = AutoSlugField(
        unique=True,
        populate_from="name",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    EXCELLENT = 'EX'
    VERY_GOOD = 'VG'
    GOOD = 'GD'
    AVERAGE = 'AV'
    PRODUCT_CONDITIONS = (
     (EXCELLENT, 'Excellent'),
     (VERY_GOOD, 'Very Good'),
     (GOOD, 'Good'),
     (AVERAGE, 'Average')
    )
    condition = models.CharField(max_length=2, choices=PRODUCT_CONDITIONS)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, help_text="Enter product name")
    slug = AutoSlugField(unique=True, populate_from="name", blank=True, null=True,)
    description = models.TextField(max_length=300, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter integer price")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    available = models.BooleanField(default=True)
    #condition = models.CharField(max_length=2, choices=PRODUCT_CONDITIONS)
    # product_dimention = models.

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),
        )

    def __str__(self):
        return self.name

#     category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
