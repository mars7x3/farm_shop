from django.urls import path

from product.views import *


urlpatterns = [
    path('', ContentView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),


]