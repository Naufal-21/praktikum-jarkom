# Modul 6 TCP (Transmission Control Protocol)
### Investigasi Mekanisme *Handshake*, *Sequence Numbers*, dan *Congestion Control*

Nama    : Ighfir Maulana  
NIM     : 103072400029  
Kelas   : IF-04-04

---

## 📋 Daftar Isi
- [Prasyarat & Instalasi](#-prasyarat--instalasi)
- [Langkah Praktikum](#-langkah-praktikum)
- [Hasil & Analisis](#-hasil--analisis)
- [Kontribusi](#-kontribusi)

---

## ⚙️ Prasyarat & Instalasi
* **Aplikasi**: Wireshark (Packet Sniffer).
* **File Uji**: `alice.txt` (naskah teks ASCII Alice in Wonderland).
* **URL Target**: `http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html`.
* **Koneksi Jaringan**: Diperlukan untuk proses unggah (upload) file ke server jarak jauh.

---

## 🚀 Langkah Praktikum

1. Kosongkan *cache browser* (sudah pernah dibahas pada modul sebelumnya)
2. Buka http://gaia.cs.umass.edu/wireshark-labs/alice.txt dan unduh salinan ASCII dari naskah `Alice in Wonderland`. Simpan file tersebut di komputer kamu.
3. Buka http://gaia.cs.umass.edu/wireshark-labs/TCP-wireshark-file1.html
![tampilan web target](../Assets/Modul6-1.png)
4. Klik tombol *Browse* untuk memasukkan file `Alice in Wonderland`. **TAPI JANGAN UPLOAD DULU**
5. Buka Wireshark dan mulai *capture*.
6. Baru *upload file* `Alice in Wonderland`.
![tampilan web target2](../Assets/Modul6-2.png)
7. Ketik `tcp` di kolom filter Wireshark.
![tampilan Wireshark](../Assets/Modul6-3.png)
8. Itu untuk file `alice.txt`. Untuk file `tcp- etherealtrace-1` bisa kamu download di sini http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip dan buka dengan Wireshark.

---

## 📝 Hasil & Analisis

### BUNDLE 1
### 1. Berapa alamat IP dan nomor port TCP yang digunakan oleh komputer klien (sumber) untuk mentransfer file ke gaia.cs.umass.edu?
![Jawaban 1](../Assets/Modul6-4.png)
* **Jawaban**: alamat IP-nya adalah `192.168.1.102` dan port-nya adalah `1161`. 

### 2. Apa alamat IP dari gaia.cs.umass.edu? Pada nomor port berapa ia mengirim dan menerima segmen TCP untuk koneksi ini?
![Jawaban 2](../Assets/Modul6-4.png)
* **Jawaban**: alamat IP-nya adalah `128.119.245.12` dan menggunakan port `80` karena menggunakan koneksi HTTP standar.

### BUNDLE 2
### 1. Berapa nomor urut segmen TCP SYN yang digunakan untuk memulai sambungan TCP antara komputer klien dan gaia.cs.umass.edu? Apa yang dimiliki segmen tersebut sehingga teridentifikasi sebagai segmen SYN?
![Jawaban 1](../Assets/Modul6-5.png)
* **Jawaban**: Pertama-tama, ketik filter `tcp.flags.syn == 1 && tcp.flags.ack == 0` untuk mengetahui paket pertama dalam koneksi. Untuk nomor urutnya yang muncul pada tampilan saya adalah `0`. Sedangkan untuk mengidentifikasi segmennya sebagai SYN adalah dengan mencari `Flags` di header `TCP`, lalu cari bit `Syn` bernilai 1, dan bit lainnya bernilai 0 yang menandakan itu adalah segmen SYN yang digunakan untuk memulai sambungan TCP.

### 2. Berapa nomor urut segmen SYNACK yang dikirim oleh gaia.cs.umass.edu ke komputer klien sebagai balasan dari SYN? Berapa nilai dari field Acknowledgement pada segmen SYNACK? Bagaimana gaia.cs.umass.edu menentukan nilai tersebut? Apa yang dimiliki oleh segmen sehingga teridentifikasi sebagai segmen SYNACK?
![Jawaban 2](../Assets/Modul6-6.png)
* **Jawaban**: Pertama-tama, ketik filter `tcp.flags.syn == 1 && tcp.flags.ack == 1`. Untuk nomor urutnya yang muncul pada tampilan saya adalah `0`. Untuk nilai `Acknowledgement`-nya adalah `1`. Server menentukannya dengan mengambil Sequence Number dari SYN di atas dan menambahnya dengan 1. Naah, untuk mengidentifikasinya yaitu dengan melihat bit `Syn` dan `Acknowledgment` bernilai 1.

### 3. Berapa nomor urut segmen TCP yang berisi perintah HTTP POST? Perhatikan bahwa untuk menemukan perintah POST, Anda harus menelusuri content field milik paket di bagian bawah jendela Wireshark, kemudian cari segmen yang berisi "POST" di bagian field DATAnya.
![Jawaban 3.2](../Assets/Modul6-7.png)
![Jawaban 3.2](../Assets/Modul6-8.png)
* **Jawaban**: Pertama-tama, ketik filter `http.request.method == "POST"`. Untuk nomor urutnya yang muncul pada tampilan saya adalah `164041`. Dan saya telah menemukan segment `POST` di bagian datanya seperti di gambar.

### 4. Anggap segmen TCP yang berisi HTTP POST sebagai segmen pertama dalam koneksi TCP. Berapa nomor urut dari enam segmen pertama dalam TCP (termasuk segmen yang berisi HTTP POST)? Pada jam berapa setiap segmen dikirim? Kapan ACK untuk setiap segmen diterima? Dengan adanya perbedaan antara kapan setiap segmen TCP dikirim dan kapan acknowledgement-nya diterima, berapakah nilai RTT untuk keenam segmen tersebut? Berapa nilai EstimatedRTT setelah penerimaan setiap ACK? (Catatan: Wireshark memiliki fitur yang memungkinkan Anda untuk memplot RTT untuk setiap segmen TCP yang dikirim. Pilih segmen TCP yang dikirim dari klien ke server gaia.cs.umass.edu pada jendela "daftar paket yang ditangkap". Kemudian pilih: Statistics->TCP Stream Graph- >Round Trip Time Graph).
![Jawaban 4](../Assets/Modul6-9.png)
* **Jawaban**:
1. No = 192, SEQ = 156469, Time = 5.197508, RTT = 0.099749
2. No = 193, SEQ = 157929, Time = 5.198388, RTT = 0.091083
3. No = 194, SEQ = 159389, Time = 5.199275, RTT = 0.098066
4. No = 195, SEQ = 160849, Time = 5.200252, RTT = 0.097089
5. No = 196, SEQ = 162309, Time = 5.201150, RTT = 0.096191
6. No = 199, SEQ = 164041, Time = 5.297341, RTT = 0.092130

### 5. Berapa panjang setiap enam segmen TCP pertama?
![Jawaban 5](../Assets/Modul6-10.png)
* **Jawaban**: Panjangnya adalah `1460` bytes yang mana itu adalah hasil pengurangan batas standar Ethernet dengan header IP (`20 byte`) dan header TCP (`20 byte`).

### 6. Berapa jumlah minimum ruang buffer tersedia yang disarankan kepada penerima dan diterima untuk seluruh trace? Apakah kurangnya ruang buffer penerima pernah menghambat pengiriman?
![Jawaban 6](../Assets/Modul6-11.png)
* **Jawaban**: Ruang buffer untuk kasus ini adalah `62780` yang setelah saya cek selalu `stabil`. Jika ruang buffer berkurang, maka akan menghambat pengiriman ke penerima. Namun untuk kasus ini stabil.

### 7. Apakah ada segmen yang ditransmisikan ulang dalam file trace? Apa yang anda periksa (di dalam file trace) untuk menjawab pertanyaan ini?
![Jawaban 7](../Assets/Modul6-11.png)
* **Jawaban**: Tidak ada. Cara mengeceknya ada 2 cara. Cara pertama mencari `[TCP Retransmission]` pada kolom info. Cara kedua (yang lebih mudah), cari paket yang `berwarna latar belakang hitam dengan tulisan merah`.

### 8. Berapa banyak data yang biasanya diakui oleh penerima dalam ACK? Dapatkah anda mengidentifikasi kasus-kasus di mana penerima melakukan ACK untuk setiap segmen yang diterima?
![Jawaban 8](../Assets/Modul6-12.png)
* **Jawaban**: Dalam kasus ini penerima melakukan ACK `untuk setiap segmen` (paket No. 146 untuk No. 145). tapi saya juga menemukan bahwa penerima juga melakukan `satu paket ACK mengakui dua segmen langsung` (paket No. 149 untuk paket No. 147 dan No. 148).

### 9. Berapa throughput (byte yang ditransfer per satuan waktu) untuk sambungan TCP? Jelaskan bagaimana Anda menghitung nilai ini.
![Jawaban 8](../Assets/Modul6-12.png)
* **Jawaban**:
1. Waktu mulai: Paket No. 145 pada detik `1.602640`.
2. Waktu selesai: Paket No. 152 pada detik `1.854215`.
3. Total data: 6405 - 1 = `6404 byte` (Ack terakhir = 6405, nomor urut dimulai dari 1).
4. Selisih waktu: 1.854215 - 1.602640 = `0.251575 detik`
5. Throughput: Total data/selisih waktu = 6404 byte/0.251575 detik = `25,455 byte/detik` atau `203,64 kbps`.

### BUNDLE 3
### Gunakan alat plotting Time-Sequence-Graph (Stevens) untuk melihat grafik nomor urut berbanding waktu dari segmen yang dikirim oleh klien ke server gaia.cs.umass.edu. Dapatkah Anda mengidentifikasi di mana fase “slow start” TCP dimulai dan berakhir, dan pada bagian mana algoritma ”congestion avoidance” mengambil alih? Berikan komentar tentang bagaimana data yang diukur berbeda dari perilaku ideal TCP yang telah kita pelajari.
![alt text](../Assets/Modul6-13.png)
* **Jawaban**: Berdasarkan gambar tersebut terlihat bahwa `fase slow start` terjadi pada `detik 0` sampai sekitar `0,5 atau 0,8` yang terlihat adanya lonjakan di detik 0 sampai detik 1. Kemudian terjadi `fase congestion avoidance` pada setelah `detik 1` yang kalau ditarik garis, akan menghasilkan `garis diagonal yang lurus`.

---

## 🤝 Kontribusi
Laporan ini disusun sebagai bagian dari tugas praktikum S-1 Informatika Telkom University. Kalau kamu ingin memberikan saran atau perbaikan pada dokumentasi ini, silakan ikuti langkah berikut:
1.  Lakukan **Fork** pada repositori ini.
2.  Buat branch baru untuk fitur atau perbaikan Anda.
3.  Kirimkan **Pull Request** dengan penjelasan mengenai perubahan yang dilakukan.

---
**Informatics Lab - Telkom University** *Tahun Ajaran 2025/2026*