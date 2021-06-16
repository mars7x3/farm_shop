from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from django.views import View
from .forms import OrderForm
from .models import *
from django.contrib import messages


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
    context_object_name = 'company'


class CategoryListView(ListView):
    model = Category
    template_name = 'product/products.html'
    context_object_name = 'categories'


class ContactView(ListView):
    model = Content
    template_name = 'product/contact.html'


class OrderCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Заявка отправлена')
            return HttpResponseRedirect(redirect_to=reverse_lazy('contacts'))
        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных')
        return HttpResponseRedirect(redirect_to=reverse_lazy('contacts'))