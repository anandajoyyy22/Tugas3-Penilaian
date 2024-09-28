from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
import xml.etree.ElementTree as ET
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from .forms import ProductForm
#

@login_required(login_url='/login')
def home(request):
    products = Product.objects.filter(user=request.user)
    print(products)
    context = {
        'npm': '2333445',
        'class' : 'PBP E',
        'products': products,
        'name': request.user.username,
        'app_name': 'Jopulee Gift',
        'Customer_name': 'Nama Customer',
        'Customer_class': 'Membership',
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'main/home.html', context)

# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)  # Jangan lupa tambahkan request.FILES untuk gambar
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')  # Arahkan ke daftar produk atau halaman lain setelah simpan
#     else:
#         form = ProductForm()

#     return render(request, 'main/create_product.html', {'form': form})

def add_product(request):
    if request.method == 'POST':  # Jika form dikirim dengan metode POST
        form = ProductForm(request.POST, request.FILES) # Menangani upload file (gambar produk)
        if form.is_valid():  # Memeriksa apakah data form valid
            product_entry = form.save(commit=False) 
            product_entry.user = request.user  # Mengaitkan produk dengan pengguna yang sedang login
            # form.save()
            product_entry.save() # Menyimpan produk ke database
            return redirect('main:home')
        else:
            # Jika ada error, tampilkan pesan error ke template
            return render(request, 'main/add_product.html', {'form': form, 'errors': form.errors})
    else:
        form = ProductForm() # Tampilkan form kosong untuk permintaan GET
    return render(request, 'main/add_product.html', {'form': form, })

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:home"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    #return redirect('main:login')
    response = HttpResponseRedirect(reverse('main:login'))
    messages.success(request, "Anda telah berhasil logout.")
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get mood entry berdasarkan id
    mood = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=mood)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:home'))

    context = {'form': form}
    return render(request, "main/edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    mood = Product.objects.get(pk = id)
    # Hapus mood
    mood.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:home'))
# def custom_logout(request):
#     logout(request)
#     messages.success(request, "Anda telah berhasil logout.")
#     return redirect('main:home')
