from django.urls import path
from .views import *
from .views_crud.products import *
from .views_crud.orders import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("register/", register_user, name="register"),
	path("login/", login_user, name="login"),
	path("logout/", logout_user, name="logout"),
	path("", index, name="index"),
	path("products/", products, name="products"),
	path("create-product/", create_product, name="create-product"),
	path("update-product/<int:id>/", update_product, name="update-product"),
	path("delete-product/<int:id>/", delete_product, name="delete-product"),
	path("orders/", orders, name="orders"),
	path("create-order/", create_order, name="create-order"),
	path("delete-order/<int:id>/", delete_order, name="delete-order"),
	path("update-order/", update_order, name="update-order"),
	path("sold-products/", sold_products, name="sold-products"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
