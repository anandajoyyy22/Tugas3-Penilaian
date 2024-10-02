# Tugas3-Penilaian
# Nama: Ananda Joy Pratiwi Pasha Patoding
# NPM: 2206811190
# Kelas: PBP E

# Tugas 3: Implementasi Form dan Data Delivery pada Django #
1. Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Platform?
==> Data delivery penting untuk memastikan informasi bisa dikirim dan diterima antara sistem atau komponen dengan cara yang konsisten dan terstruktur.

2. Mana yang Lebih Baik antara XML dan JSON? Mengapa JSON Lebih Populer?
==> JSON umumnya lebih baik karena lebih ringkas, mudah dibaca dan ditulis manusia, serta lebih cepat diproses. JSON lebih populer dibandingkan XML karena kelebihan tersebut.

==> <Mengapa JSON Lebih Populer Dibandingkan XML:>

- Simplicity: JSON lebih sederhana dan lebih mudah dibaca oleh manusia serta lebih ringkas dibandingkan XML.
- Less Overhead: JSON memiliki overhead yang lebih rendah karena tidak memerlukan tag pembuka dan penutup yang panjang seperti XML.
Performance: JSON lebih cepat dalam pemrosesan dan parsing, terutama dalam konteks web dan aplikasi JavaScript.
- Support: JSON secara native didukung oleh JavaScript, menjadikannya pilihan populer dalam pengembangan web.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
==> is_valid() memastikan data yang dimasukkan ke dalam form memenuhi kriteria validasi sebelum diproses atau disimpan. Ini penting untuk menjaga integritas data.

==> <Fungsi ini melakukan beberapa hal:>
- Validasi Field: Memeriksa setiap field dalam form untuk memastikan data yang dimasukkan sesuai dengan aturan validasi yang ditetapkan, seperti format email yang benar atau rentang nilai yang sesuai.
- Error Handling: Mengumpulkan dan menampilkan pesan kesalahan jika ada field yang tidak valid, memungkinkan pengguna untuk memperbaiki data yang dimasukkan.

==> <Mengapa Kita Membutuhkan is_valid():>
- Data Integrity: Memastikan bahwa data yang diterima dari pengguna sesuai dengan yang diharapkan sebelum diproses lebih lanjut atau disimpan ke database.
- User Feedback: Menyediakan umpan balik kepada pengguna tentang kesalahan dalam data yang mereka masukkan, sehingga mereka dapat memperbaikinya.

4. Mengapa Kita Membutuhkan csrf_token saat Membuat Form di Django?
==> csrf_token melindungi dari serangan Cross-Site Request Forgery (CSRF) dengan memverifikasi bahwa form yang dikirim berasal dari aplikasi atau sumber yang sah.

5. Apa yang Terjadi jika csrf_token Tidak Ada? Bagaimana Penyerang Memanfaatkannya?
==> Tanpa csrf_token, form rentan terhadap serangan CSRF. Penyerang bisa memanfaatkan ini untuk melakukan aksi yang tidak sah atas nama pengguna yang sah, seperti mengubah data atau melakukan transaksi tanpa izin.

6. Jelaskan Cara Mengimplementasikan Checklist Secara Step-by-Step

- <Membuat sebuah proyek Django baru.> Buat sebuah direktori baru yang akan dijadikan tempat membuat project django, selanjutnya masuk ke dalam Virtual Environtment ( via command promt ) dan mulai membuat project django. Dalam membuat project ini bisa dengan menginput "django-admin startproject <nama project>" di cmd. Setelau itu base directory dan project directory akan otomatis muncul di dalam direktori yang kita buat di awal. Setelah itu server django sudah bisa dijalankan dengan input "python manage.py runserver" di cmd.

- <Membuat aplikasi dengan nama main pada proyek tersebut.> dilakukan dengan cara menginput python manage.py startapp main di terminal.

- <Mengatur URL Routing>
Menambahkan URL patterns di file urls.py untuk setiap view yang ada di aplikasi Django Anda.
Contoh:
from django.urls import path


<urlpatterns = [
    path('', views.home, name='home'),
    path('add/', view.add_product, name='add_product'),
]>

- <Membuat model pada aplikasi main dengan nama product dan memiliki atribut wajib sebagai berikut.> untuk memuat model dengan atribut yang sudah ditentukan isi file models.py dengan : 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

- <Menambahkan Gambar Background dan Memeriksa Kesalahan:>

Memastikan URL gambar dalam file CSS valid. Lalu menguji tampilan halaman web di browser local host yang disediakan
 
- <Menggunakan csrf_token dalam Form:>

Tambahkan {% csrf_token %} dalam tag <form> di template HTML untuk melindungi form dari serangan CSRF.
Contoh:
<form method="post">
    {% csrf_token %}
    <!-- Form fields -->
    <button type="submit">Submit</button>
</form>

- <Menggunakan is_valid() dalam View:>
Dalam views.py, saya menggunakan is_valid() untuk memeriksa form dan memproses data yang valid.
Contoh:
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        <if form.is_valid():>
            <form.save()>
            return redirect('home')
    else:
        <form = ProductForm()
    return render(request, 'main/add_product.html', {'form': form})>

7. Hasil Pengujian URL di postman
- "C:\Users\Ananda Joy\Downloads\Screenshot POSTMAN Body.png"
- "C:\Users\Ananda Joy\Downloads\Screenshot POSTMAN Header.png"
<link:> - https://imgpost.co/image/ylxvK
      - https://imgpost.co/image/ylPEY 


## Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django #

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?

=> HttpResponseRedirect() adalah objek yang digunakan untuk mengarahkan pengguna ke URL tertentu. Fungsi ini mengharuskan user untuk memberikan URL secara eksplisit. Sementara itu, redirect() adalah fungsi helper yang menyederhanakan proses ini. Dengan redirect(), user bisa langsung menggunakan nama view atau URL dan secara otomatis akan menghasilkan objek HttpResponseRedirect() yang sesuai. Ini membuat redirect() lebih mudah digunakan dalam konteks Django.

2. Jelaskan cara kerja penghubungan model Product dengan User!

=> Penghubungan model Product dengan User dilakukan dengan menambahkan field ForeignKey pada model Product. Ini berarti setiap produk terkait dengan satu pengguna tertentu, memungkinkan setiap pengguna memiliki banyak produk yang terasosiasi dengannya. Ketika pengguna membuat produk baru, informasi pengguna yang sedang login disimpan dalam field user, sehingga setiap produk dapat diidentifikasi pemiliknya.

=> <contoh:  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products') >
=> <on_delete=models.CASCADE berarti bahwa jika pengguna dihapus, semua produk terkait dengan pengguna tersebut juga akan dihapus. Ini membantu menjaga integritas data dalam aplikasi.>

3. Apa perbedaan antara authentication dan authorization?

=> Authentication adalah proses verifikasi identitas pengguna (misalnya, saat user melakukan login). Di sisi lain, Authorization adalah proses penentuan hak akses user setelah mereka berhasil diotentikasi. Setelah user login, sistem menentukan apa yang boleh dan tidak boleh dilakukan pengguna tersebut berdasarkan hak akses yang diberikan. Dalam konteks Django, authentication menangani kredensial login, sedangkan authorization mengelola izin untuk mengakses resource tertentu.

4. Bagaimana Django mengingat pengguna yang telah login?

=> Django mengingat pengguna yang telah login dengan menggunakan session. Ketika pengguna berhasil login, Django menyimpan informasi pengguna dalam session dan mengaitkan session tersebut dengan cookie di browser user. Setiap kali pengguna melakukan permintaan ke server, session ID yang disimpan dalam cookie tersebut dikirimkan untuk mengidentifikasi pengguna dan memulihkan informasi state dari server.

5. Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

=> Cookies digunakan untuk menyimpan informasi tambahan, seperti preferensi pengguna, pengaturan tampilan, dan data login. Meskipun cookies sangat berguna, tidak semua cookies aman; beberapa cookies dapat disalahgunakan dalam serangan seperti XSS (Cross-Site Scripting) jika tidak diatur dengan benar. Oleh karena itu, penting untuk menggunakan cookie yang aman dan membatasi informasi sensitif yang disimpan di dalamnya. Penggunaan secure flag dan httpOnly flag pada cookies adalah cara untuk meningkatkan keamanan.

6. Berikut adalah rangkuman dari tutorial tentang membuat fungsi dan formulir registrasi serta autentikasi pengguna di Django:

### A. Membuat Fungsi dan Form Registrasi

1. **Pengantar**:
   - Tutorial ini melanjutkan dari tutorial sebelumnya, di mana kita membuat form untuk menambahkan mood entry. Sekarang, kita akan membuat halaman utama terbatas (restricted) dengan sistem login untuk pengguna.

2. **Persiapan**:
   - Aktifkan virtual environment di terminal.
   - Buka `views.py` di subdirektori `main` dan tambahkan import:
     ```python
     from django.contrib.auth.forms import UserCreationForm
     from django.contrib import messages
     ```

3. **Fungsi Registrasi**:
   - Tambahkan fungsi `register` dalam `views.py`:
     ```python
     def register(request):
         form = UserCreationForm()
         if request.method == "POST":
             form = UserCreationForm(request.POST)
             if form.is_valid():
                 form.save()
                 messages.success(request, 'Your account has been successfully created!')
                 return redirect('main:login')
         context = {'form': form}
         return render(request, 'register.html', context)
     ```

4. **Membuat Form Registrasi**:
   - Buat berkas `register.html` di `main/templates` dengan struktur HTML untuk formulir pendaftaran.

5. **Menambahkan URL untuk Registrasi**:
   - Di `urls.py`, import dan tambahkan path untuk fungsi registrasi:
     ```python
     from main.views import register
     urlpatterns = [
         ...
         path('register/', register, name='register'),
     ]
     ```

### B. Membuat Fungsi Login

1. **Import Fungsi Autentikasi**:
   - Tambahkan import ke `views.py`:
     ```python
     from django.contrib.auth.forms import AuthenticationForm
     from django.contrib.auth import authenticate, login
     ```

2. **Fungsi Login**:
   - Tambahkan fungsi `login_user`:
     ```python
     def login_user(request):
         if request.method == 'POST':
             form = AuthenticationForm(data=request.POST)
             if form.is_valid():
                 user = form.get_user()
                 login(request, user)
                 return redirect('main:show_main')
         else:
             form = AuthenticationForm(request)
         context = {'form': form}
         return render(request, 'login.html', context)
     ```

3. **Membuat Form Login**:
   - Buat berkas `login.html` di `main/templates` dengan struktur HTML untuk login.

4. **Menambahkan URL untuk Login**:
   - Di `urls.py`, import dan tambahkan path untuk fungsi login:
     ```python
     from main.views import login_user
     urlpatterns = [
         ...
         path('login/', login_user, name='login'),
     ]
     ```

### C. Membuat Fungsi Logout

1. **Import Logout**:
   - Tambahkan import ke `views.py`:
     ```python
     from django.contrib.auth import logout
     ```

2. **Fungsi Logout**:
   - Tambahkan fungsi `logout_user`:
     ```python
     def logout_user(request):
         logout(request)
         return redirect('main:login')
     ```

3. **Menambahkan Tombol Logout**:
   - Di `main.html`, tambahkan tombol logout setelah hyperlink untuk menambah mood entry.

4. **Menambahkan URL untuk Logout**:
   - Di `urls.py`, import dan tambahkan path untuk fungsi logout:
     ```python
     from main.views import logout_user
     urlpatterns = [
         ...
         path('logout/', logout_user, name='logout'),
     ]
     ```


### D. Merestriksi Akses Halaman Main
1. **Import Decorator**: Tambahkan import `login_required` dari `django.contrib.auth.decorators` di bagian atas `views.py`.
   
2. **Terapkan Restriksi**: Tambahkan decorator `@login_required(login_url='/login')` di atas fungsi `home` untuk memastikan hanya pengguna yang sudah login yang dapat mengakses halaman ini.

3. **Jalankan Proyek**: Setelah restriksi diterapkan, jalankan proyek Django menggunakan `python manage.py runserver`. Akses `http://localhost:8000/` untuk memastikan halaman yang muncul adalah halaman login, bukan daftar mood entry.

### E. Menggunakan Data Dari Cookies
1. **Logout**: Pastikan untuk logout dari aplikasi sebelum melanjutkan.

2. **Import Tambahan**: Tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` di bagian atas `views.py`.

3. **Menambahkan Cookie**: Dalam fungsi `login_user`, modifikasi blok `if form.is_valid()` untuk menambahkan cookie `last_login` yang menyimpan waktu terakhir login:
   ```python
   response.set_cookie('last_login', str(datetime.datetime.now()))
   ```

4. **Kirim Data Cookie**: Di dalam fungsi `home`, tambahkan informasi cookie `last_login` ke dalam konteks yang dikirim ke template:
   ```python
   'last_login': request.COOKIES['last_login']
   ```

5. **Hapus Cookie Saat Logout**: Modifikasi fungsi `logout_user` untuk menghapus cookie `last_login` saat pengguna logout:
   ```python
   response.delete_cookie('last_login')
   ```

6. **Tampilkan Data di Template**: Tambahkan potongan kode di `main.html` untuk menampilkan informasi `last_login` setelah tombol logout:
   ```html
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```

7. **Cek Data Cookie**: Setelah login, data `last_login` akan muncul di halaman utama. Untuk memeriksa cookie di browser, gunakan fitur inspect element. 

Berikut adalah ringkasan dari tutorial tentang cara menghubungkan model `MoodEntry` dengan pengguna dalam aplikasi Django:

### E. Menghubungkan Model MoodEntry dengan Class class ProductForm(forms.ModelForm): dengan User


2. **Impor Model User**: Buka `models.py` di subdirektori `main` dan tambahkan import untuk model `User`:
   ```python
   from django.contrib.auth.models import User
   ```

3. **Definisikan Relasi di Model**: Tambahkan relasi ke model `Product` dengan menambahkan field `user`:
   ```python
   class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
    
   ```

   *!*: Kode ini menghubungkan setiap `product` dengan satu pengguna.

4. **Modifikasi Fungsi `add_product`**: Ubah kode di fungsi `create_mood_entry` untuk mengaitkan mood entry dengan pengguna yang sedang login, menambahkan produk baru ke dalam database.
   ```python
   def add_product(request):
    if request.method == 'POST':  
        form = ProductForm(request.POST, request.FILES) 
        if form.is_valid():  
            product_entry = form.save(commit=False) 
            product_entry.user = request.user  
            product_entry.save() 
            return redirect('main:home')
        else:
            return render(request, 'main/add_product.html', {'form': form, 'errors': form.errors})
    else:
        form = ProductForm() 
    return render(request, 'main/add_product.html', {'form': form, })
   ```

5. **Update Fungsi `home`**: Sesuaikan nilai dari `mood_entries` dan konteks untuk menampilkanproducts yang sesuai dengan pengguna yang login:
   ```python
    @login_required(login_url='/login')
    def home(request):
    products = Product.objects.filter(user=request.user)
    print(products)
    context = {
        'products': products,
        'name': request.user.username,
        'app_name': 'Jopulee Gift',
        'Customer_name': 'Nama Customer',
        'Customer_class': 'Membership',
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, 'main/home.html', context)
   ```

6. **Migrasi Model**:
   - Simpan semua perubahan dan jalankan `python manage.py makemigrations`.
   - Ketika muncul error, pilih opsi untuk menetapkan nilai default untuk field `user`.
   - Lanjutkan dengan `python manage.py migrate` untuk menerapkan migrasi.

7. **Persiapan untuk Produksi**: Di `settings.py`, tambahkan import `os` dan ubah pengaturan `DEBUG`:
   ```python
   import os
   PRODUCTION = os.getenv("PRODUCTION", False)
   DEBUG = not PRODUCTION
   ```

8. **Jalankan Proyek**: Jalankan proyek Django dengan `python manage.py runserver` dan akses `http://localhost:8000/`. Buat akun baru dan login. Mood entry yang dibuat dengan akun sebelumnya tidak akan muncul, menunjukkan bahwa hubungan antara objek `Product` dan pengguna telah berhasil diterapkan.

Melakukan add-commit-push ke GitHub.


### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

### a. **Inline Styles**:
Gaya yang diterapkan langsung pada elemen HTML menggunakan atribut `style`. Gaya ini memiliki prioritas tertinggi di antara semua jenis gaya.

**Contoh dari file**: `register.html`

```html
<h2 id="register-header" class="text-pink" style="color: red;">
  Create your account
</h2>
```

Pada contoh ini, meskipun elemen ini menggunakan **class selector** `text-pink`, warna teks akan menjadi **merah** karena gaya inline (`color: red;`) memiliki prioritas tertinggi.

---

### b. **ID Selector**:
Selector **ID** digunakan untuk menargetkan elemen tertentu. Selector ini memiliki prioritas lebih tinggi dari **class selector** tetapi lebih rendah dari **inline styles**.

**Contoh dari file**: `home.html`

```html
<h2 id="special-heading">
  Welcome to our website!
</h2>
```

Jika di CSS terdapat aturan seperti berikut:

```css
#special-heading {
  color: green;
}
```

Maka teks pada elemen dengan `id="special-heading"` akan berwarna **hijau**, kecuali jika ada **inline styles** yang mendahului.

---

### c. **Class Selector**:
Selector **class** digunakan untuk mengatur beberapa elemen yang berbagi kelas yang sama. **Class selector** memiliki prioritas lebih rendah dari **ID selector** dan **inline styles**.

**Contoh dari file**: `add_product.html`

```html
<button class="btn-primary">
  Add Product
</button>
```

Jika di CSS ada aturan seperti berikut:

```css
.btn-primary {
  background-color: blue;
  color: white;
}
```

Maka tombol tersebut akan memiliki latar belakang berwarna **biru** dan teks berwarna **putih**

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web?Berikan contoh nama aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting dalam pengembangan aplikasi web karena:

- **Pengalaman Pengguna yang Konsisten**: Dengan responsive design, pengguna mendapatkan pengalaman yang baik di berbagai perangkat, baik desktop, tablet, maupun smartphone. Ini membantu mempertahankan pengguna dan meningkatkan kepuasan mereka.
  
- **SEO yang Lebih Baik**: Mesin pencari, seperti Google, lebih menyukai situs yang responsif, sehingga dapat meningkatkan peringkat SEO dan visibilitas di hasil pencarian.

- **Efisiensi dalam Pengembangan**: Menggunakan satu desain yang responsif mengurangi kebutuhan untuk membuat dan memelihara beberapa versi situs untuk berbagai perangkat, sehingga menghemat waktu dan biaya.

- **Aksesibilitas**: Responsif memastikan bahwa konten dapat diakses oleh semua pengguna, termasuk mereka yang menggunakan perangkat dengan ukuran layar yang lebih kecil.

### Contoh Aplikasi

**Aplikasi yang Sudah Menerapkan Responsive Design**:
- **Instagram**: Platform media sosial ini memiliki desain responsif yang memungkinkan pengguna mengakses konten dengan nyaman di perangkat apa pun.
- **Netflix**: Aplikasi streaming ini secara otomatis menyesuaikan tampilannya untuk memberikan pengalaman yang baik di berbagai ukuran layar.

**Aplikasi yang Belum Menerapkan Responsive Design**:
- **Adobe Flash Player**: Banyak aplikasi dan situs yang bergantung pada Flash tidak responsif dan tidak bekerja dengan baik di perangkat mobile.
- **Shopzilla**: Versi lama dari platform belanja ini tidak dioptimalkan untuk tampilan mobile, menyulitkan pengguna untuk menjelajahi produk di perangkat kecil. Bahkan untuk versi barunya juga kurang terlalu responsive

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

### a. Padding
Padding digunakan untuk memberi ruang di dalam elemen, antara konten dan batas elemen tersebut.
**contoh:**
- **Tombol "Add Product" pada `home.html`**:
   ```html
   <button class="bg-pink-600 text-white py-2 px-4 rounded mt-4">Add to Cart</button>
   ```
   - `py-2` memberikan padding vertikal (atas dan bawah) sebesar 0.5rem.
   - `px-4` memberikan padding horizontal (kiri dan kanan) sebesar 1rem.

- **Form untuk menambahkan produk baru pada `add_product.html`**:
   ```html
   <div class="container bg-white bg-opacity-60 rounded-lg shadow-md p-6">
   ```
   - `p-6` memberikan padding sebesar 1.5rem di semua sisi kontainer.

### b.Margin
Margin digunakan untuk memberi ruang di luar elemen, antara elemen yang satu dengan yang lainnya.
**contoh:**
- **Judul pada `home.html`**:
   ```html
   <h2 class="text-xl font-bold mb-4">Featured Products</h2>
   ```
   - `mb-4` memberikan margin bawah sebesar 1rem.

- **Tombol "Edit Product Entry" pada `edit_product.html`**:
   ```html
   <div class="flex justify-center mt-6">
   ```
   - `mt-6` memberikan margin atas sebesar 1.5rem.

### c. Border
Border digunakan untuk membuat garis di sekitar elemen.
**contoh:**
- **Pemberitahuan kesalahan pada `register.html`**:
   ```html
   <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
   ```
   - `border border-red-400` membuat border dengan warna merah yang memiliki ketebalan standar.

- **Kontainer pada `edit_product.html`**:
   ```html
   <div class="bg-white rounded-lg p-6 form-style">
   ```
   - `rounded-lg` membuat sudut kontainer menjadi bulat, memberikan efek border yang halus.

### Intinya!!
- **Padding**: Menambah ruang di dalam elemen.
- **Margin**: Menambah ruang di luar elemen.
- **Border**: Membuat garis di sekitar elemen.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan Grid Layout adalah dua sistem tata letak CSS yang memungkinkan pengembang web untuk membuat tata letak responsif dan fleksibel dengan lebih mudah. 

### a. Flexbox (Flexible Box Layout)
- **Konsep:** Model tata letak satu dimensi yang mengatur elemen dalam satu arah (horizontal atau vertikal).
- **Kegunaan:**
  - Memudahkan penyelarasan elemen.
  - Fleksibel dan responsif terhadap ukuran layar.
  - Mengatur jarak antar elemen dengan mudah.
  - Memungkinkan pengaturan ulang urutan elemen tanpa mengubah HTML.

### b. Grid Layout
- **Konsep:** Model tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom.
- **Kegunaan:**
  - Membuat tata letak yang kompleks dan terorganisir.
  - Memungkinkan penempatan elemen di area tertentu.
  - Fleksibel dan responsif dengan penggunaan unit `fr`.
  - Memisahkan konten dengan jelas dalam baris dan kolom.

**Kesimpulan:** Gunakan **Flexbox** untuk tata letak satu dimensi dan **Grid Layout** untuk tata letak dua dimensi yang lebih kompleks. Keduanya membantu menciptakan desain responsif.


Berikut adalah langkah-langkah yang telah dilakukan untuk menambahkan Tailwind CSS dan Bootstrap ke dalam aplikasi Django, serta melakukan beberapa modifikasi pada aplikasi tersebut. 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

### 1. Menambahkan Tailwind CSS ke Aplikasi

1. **Buka project Django** (`tugas3-penilaian`) dan buka file `base.html` yang berada di dalam folder `templates`.
   
2. **Tambahkan tag `<meta>`** agar halaman web dapat menyesuaikan ukuran dan perilaku perangkat mobile (apabila belum ada):
   ```html
   <head>
       {% block meta %}
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1">
       {% endblock meta %}
   </head>
   ```

3. **Sambungkan Tailwind CSS** dengan menambahkan script CDN di bagian `<head>`:
   ```html
   <head>
       {% block meta %}
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1">
       {% endblock meta %}
       <script src="https://cdn.tailwindcss.com"></script>
   </head>
   ```

### 2. Menambahkan Bootstrap ke Aplikasi (Opsional)

Jika menggunakan Bootstrap, lakukan langkah-langkah berikut:

1. **Tambahkan Bootstrap CSS** di dalam `base.html`:
   ```html
   <head>
       {% block meta %}
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1">
       {% endblock meta %}
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
   </head>
   ```

2. **Tambahkan JavaScript Bootstrap**:
   ```html
   <head>
       ...
       <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
   </head>
   ```

3. **Tambahkan Popper.js dan Bootstrap JS** untuk dropdowns dan tooltips:
   ```html
   <head>
       ...
       <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
   </head>
   ```

### 3. Menambahkan Fitur Edit dan Delete Produk

1. **Modifikasi fungsi `login_user`** untuk menangani autentikasi pengguna:
   ```python
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
   ```

2. **Modifikasi fungsi `logout_user`**:
   ```python
   def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       messages.success(request, "Anda telah berhasil logout.")
       response.delete_cookie('last_login')
       return response
   ```

3. **Implementasi fungsi `edit_product`**:
   ```python
   def edit_product(request, id):
       product = Product.objects.get(pk=id)
       form = ProductForm(request.POST or None, instance=product)

       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:home'))

       context = {'form': form}
       return render(request, "main/edit_product.html", context)
   ```

4. **Implementasi fungsi `delete_product`**:
   ```python
   def delete_product(request, id):
       product = Product.objects.get(pk=id)
       product.delete()
       return HttpResponseRedirect(reverse('main:home'))
   ```

### 4. Menambahkan Navigation Bar

- Buat file `navbar.html` yang diambil dari kode tutorial sebelumnya untuk menyertakan navigasi dalam aplikasi.

### 5. Konfigurasi Static Files di `settings.py`

1. **Tambahkan middleware `WhiteNoise`**:
   ```python
   MIDDLEWARE = [
       'django.middleware.security.SecurityMiddleware',
       'whitenoise.middleware.WhiteNoiseMiddleware',  # Tambahkan tepat di bawah SecurityMiddleware
       ...
   ]
   ```

2. **Konfigurasi `STATIC_URL`, `STATICFILES_DIRS`, dan `STATIC_ROOT`**:
   ```python
   STATIC_URL = '/static/'
   if DEBUG:
       STATICFILES_DIRS = [
           BASE_DIR / 'static'  # merujuk ke /static root project pada mode development
       ]
   else:
       STATIC_ROOT = BASE_DIR / 'static'  # merujuk ke /static root project pada mode production
   ```

### 6. Menghubungkan `global.css` dan Script Tailwind ke `base.html`

1. **Modifikasi `base.html`** untuk menambahkan `global.css`:
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       {% block meta %} {% endblock meta %}
       <script src="https://cdn.tailwindcss.com"></script>
       <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
     </head>
     <body>
       {% block content %} {% endblock content %}
     </body>
   </html>
   ```

### 7. Menambahkan Custom Styling ke `global.css`

1. **Modifikasi file `global.css`** pada `static/css/global.css`:
   ```css
   .form-style form input, form textarea, form select {
       width: 100%;
       padding: 0.5rem;
       border: 2px solid #bcbcbc;
       border-radius: 0.375rem;
   }
   .form-style form input:focus, form textarea:focus, form select:focus {
       outline: none;
       border-color: #674ea7;
       box-shadow: 0 0 0 3px #674ea7;
   }
   @keyframes shine {
       0% { background-position: -200% 0; }
       100% { background-position: 200% 0; }
   }
   .animate-shine {
       background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
       background-size: 200% 100%;
       animation: shine 3s infinite;
   }
   ```

### 8. Styling Halaman

1. **Styling untuk halaman Login, Register, Home, dan Edit Product** juga dilakukan dengan extend dari `base.html` dan include `navbar.html`.

### Melakukan add-commit-push ke GitHub.