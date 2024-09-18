from django.urls import path
from . import views
from .views import main_view  # Import view main_view

urlpatterns = [
    # Routing untuk halaman utama
    path('', views.home, name='home'),
    #path('', main_view, name='main'),  # Menyambungkan URL root dengan view utama
    # Routing untuk halaman tambah produk
    path('add/', views.add_product, name='add_product'),
     # Routing untuk halaman daftar produk
    path('product-list/', views.product_list, name='product_list'),
    path('', main_view, name='main_view'),
    path('products/json/', views.product_json, name='products_json'),
    path('products/xml/', views.product_xml, name='products_xml'),
    path('products/<int:pk>/json/', views.product_json_by_id, name='product_json_by_id'),
    path('products/<int:pk>/xml/', views.product_xml_by_id, name='product_xml_by_id'),
]
