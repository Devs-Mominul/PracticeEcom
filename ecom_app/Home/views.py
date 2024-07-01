from django.shortcuts import render
from store.models import Product, Category, ProductImage

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', locals())
def product_details(request, id):
  
    product_details = Product.objects.filter(id=id)
    photos = ProductImage.objects.filter(product=product_details)
    return render(request, 'store/product_details.html', context={
        'photos': photos,
    })
    
