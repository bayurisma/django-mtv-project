# Tugas 4 PBP 22/23 Repository

Berikut adalah link hasil web yang telah di-deploy [ToDoList App](https://tugas-2-project.herokuapp.com/todolist/)

## Kegunaan {% csrf_token %} pada elemen form

Baris kode atau tag tersebut berguna untuk mencegah adanya serangan web berbahaya yang disebut CSRF (Cross Site Request Forgery). Tag tersebut akan menghasilkan suatu token yang terhubung dengan session user tertentu dan digunakan untuk memastikan request yang dikirimkan memang berasal dari user tersebut dan bukan dari pihak lain. Tanpa adanya baris kode tersebut, elemen form akan rentan untuk dijadikan celah penyerangan CSRF karena biasanya serangan tersebut memanfaatkan fitur form yang tersedia dalam sebuah web.

## Cara membuat elemen form secara manual

Form dapat dibuat secara manual dengan memanfaatkan tag <form> dari HTML. Tag ini memiliki elemen input yang berbeda-beda jenisnya seperti text fields, checkboxes, radio buttons, submit buttons, dsb. Ada juga beberapa atribut yang tersedia di dalamnya seperti action yang digunakan untuk mendefinisikan aksi yang akan dijalankan ketika form dikirim dan method untuk menentukan metode HTTP yang akan dipakai ketika data dikirimkan.

Untuk membuat form seperti yang ditampilkan oleh {{ form.as_table }} secara manual, kita dapat menambahkan table di dalam tag form. Kemudian, di dalam tabel tersebut ditambahkan element input yang sesuai dengan data yang akan dikirimkan.

## Proses alur data submisi

Data yang pertama diinput melalui form adalah data user. Data ini ditangani oleh module UserCreationForm untuk proses registrasi sedangkan untuk proses login data akan diautentikasi terlebih dahulu kemudian digunakan untuk mengatur cookie pada response. Data user ini akan tetap berada di dalam request guna memberikan identitas pada tiap task yang akan dibuat.

Selanjutnya adalah data untuk task yang akan diinput melalui form yang sudah dibuat menggunakan Model Form di models.py dan forms.py. Data tersebut akan ditambahkan dengan data user di request kemudian disimpan langsung ke dalam database. Nantinya kumpulan data task ini yang akan dikirimkan ke template HTML untuk ditampilkan ke pengguna.

## Implementasi Checkpoint

Yang pertama adalah membuat app todolist dan menambahkan path urlnya ke dalam urls.py. Kemudian menambahkan model untuk Task dengan atribut-atribut yang dibutuhkan. Untuk atribut user saya menggunakan model foreign key dengan parameter yang diimport dari model User, sedangkan atribute date saya buat agar otomatis diinput dengan tanggal saat pembuatan task tersebut.

Selanjutnya ada 3 form yang harus dibuat untuk masing-masing fungsi. Pertama adalah form untuk registrasi user, saya menggunakan module UserCreationForm dan membuat fungsi register untuk menampilkan form tersebut ke template HTML dengan bantuan generator as_table. Setelah itu, form login dibuat langsung di dalam template HTML dan datanya akan diautentikasi dengan fungsi login_user untuk kemudian digunakan menjadi cookie. Fungsi logout juga dibuat dengan module logout dan menghapus cookie yang ada. Terakhir adalah form untuk pembuatan task yang dibuat dengan Model Form dan hanya memasukkan 2 field di forms.py yaitu untuk title dan description.

Kemudian saya membuat halaman utama untuk menampilkan daftar todolist, tombol logout, dan tombol untuk menambah task baru. Setelah semua form selesai dibuat beserta template HTML-nya, routing untuk masing-masing fungsi ditambahkan ke dalam urls.py agar dapat diakses. Setelah itu, deployment dilakukan ke Heroku dan menambahkan dua akun dummy dengan tiga data yang dibutuhkan.
