# Laporan Praktikum: Analisis Protokol HTTP dengan Wireshark

## 3.2 Basic HTTP GET/Response Interaction

Bagian ini mendokumentasikan interaksi dasar antara browser (client) dan web server menggunakan protokol HTTP.

---

### Langkah-Langkah Eksperimen

#### 1. Persiapan dan Filter Wireshark
Pertama, buka aplikasi Wireshark dan ketikkan `http` pada kolom filter. Hal ini dilakukan agar Wireshark hanya menampilkan paket-paket yang relevan dengan protokol HTTP.

![Gambar 1](assets/image/week3(Gambar1).png)

#### 2. Memulai Capture dan Akses URL
Setelah filter siap, mulai proses *packet capture*. Buka browser dan masukkan alamat URL berikut:
`http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html`

![Gambar 2](assets/image/week3(Gambar2).png)

#### 3. Verifikasi Tampilan Browser
Halaman web akan menampilkan teks satu baris sebagai tanda bahwa file HTML berhasil diunduh. Segera hentikan proses *capture* di Wireshark setelah halaman muncul.

![Gambar 3](assets/image/week3(Gambar3).png)

#### 4. Analisis Paket HTTP GET dan Response
Pada jendela Wireshark, kita dapat melihat paket **HTTP GET** yang dikirim oleh browser dan paket **HTTP OK (200)** yang dikirim oleh server sebagai balasan.

![Gambar 4](assets/image/week3(Gambar4).png)

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

![Gambar 5](assets/image/week3(Gambar5).png)

4. **Refresh Halaman (Akses Kedua):** Menekan tombol refresh atau memasukkan kembali URL yang sama dengan cepat untuk memicu mekanisme Conditional GET.
5. **Filter dan Hentikan:** Menghentikan capture dan menggunakan filter `http` untuk melihat daftar paket.

![Gambar 6](assets/image/week3(Gambar6).png)

---

### Analisis Hasil Capture

Berdasarkan data pada Wireshark (seperti terlihat pada **Gambar 6** dan **Gambar 7**), kita dapat mengamati perbedaan antara permintaan pertama dan kedua:

#### 1. HTTP GET Pertama (Initial Request)
Pada permintaan pertama, server merespons dengan **HTTP/1.1 200 OK**. Server mengirimkan seluruh isi file karena browser belum memiliki salinan di cache lokal.

#### 2. HTTP GET Kedua (Conditional GET)
Pada permintaan kedua (setelah refresh), browser mengirimkan header `If-Modified-Since`. Header ini memberitahu server untuk hanya mengirimkan file jika file tersebut telah berubah sejak waktu tertentu.

![Gambar 7](assets/image/week3(Gambar7).png)

#### 3. Respon Server: 304 Not Modified
Karena file di server tidak berubah, server tidak mengirimkan kembali isi file. Sebaliknya, server mengirimkan kode status **HTTP/1.1 304 Not Modified**. Hal ini menginstruksikan browser untuk menggunakan salinan file yang sudah ada di cache lokal.

---

## 3.3 HTTP Retrieval of Long Documents

Bagian ini menganalisis bagaimana protokol HTTP dan TCP menangani transfer file HTML yang ukurannya melebihi kapasitas satu segmen data standar (biasanya di atas 1460 byte).

---

### Langkah-Langkah Eksperimen

1. **Akses URL File Panjang:** Memasukkan URL:
   `http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html`

![Gambar 8](assets/image/week3(Gambar10).png)

2. **Filter dan Pengamatan:** Menggunakan filter `http` untuk menemukan pesan GET.

![Gambar 9](assets/image/week3(Gambar8).png)

3. **Mekanisme Segmentasi TCP:**
Berdasarkan pengamatan pada jendela Wireshark (lihat **Gambar 10**), satu respons HTTP tunggal dipecah menjadi beberapa segmen TCP. Wireshark memberikan keterangan **"TCP segment of a reassembled PDU"**.

![Gambar 10](assets/image/week3(Gambar9).png)

---

## 3.4 HTML Documents dengan Embedded Objects

Pada bagian ini, kita menganalisis bagaimana browser menangani sebuah halaman HTML yang mengandung objek yang disematkan (*embedded objects*), seperti gambar.

---

### Langkah-Langkah Eksperimen

1. **Akses URL dengan Objek:** Memasukkan URL:
   `http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html`

![Gambar 11](assets/image/week3(Gambar11).png)

2. **Pengambilan File HTML Dasar:**
Browser pertama kali mengirimkan perintah `GET` untuk file HTML dasar.

![Gambar 12](assets/image/week3(Gambar13).png)

3. **Pengambilan Objek Gambar Tambahan:**
Segera setelah memproses HTML, browser mengirimkan permintaan `GET` tambahan untuk gambar (logo dan sampul buku).

![Gambar 13](assets/image/week3(Gambar14).png)

![Gambar 14](assets/image/week3(Gambar15).png)

---

## 3.5 HTTP Password Authentication

Pada bagian terakhir ini, kita memeriksa bagaimana protokol HTTP menangani akses ke situs web yang dilindungi oleh kata sandi (Basic Authentication).

---

### Langkah-Langkah Eksperimen

1. **Input Kredensial:** Ketika muncul jendela pop-up login.

![Gambar 15](assets/image/week3(Gambar16).png)

2. **Permintaan Pertama & Penolakan (401 Unauthorized):**
Saat browser pertama kali meminta file tanpa password, server menolak dengan kode **401 Unauthorized**.

![Gambar 16](assets/image/week3(Gambar17).png)

3. **Keberhasilan Akses (200 OK):**
Setelah user memasukkan password, browser mengirimkan header **Authorization: Basic** dan server memberikan akses.

![Gambar 17](assets/image/week3(Gambar18).png)

---
**Selesai.** Laporan ini mencakup seluruh modul interaksi HTTP menggunakan Wireshark.