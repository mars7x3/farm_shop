
from django.views.generic import *


from .models import *






class ProductListView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'products'


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     category = self.kwargs.get('slug')
    #     queryset = queryset.filter(category__slug=category)
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['category'] = self.kwargs.get('slug')
    #     return context




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

