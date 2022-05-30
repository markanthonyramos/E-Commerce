from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms import *
from ..models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def create_product(request):
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Created a new product.")
			return redirect("products")
		else:
			messages.error(request, "Product can't be created.")
			return redirect("create-product")

	return render(request, "products/create-product.html")

@login_required(login_url="login")
def update_product(request, id):
	product = Product.objects.get(id=id)
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			form.save()
			messages.success(request, "Updated a product.")
			return redirect("products")
		else:
			messages.error(request, "Product can't be updated.")
			return redirect(reverse("update-product", kwargs={"id": id}))

	context = {
		"product": product,
	}
	return render(request, "products/update-product.html", context)

@login_required(login_url="login")
def delete_product(request, id):
	product = Product.objects.get(id=id)
	if product.delete():
		messages.success(request, "Product has been deleted.")
	else:
		messages.error(request, "Product can't be deleted.")

	return redirect("products")