from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from ..forms import *
from ..models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def create_order(request):
	form = OrderForm()
	if request.method == "POST":
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Created a new order.")
		else:
			messages.error(request, "Order can't be created.")

	return redirect("index")

@login_required(login_url="login")
def update_order(request):
	orders = Order.objects.filter(product__seller_id=request.user.id, status="Pending")
	if request.method == "POST":
		order = Order.objects.get(id=request.POST["id"])
		order.status = request.POST["status"]
		order.save()
		messages.success(request, "Order has been updated")
		return redirect("update-order")
	
	context = {
		"orders": orders,
	}
	return render(request, "orders/update-order.html", context)

@login_required(login_url="login")
def delete_order(request, id):
	order = Order.objects.get(id=id)
	redirect = request.GET["redirect"]
	if order.delete():
		messages.success(request, "Order has been deleted.")
		return HttpResponseRedirect(redirect)
	else:
		messages.error(request, "Order can't be deleted.")
		return HttpResponseRedirect(redirect)

	return redirect("orders")