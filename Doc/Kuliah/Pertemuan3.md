
Representasi Ruang Keadaan ( State Space )

 

Ruang Keadaan merupakan cara mendefinisikan permasalahan ke dalam bentuk representasi algoritma

 

Cara untuk merepresentasikan ruang keadaan adalah :

 

A. Graph Keadaan

 

Graph terdiri dari node - node yang menunjukkan keadaan yaitu keadaan awal dan

keadaan baru yang akan dicapai dengan menggunakan operator. Node - node dalam graph keadaanya saling dihubungkan dengan menggunakan busur (arc) yang diberi panah untuk menunjukkan arah dari suatu keadaan ke adaan berikutnya.

 

Dalam prakteknya sangatlah sulit untuk menggambarkan graph keadaan. Pada gambar menunjukkan graph berarah dengan node M menunjukkan keadaan awal, dan node T adalah tujuan. Pada gambar tersebut kita dapat melihat ada 4 lintasan dari M ke T yaitu:

 

Kemudian ada juga lintasan yang tidak sampai ke tujuan/buntu yaitu:

 

 Gambar Graph Keadaan :




Bentuk seperti ini biasanya cukup sulit untuk direpresentasikan dalam suatu software, karena memungkinkan adanya silkus dalam graph tersebut. Misal tanpa mempertimbangkan arah akan didapat silkus :D-C-E-I-D. Node - node ini akan selalu berulang.

 

B. Pohon Pelacakan

 

Untuk menghindari kemungkinan adanya proses pelacakan node yang berulang maka digunakan struktur pohon. Sruktur pohon digunakan untuk menggambarkan keadaan secara hirarkis. Pohon terdiri atas node - node. Node yang terletak pada level 0 disebut “akar”. Node akar menunjukkan keadaan awal yang biasanya merupakan topic atau objek. Node akar memiliki beberapa percabangan yang terdiri atas beberapa node successor yanga disebut “anak” . Namun jika dilakukan pencarian mundur, maka dapat dikatakan node tersebut memiliki predessor.

 

Node yang tidak memilik anak disebut “daun” yang menunjukkan akhir dari suatu pencarian, dapat berupa tujuan yang diharapkan (goal) atau jalan buntu (dead end). Gambar dibawah menunjukkan graph dan terlihat tidak ada lagi siklus, karena setiap node tidak diperbolehkan memiliki cabang kembali ke node dengan level yang lebih rendah.

 

 

C. Pohon AND/OR

 
Pada ke dua cara yang telah disebutkan di atas, muncul masalah - masalah lain karena persoalan yang komplek sering tidak dapat diselesaikan secara langsung dalam ruang lingkup masalah. Persoalan tersebut bias diselesaikan dengan memecah menjadi beberapa sub - sub yang sederhana. Strategi ini disebut Dekomposisi, Dekomposisi ini digambarkan dengan grafik AND/OR.

 

Pada gambar dibawah terlihat ada masalah M yang hendak dicari solusinya dengan 3 kemungkinan yaitu A, B, dan C. Artinya masalah M bias diselesaikan jika salah satu dari subgoal A,B,C tidak terpecahkan. Pada gambar kedua masalah M hanya bisa diselesaikan dengan A AND B AND C, jadi subgoal A, B dan C harus dipecahkan terlebih dulu.

 

 

Gambar Node AND/OR 


Untuk memecahkan persoalan yang berhubungan dengan simpul AND, seluruh anakkan simpul AND, seluruh anakan simpul AND tersebut harus dipecahkan. Jika menggunakan simpul OR maka pemecahan persoalan yang berhubungan dengan simpul induk dari simpul OR , maka salah satu anakan harus dapt dipecahkan. Pada gambar 3.4 memperlihatkan tujuan pada graph dari gambar 3.2. Dengan menggunakan pohon AND/OR, tujuan yang dicapai pada pohon sampai level 6 dapat dipersingkat hanya sampai pada level 2 saja.

 

 Gambar Pohon AND/OR

 

Penutup

 

Kesimpulan

 

Dari pernyataan diatas dapat disimpulkan bahwa ruang keadaan merupakan Suatu ruang yang berisi semua keadaan yang mungkin dan memiliki graf keadaan, pohon keadaan dan pohon AND/OR untuk mempresentasikannya

 

Saran

 

Dari kesimpulan yang dibuat sebaiknya proses yang ada pada ruang keadaan dapat diimplementasikan untuk mencapai sebuah keadaan baru dengan menggunakan operator yang tersedia


    Nama : Muh Akbar Tamrin
    NPM : 1144012
    Kelas : D4 Teknik Informatika 3C
    Mata Kuliah : Kecerdasan Buatan
