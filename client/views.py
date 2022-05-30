from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Sum, Count
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_user(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				user = User.objects.get(username=request.POST["username"])
				profile = Profile(user=user, first_name=request.POST["first_name"], last_name=request.POST["last_name"])
				profile.save()
				messages.success(request, "User has been created successfully.")
				return redirect("login")
			else:
				messages.error(request, "Passwords didn't match.")

		return render(request, "register.html")
	else:
		return redirect("index")

def login_user(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("index")
			else:
				messages.error(request, "Wrong username or password.")

		return render(request, "login.html")
	else:
		return redirect("index")

def logout_user(request):
	logout(request)
	return redirect("login")

@login_required(login_url="login")
def index(request):
	products = Product.objects.all()

	context = {
		"products": products
	}
	return render(request, "index.html", context)

@login_required(login_url="login")
def products(request):
	products = Product.objects.filter(seller_id=request.user.id)
	orders = Order.objects.filter(product__seller_id=request.user.id)
	pending_orders = orders.filter(status="Pending")
	sold_products = orders.filter(status="Delivered")

	context = {
		"products": products,
		"pending_orders": pending_orders,
		"sold_products": sold_products,
	}
	return render(request, "products.html", context)

@login_required(login_url="login")
def orders(request):
	orders = Order.objects.filter(buyer_id=request.user.id)

	context = {
		"orders": orders,
	}
	return render(request, "orders.html", context)

@login_required(login_url="login")
def sold_products(request):
	orders = Order.objects.filter(product__seller_id=request.user.id, status="Delivered")
	total_customers = orders.values("buyer").distinct().count
	profit = orders.aggregate(profit=Sum("product__price"))
	quantity = orders.values("product__id").distinct().annotate(count=Count("product__id"))

	context = {
		"orders": orders,
		"total_customers": total_customers,
		"profit": profit,
		"quantity": quantity,
	}
	return render(request, "sold-products.html", context)
