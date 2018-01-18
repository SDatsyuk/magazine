from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from products.models import ProductImage, Product
#magazine views
def index(request):
	product_images = ProductImage.objects.filter(is_active=True, is_main=True)
	if request.user.is_authenticated:
		username = request.user.username

	return render(request, 'magazine/home.html', locals())

def slider(request):
	images = ProductImage.objects.filter(product=1).order_by('is_main')
	main = ProductImage.objects.get(product=1, is_main=True)

	return render(request, 'slider.html', locals())
