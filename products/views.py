from django.shortcuts import render, get_object_or_404
from .models import ProductImage, PropertyValue, Product

def product_view(request, slug):
	product = get_object_or_404(Product, slug=slug)
	image = ProductImage.objects.get(product=product.id, is_main=True)
	# product_images = ProductImage.objects.filter(product_id=product.id)
	
	# main = ProductImage.objects.get(product=product.id, is_main=True)

	propertys = PropertyValue.objects.filter(product=product.id)

	if request.user.is_authenticated:
		username = request.user.username
	
	return render(request, 'products/product_page.html', locals())
