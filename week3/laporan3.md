# Laporan Praktikum: Analisis Protokol HTTP dengan Wireshark

## 3.2 Basic HTTP GET/Response Interaction

Bagian ini mendokumentasikan interaksi dasar antara browser (client) dan web server menggunakan protokol HTTP.

---

### Langkah-Langkah Eksperimen

#### 1. Persiapan dan Filter Wireshark
Pertama, buka aplikasi Wireshark dan ketikkan `http` pada kolom filter. Hal ini dilakukan agar Wireshark hanya menampilkan paket-paket yang relevan dengan protokol HTTP.

![Gambar 1](../assets/image/week3(Gambar1).png)

#### 2. Memulai Capture dan Akses URL
Setelah filter siap, mulai proses *packet capture*. Buka browser dan masukkan alamat URL berikut:
`http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html`

![Gambar 2](../assets/image/week3(Gambar2).png)

#### 3. Verifikasi Tampilan Browser
Halaman web akan menampilkan teks satu baris sebagai tanda bahwa file HTML berhasil diunduh. Segera hentikan proses *capture* di Wireshark setelah halaman muncul.

![Gambar 3](../assets/image/week3(Gambar3).png)

#### 4. Analisis Paket HTTP GET dan Response
Pada jendela Wireshark, kita dapat melihat paket **HTTP GET** yang dikirim oleh browser dan paket **HTTP OK (200)** yang dikirim oleh server sebagai balasan.

![Gambar 4](../assets/image/week3(Gambar4).png)

---

### Ringkasan Hasil Analisis

Berdasarkan data yang tertangkap pada **Gambar 4**:

* **Metode Permintaan:** HTTP GET
* **Status Balasan:** 200 OK
* **Source IP:** Alamat IP perangkat Anda (Client).
* **Destination IP:** 128.119.245.12 (Server gaia.cs.umass.edu).

---

**Kesimpulan:**
Eksperimen ini berhasil menunjukkan proses *handshake* sederhana di tingkat aplikasi, di mana client meminta data dan server merespons dengan konten file HTML yang dimaksud.

## 3.2.1 HTTP CONDITIONAL GET/Response Interaction

Bagian ini menganalisis mekanisme *caching* pada browser menggunakan metode Conditional GET untuk mengoptimalkan penggunaan bandwidth.

---

### Langkah-Langkah Eksperimen

1. **Pembersihan Cache:** Memastikan cache dan history browser telah dihapus agar browser melakukan pengambilan data segar dari server.
2. **Mulai Capture:** Menjalankan Wireshark dan mulai merekam paket data.
3. **Akses URL Pertama kali:** Memasukkan URL:
   `http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html`
   Browser menampilkan file HTML sederhana lima baris.

![Gambar 5](../assets/image/week3(Gambar5).png)

4. **Refresh Halaman (Akses Kedua):** Menekan tombol refresh atau memasukkan kembali URL yang sama dengan cepat untuk memicu mekanisme Conditional GET.
5. **Filter dan Hentikan:** Menghentikan capture dan menggunakan filter `http` untuk melihat daftar paket.

![Gambar 6](../assets/image/week3(Gambar6).png)

---

### Analisis Hasil Capture

Berdasarkan data pada Wireshark (seperti terlihat pada **Gambar 6** dan **Gambar 7**), kita dapat mengamati perbedaan antara permintaan pertama dan kedua:

#### 1. HTTP GET Pertama (Initial Request)
Pada permintaan pertama, server merespons dengan **HTTP/1.1 200 OK**. Server mengirimkan seluruh isi file karena browser belum memiliki salinan di cache lokal.

#### 2. HTTP GET Kedua (Conditional GET)
Pada permintaan kedua (setelah refresh), browser mengirimkan header `If-Modified-Since`. Header ini memberitahu server untuk hanya mengirimkan file jika file tersebut telah berubah sejak waktu tertentu.

![Gambar 7](../assets/image/week3(Gambar7).png)

#### 3. Respon Server: 304 Not Modified
Karena file di server tidak berubah, server tidak mengirimkan kembali isi file. Sebaliknya, server mengirimkan kode status **HTTP/1.1 304 Not Modified**. Hal ini menginstruksikan browser untuk menggunakan salinan file yang sudah ada di cache lokal.

---

### Kesimpulan
Mekanisme **Conditional GET** sangat efektif untuk menghemat sumber daya jaringan. Dengan kode status **304 Not Modified**, server tidak perlu mengirimkan ulang data yang sama, sehingga proses pemuatan halaman menjadi lebih cepat dan penggunaan kuota data menjadi lebih efisien.

## 3.3 HTTP Retrieval of Long Documents

Bagian ini menganalisis bagaimana protokol HTTP dan TCP menangani transfer file HTML yang ukurannya melebihi kapasitas satu segmen data standar (biasanya di atas 1460 byte).

---

### Langkah-Langkah Eksperimen

1. **Pembersihan Cache:** Menghapus cache browser untuk memastikan file diunduh sepenuhnya dari server.
2. **Akses URL File Panjang:** Memasukkan URL:
   `http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html`
   Browser menampilkan dokumen "US Bill of Rights" yang cukup panjang.

![Gambar 8](../assets/image/week3(Gambar10).png)

3. **Filter dan Pengamatan:** Setelah menghentikan capture, masukkan filter `http` untuk menemukan pesan GET, lalu hapus filter tersebut (atau gunakan filter `tcp`) untuk melihat bagaimana file tersebut dipecah.

![Gambar 9](../assets/image/week3(Gambar8).png)

---

### Analisis Segmentasi TCP (Multi-packet Response)

File HTML yang diminta memiliki ukuran sekitar 4500 byte. Karena ukuran ini melebihi **Maximum Segment Size (MSS)** dari koneksi TCP, maka server tidak dapat mengirimkannya dalam satu paket tunggal.

#### 1. Mekanisme "TCP segment of a reassembled PDU"
Berdasarkan pengamatan pada jendela Wireshark (lihat **Gambar 10**), satu respons HTTP tunggal dipecah menjadi beberapa segmen TCP. Wireshark memberikan keterangan **"TCP segment of a reassembled PDU"** pada kolom info.

![Gambar 10](../assets/image/week3(Gambar9).png)

#### 2. Reassembly (Penyusunan Kembali)
Meskipun file terbagi menjadi beberapa paket di lapisan transport (TCP), pada lapisan aplikasi (HTTP), Wireshark tetap menunjukkan bahwa paket-paket tersebut adalah bagian dari satu kesatuan respons `200 OK`. 

---

### Kesimpulan
Praktikum ini membuktikan bahwa:
* Protokol HTTP mengandalkan protokol TCP di bawahnya untuk menangani segmentasi data.
* File yang besar akan dipecah menjadi segmen-segmen kecil agar dapat ditransmisikan melalui jaringan tanpa menyebabkan error.
* Wireshark memiliki kemampuan untuk menyatukan kembali (*reassemble*) segmen-segmen tersebut sehingga kita dapat melihat isi file HTML secara utuh di level aplikasi.

## 3.4 HTML Documents dengan Embedded Objects

Pada bagian ini, kita menganalisis bagaimana browser menangani sebuah halaman HTML yang mengandung objek yang disematkan (*embedded objects*), seperti gambar.

---

### Langkah-Langkah Eksperimen

1. **Akses URL dengan Objek:** Memasukkan URL:
   `http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html`
   Browser menampilkan teks beserta dua buah gambar (logo Pearson dan sampul buku).

![Gambar 11](../assets/image/week3(Gambar11).png)

2. **Pengambilan File HTML Dasar:**
Browser pertama kali mengirimkan perintah `GET` untuk file `HTTP-wireshark-file4.html`. Setelah menerima file ini, browser menemukan referensi URL untuk dua gambar yang disematkan.

![Gambar 12](../assets/image/week3(Gambar13).png)

3. **Pengambilan Objek Gambar (Embedded Objects):**
Segera setelah mengetahui ada objek tambahan, browser secara otomatis mengirimkan permintaan `GET` tambahan untuk masing-masing gambar.

![Gambar 13](../assets/image/week3(Gambar14).png)

![Gambar 14](../assets/image/week3(Gambar15).png)

---

### Kesimpulan
Dari eksperimen ini, dapat disimpulkan bahwa:
* Sebuah halaman web tunggal seringkali terdiri dari banyak file yang terpisah.
* Browser melakukan permintaan HTTP yang terpisah untuk setiap objek yang direferensikan dalam file HTML dasar.
* Meskipun pengguna hanya mengetik satu alamat URL, terjadi banyak interaksi *Request-Response* di balik layar.

## 3.5 HTTP Password Authentication

Pada bagian terakhir ini, kita akan memeriksa bagaimana protokol HTTP menangani akses ke situs web yang dilindungi oleh kata sandi (Basic Authentication).

---

### Langkah-Langkah Eksperimen

1. **Input Kredensial:** Memasukkan username dan password ketika muncul pop-up.

![Gambar 15](../assets/image/week3(Gambar16).png)

2. **Permintaan Pertama & Penolakan (401 Unauthorized):**
Saat browser pertama kali meminta file, server merespons dengan kode status **401 Unauthorized**. Pesan ini memberitahu browser untuk meminta kredensial kepada pengguna.

![Gambar 16](../assets/image/week3(Gambar17).png)

3. **Keberhasilan Akses (200 OK):**
Setelah pengguna memasukkan username dan password, browser mengirimkan kembali permintaan `GET` dengan header **Authorization: Basic**. Server memverifikasi dan mengirimkan kode status **200 OK**.

![Gambar 17](../assets/image/week3(Gambar18).png)

---

### Kesimpulan
Dari percobaan ini, dapat disimpulkan bahwa:
* Mekanisme autentikasi dasar HTTP melibatkan setidaknya dua pasang *request/response*.
* Permintaan pertama akan selalu gagal (**401**) untuk memicu prompt login.
* Kredensial dikirimkan dalam header HTTP dalam format Base64 yang tidak terenkripsi, sehingga disarankan untuk selalu menggunakan HTTPS demi keamanan.

---
**Selesai.** Laporan ini mencakup seluruh modul interaksi HTTP dasar hingga autentikasi menggunakan Wireshark.