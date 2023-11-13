from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .forms import *
from .models import *

# Create your views here.


class CreateOrderView(CreateView):
    template_name = "create_order.html"
    form_class = OrderForm
    queryset = Order.objects.all()
    success_url = "/"


class ProductFilterView(ListView):
    context_object_name = "products"
    template_name = "product_filter.html"

    def get_queryset(self):
        return Product.objects.filter(tag__name__icontains=self.request.GET.get("tag"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.request.GET.get("tag")
        return context


class TagsView():
    def get_queryset_tag(self):
        return Tag.objects.all()


class ProductsView(ListView, TagsView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'product_list'
