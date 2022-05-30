from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.user.username}"

class Product(models.Model):
	name = models.CharField(max_length=30)
	price = models.FloatField()
	description = models.CharField(max_length=255)
	product_pic = models.ImageField()
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.name}"

class Order(models.Model):
	STATUS = [
		["Pending", "Pending"],
		["Delivered", "Delivered"],
	]
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, default="Pending", choices=STATUS)
	buyer = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.product.name}"