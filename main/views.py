from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
import json
import xml.etree.ElementTree as ET

def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'app_name': 'Jopulee Gift',
        'Customer_name': 'Nama Customer',
        'Customer_class': 'Membership',
    }
    return render(request, 'main/home.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'main/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})

def main_view(request):
    return HttpResponse("Hello, this is the main view.")
# def main_view(request):
#     products = Product.objects.all()  # Mengambil semua produk dari database
#     return render(request, 'main/main.html', {'products': products})

def product_json(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, request, content_type='application/json')

def product_xml(request):
    products = Product.objects.all()
    data = serializers.serialize('xml', products)
    return HttpResponse(data, request, content_type='application/xml')

def product_json_by_id(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)
    data = serializers.serialize('json', [product])
    return HttpResponse(data, request, content_type='application/json')

def product_xml_by_id(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found', status=404)
    product = Product.objects.get(id=id)
    data = serializers.serialize('xml', [product])
    return HttpResponse(data, request, content_type='application/xml')



