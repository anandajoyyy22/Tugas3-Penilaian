# Tugas3-Penilaian
# Nama: Ananda Joy Pratiwi Pasha Patoding
# NPM: 2206811190
# Kelas: PBP E

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