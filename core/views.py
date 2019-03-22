from django.shortcuts import render
from .models import Category, Product
# Create your views here.

def index(request):
    # this is my view (list view)
	products = Product.objects.all()
	return render(request, 'index.html', context={'products': products}) #visit home page call index view and render tempalte index

def product_detail_view(request, product_id):
	# this is where we get the product, will need to address the url
	# slugs helpful
	product = Product.objects.get(id=product_id)
	return render(request,'product_detail.html', context={'product': product}) 

# view connect to url and have model connnect templae