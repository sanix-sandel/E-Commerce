from django.shortcuts import render
from .models import Product
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView
)
from django.urls import reverse_lazy
# Create your views here.

class ProductListView(ListView):
    model=Product
    context_object_name='products'
    template_name='products/list.html'


class ProductDetailView(DetailView):
    model=Product
    context_object_name='product'
    template_name='products/detail.html'



class ProductDeleteView(DeleteView):
    model=Product
    success_url=reverse_lazy('product_list')
    template_name='products/delete.html'



class ProductUpdateView(UpdateView):
    model=Product
    fields=['title', 'description', 'price']
    success_url=reverse_lazy('product_list')
    template_name='products/update.html'
