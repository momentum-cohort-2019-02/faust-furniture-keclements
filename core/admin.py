from django.contrib import admin

# Register your models here.
from core.models import Category, Product

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available',]
    list_filter = ['available', ]
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}

	# use prepopulated_fields attribute to specify fields were the value is automatically set using value of other fields