from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductsView.as_view(), name="products"),
    path("create_order", CreateOrderView.as_view(), name="create_order"),
    path("products", ProductFilterView.as_view(), name="tags_filter")
]
