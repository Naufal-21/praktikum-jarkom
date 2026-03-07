# Laporan Praktikum Jarkom IF - Modul 2

## Tujuan Praktikum
1. Memahami antarmuka (interface) dan fitur-fitur dasar pada aplikasi Wireshark.
2. Mampu melakukan *capture* (tangkapan) paket data pada jaringan yang sedang aktif.
3. Mampu menggunakan fitur *filter* tampilan untuk mencari dan menganalisis protokol jaringan tertentu, khususnya HTTP.
4. Memahami konsep enkapsulasi data jaringan dengan menganalisis lapisan protokol (HTTP, TCP, IPv4, Ethernet II).

## Alat dan Bahan
* Laptop / PC
* Aplikasi Wireshark yang sudah terinstal
* Koneksi Jaringan (Wi-Fi atau LAN/Ethernet)
* Browser web (untuk menghasilkan *traffic* HTTP)

## Langkah Percobaan

### A. Memulai Capture Paket
1. Buka aplikasi Wireshark.
2. Pada halaman awal, pilih antarmuka jaringan yang sedang aktif dan digunakan untuk koneksi internet (contoh: `Wi-Fi` atau `Ethernet`).
3. Klik ganda pada antarmuka tersebut, atau klik ikon sirip hiu berwarna biru (**Start capturing packets**) di pojok kiri atas untuk memulai penangkapan data.
4. Buka *browser* dan akses sebuah situs web untuk menghasilkan lalu lintas data.

### B. Menerapkan Display Filter (Penyaringan Tampilan)
1. Kembali ke jendela utama Wireshark, perhatikan kolom *display filter* (spesifikasi filter tampilan) di bagian atas.
2. Ketikkan `http` (tanpa tanda kutip, huruf kecil semua) pada kolom tersebut.
3. Tekan **Enter** pada keyboard atau klik tombol **Terapkan/Apply** (panah biru di sebelah kanan kolom).
4. Amati jendela daftar paket (*Packet List*). Sekarang jendela tersebut hanya akan menampilkan pesan-pesan yang menggunakan protokol HTTP saja.

### C. Menganalisis Detail Enkapsulasi Paket HTTP
1. Klik salah satu baris pesan HTTP yang muncul di jendela daftar paket untuk memilihnya.
2. Perhatikan jendela detail paket (*Packet Details*) di panel tengah.
3. Lakukan ekspansi (klik tanda panah `>`) pada masing-masing tingkatan protokol untuk melihat konten terperinci dari proses enkapsulasi:
   * **Hypertext Transfer Protocol (HTTP):** Berisi pesan tingkat aplikasi yang sedang diakses.
   * **Transmission Control Protocol (TCP):** Menunjukkan bahwa pesan HTTP tersebut berada di dalam segmen TCP.
   * **Internet Protocol Version 4 (IPv4):** Menunjukkan bahwa segmen TCP berada di dalam datagram IPv4.
   * **Ethernet II:** Menunjukkan bahwa datagram IPv4 dibungkus di dalam bingkai (*frame*) Ethernet (Wi-Fi/LAN).
4. Berfokus pada konten di tingkat pesan, segmen, datagram, dan bingkai ini memungkinkan kita untuk melihat secara spesifik bagaimana pesan HTTP dibungkus dan dikirimkan melalui jaringan.

### D. Menghentikan Capture
1. Klik ikon kotak berwarna merah (**Stop capturing packets**) di *toolbar* atas untuk menghentikan tangkapan jaringan setelah analisis selesai.

## Lampiran
Hasil Percobaan:
![Hasil Percobaan Modul 2](../assets/image/week2.png)