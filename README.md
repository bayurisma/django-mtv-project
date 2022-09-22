# Tugas 3 PBP 22/23 Repository

Berikut adalah link hasil web yang telah di-deploy [Tugas 2 Web](https://watchlistku.herokuapp.com/mywatchlist/html/)

## Perbedaan JSON, XML, dan HTML

JSON adalah singkatan dari JavaScript Object Notation merupakan suatu format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Walaupun memiliki fungsi yang serupa dengan XML, akan tetapi JSON memiliki perbedaan di beberapa faktor seperti cara menyimpan elemennya, keamanan, dan cara penerapannya. Selain itu, JSON juga memiliki kelebihan yaitu dapat menyimpan data dalam bentuk array sehingga transfer data menjadi lebih mudah dan mendukung beberapa bahasa pemrograman lain. JSON juga memiliki kekurangan yaitu format penulisannya sulit untuk dipahami oleh manusia dan rentan terhadap serangan.

Di sisi lain, ada XML yang digunakan untuk menyimpan dan menyederhanakan pertukaran data sedangkan HTML digunakan untuk menampilkan data. XML dapat digunakan di berbagai sistem karena merupakan bahasa pemrograman yang independen. Akan tetapi XML juga memiliki kekurangan seperti tidak adanya penggunaan array. Sementara itu, HTML adalah bahasa markup yang digunakan untuk membuat halaman website. Isinya terdiri dari berbagai elemen, tag, dan atribute. XML juga menggunakan sistem tag, tetapi dapat dikustomisasi secara beragam dan tidak terkhusus seperti HTML.

## Pentingnya Data Delivery

Dalam membuat sebuah platform pastinya kita akan memiliki sekumpulan data yang baik itu akan disimpan atau dikirimkan kepada pengguna yang mengakses platform tersebut. Data-data tersebut dapat disajikan dalam berbagai format sesuai request yang dikirimkan. Oleh karena itu, peran data delivery disini sangat vital untuk menampilkan response yang sesuai kepada client. Karena tanpa adanya data delivery maka platform kita akan sulit untuk menampilkan data.

## Implementasi Checkpoint

Pertama-tama saya membuat app project baru bernama mywatchlist dan menambahkan path routingnya ke dalam urls.py. Kemudian saya membuat models untuk atribut-atribut data yang akan dimasukkan ke dalam watchlist item. Setelah itu, migrations dilakukan untuk mengimplementasi model tersebut ke dalam database. Saya menggunakan fitur djangoadmin untuk menambahkan 10 data item yang dibutuhkan. Data tersebut disimpan ke dalam objek MyWatchList yang sebelumnya sudah didefinisikan di models.py.

Beralih ke implementasi fitur penyajian data. Saya mendefinisikan 3 fungsi berbeda di dalam views.py untuk menampilkan data dalam format HTML, XML, dan JSON. Kemudian, fungsi-fungsi tersebut dipanggil dalam pathnya masing-masing di urls.py yang telah dibuat. Setelah memastikan seluruh URL dapat berjalan, deployment pun dilakukan ke Heroku untuk app mywatchlist.
