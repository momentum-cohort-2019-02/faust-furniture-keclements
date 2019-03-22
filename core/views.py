from django.shortcuts import render
from models import Category, Product
# Create your views here.
def index(request):
    # this is my view
	products = Product.objects.all()
	return render(request, 'index.html', context) #visit home page call index view and render tempalte index

def category_detail_view(request):
    category =  Category.objects.get(title='table')
    products = Product.objects.filter(category=category)