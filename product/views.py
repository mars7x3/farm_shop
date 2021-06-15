
from django.views.generic import *

from .forms import CreateProductForm
from .models import *




class ProductListView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ContentView(ListView):
    model = Content
    template_name = 'product/home.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'product/products.html'
    context_object_name = 'categories'


class ContactView(ListView):
    model = Content
    template_name = 'product/contact.html'


class OrderView(CreateView):
    model = Order
    template_name = 'product/contact.html'
    form_class = CreateProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_form'] = self.get_form(self.get_form_class())
        return context


