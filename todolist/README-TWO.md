# Tugas 6 PBP 22/23

## Perbedaan antara asynchronous programming dengan synchronous programming

Dalam Synchronous programming, program dieksekusi secara sekuensial sehingga menimbulkan antrian yang berarti bahwa langkah selanjutnya tidak akan dijalankan selama langkah yang sebelumnya belum selesai dijalankan. Sementara dalam Asynchronous programming, program dapat dieksekusi secara bersamaan sehingga tidak perlu menunggu program sebelumnya selesai dijalankan.

## Paradigma Event-Driven Programming

Paradigma ini akan mengatur jalannya suatu program berdasarkan adanya event/peristiwa yang dapat dipicu oleh berbagai hal, seperti tindakan dari pengguna, pesan yang muncul dari program lain, atau adanya sensor output. Dengan cara ini, sistem akan saling berinteraksi satu sama lain untuk dapat menjalankan program. Contohnya penerapannya dalam tugas ini adalah event click yang ada dalam button sehingga suatu perintah dapat dijalankan hanya ketika pengguna menekan button yang sudah ditentukan.

## Penerapan Asynchronous programming pada AJAX

AJAX akan melakukan request ke server yang memungkinkan halaman web untuk terupdate secara asynchronous. Dengan demikian, browser tidak perlu memuat ulang halaman web secara keseluruhan karena AJAX hanya akan mengirimkan perubahan informasi yang ada ke server dan pengguna tetap dapat mengakses website selama proses tersebut berjalan.

## Implementasi Checkpoint

Untuk proses pembuatan AJAX GET, saya terlebih dahulu membuat views yang mengembalikan data dalam bentuk JSON dan menambahkan path untuk nantinya digunakan sebagai endpoint fetching. Kemudian, fetch dilakukan dengan metode native javascript yang akan mengambil data task dalam bentuk JSON dan mengembalikannya sesuai layout HTML yang sudah dibuat.

Untuk proses AJAX POST, pertama-tama membuat modal yang akan digunakan sebagai form untuk menambahkan task baru. Saya menggunakan JQuery untuk mengeksekusi event handler form dan mengirimkan data dari form melalui request AJAX. Setelah itu dibuat views yang akan menghandle data form tersebut untuk ditambahkan ke database. Terakhir adalah menambahkan path yang mengarah ke view tersebut.