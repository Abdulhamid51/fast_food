from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path("products/", views.index_view, name="index"),
    path("add_cart/", views.add_cart, name="add_cart"),
    path("update_cart/", views.update_cart, name="update_cart"),
]
