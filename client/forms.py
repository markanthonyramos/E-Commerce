from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ["user", "first_name", "last_name"]

class ProductForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Product
		fields = ["name", "price", "description", "product_pic", "seller"]

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ["product", "buyer"]