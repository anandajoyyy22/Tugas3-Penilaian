from django.urls import path
from . import views
from .views import main_view  # Import view main_view#
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product

app_name = "main"
urlpatterns = [
    # Routing untuk halaman utama
    path('', views.home, name='home'),
    #path('', main_view, name='main'),  # Menyambungkan URL root dengan view utama
    # Routing untuk halaman tambah produk
    path('add_product/', views.add_product, name='add_product'),
     # Routing untuk halaman daftar produk
    path('product-list/', views.product_list, name='product_list'),
    path('', main_view, name='main_view'),
    path('products/json/', views.product_json, name='products_json'),
    path('products/xml/', views.product_xml, name='products_xml'),
    path('products/<int:pk>/json/', views.product_json_by_id, name='product_json_by_id'),
    path('products/<int:pk>/xml/', views.product_xml_by_id, name='product_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
]
