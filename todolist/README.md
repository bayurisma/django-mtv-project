# Tugas 5 PBP 22/23

## Perbedaan dari Inline, Internal, dan External CSS serta kelebihan dan kekurangan dari masing-masing style

Inline CSS adalah cara meletakkan kode CSS di dalam masing-masing tag HTML yang ada. Kekurangannya adalah kita harus memberikan style pada setiap elemen HTML sehingga menjadi kurang efisien untuk diterapkan. Namun, Inline CSS berguna jika kita hanya ingin mengubah style sebuah tag HTML yang spesifik.
Pada internal CSS, kode CSS akan diletakkan di bagian head dari sebuah file HTML, biasanya menggunakan tag < style >. Cara ini tidak efisien jika CSS yang sama digunakan untuk beberapa file dan juga dapat meningkatkan waktu akses ke website. Internal CSS dapat berguna jika dilakukan untuk styling pada sebuah halaman saja.
External CSS membutuhkan sebuah file CSS eksternal yang berisi style website secara keseluruhan. File ini akan selalu dipanggil setiap website akan ditampilkan. Kekurangannya adalah waktu akses yang meningkat dan kemungkinan website tidak tampil secara sempurna sebelum file CSS dapat dipanggil. Kelebihannya adalah menjadikan file HTML lebih terstruktur dan rapi serta cocok digunakan untuk website dengan banyak halaman.

## Jelaskan tag HTML5 yang kamu ketahui.

`<a>` untuk menyisipkan sebuah hyperlink
`<form>` untuk membuat form HTML
`<img>` untuk memasukkan gambar
`<label>` untuk memberikan label pada input user
`<table>` untuk membuat sebuah tabel data
`<script>` untuk menyisipkan skrip kode ke file HTML

## Jelaskan tipe-tipe CSS selector yang kamu ketahui

.class : memilih elemen berdasarkan jenis class
#id : memilih elemen berdasarkan nilai id
element : memilih berdasarkan jenis elemen tertentu
:active : memilih elemen link yang aktif
:hover : memilih elemen link yang disorot oleh kursor

## Implementasi Checkpoint

Karena saya akan menggunakan Bootstrap maka yang pertama dilakukan adalah melakukan inisialisasi Bootstrap ke dalam file HTML. Kemudian saya menambahkan elemen table, card, dan button dari Bootstrap untuk setiap halaman yang sesuai. Metode styling yang saya pakai adalah internal dan inline CSS karena ini hanyalah website kecil yang tidak memiliki banyak halaman sehingga tidak memerlukan file CSS eksternal.
