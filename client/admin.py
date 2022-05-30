from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ["user", "first_name", "last_name", "created_at"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "price", "seller", "updated_at"]
	list_filter = ["name", "seller__username"]
	search_fields = ["name__startswith", "seller__username__startswith"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ["id", "product_name", "buyer", "updated_at"]
	list_filter = ["product__name", "buyer__username"]
	search_fields = ["product_name__startswith", "buyer__name__startswith"]

	def product_name(self, obj):
		return obj.product.name