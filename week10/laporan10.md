# Modul 10 IP (Internet Protocol)
### Datagram IPv4 dan IPv6 menggunakan Wireshark

Nama    : Naufal Fudhail  
NIM     : 103072400013  
Kelas   : IF-04-04

---

## 📋 Daftar Isi
- [Alat yang Perlu disiapkan](#-alat-yang-perlu-disiapkan)
- [Hasil Analisis IPv4](#-hasil-analisis-ipv4)
- [Investigasi IPv6](#-investigasi-ipv6)

---

## 🛠️ Alat yang Perlu disiapkan
* **Wireshark**: Alat bantu analisis paket (Packet Sniffer).
* **Terminal/CMD**: Digunakan untuk menjalankan perintah `ping` dan `traceroute` (atau `tracert` di Windows).
* **Browser**: Untuk memicu lalu lintas HTTP/IP.

---

## 📝 Hasil Analisis IPv4

Berdasarkan penangkapan paket menggunakan perintah `tracert gaia.cs.umass.edu`, berikut adalah analisis header IPv4 pada paket ICMP Echo Request:

### 1. Header Detail
| Field | Nilai (Value) | Deskripsi |
| :--- | :--- | :--- |
| **Source Address** | `192.168.56.1` | Alamat IP pengirim. |
| **Destination Address** | `128.119.245.12` | Alamat IP server tujuan. |
| **Protocol** | `ICMP (1)` | Protokol lapisan atas yang diangkut. |
| **Header Length** | `20 bytes` | Ukuran standar header IP tanpa options. |
| **Total Length** | `92 bytes` | Total ukuran header + payload. |

![IPv4](../Assets/Modul10-1.png)

### 2. Analisis Time to Live (TTL)
Pada setiap *hop* (lompatan) router dalam perintah `traceroute`, nilai TTL pada paket yang kembali akan memberikan informasi mengenai jarak logis router tersebut. Setiap kali paket melewati router, nilai TTL dikurangi 1. Jika TTL mencapai 0, router akan membuang paket dan mengirimkan pesan *ICMP Time Exceeded* kembali ke pengirim.

![TTL](../Assets/Modul10-2.png)

---

## 🌍 Investigasi IPv6

Perbedaan signifikan ditemukan saat menganalisis datagram IPv6 dibanding IPv4:
* **Alamat IPv6** menggunakan alamat 128-bit yang jauh lebih panjang.
* **Header IPv6** lebih sederhana (fixed size 40 bytes) karena field seperti *Checksum* dan *Fragmentation* dihilangkan dari header utama untuk mempercepat pemrosesan router.
* **IPv6** digunakan untuk manajemen Quality of Service (QoS).

## 🤝 Kontribusi
Laporan ini disusun sebagai bagian dari tugas praktikum S-1 Informatika Telkom University. Kalau kamu ingin memberikan saran atau perbaikan pada dokumentasi ini, silakan ikuti langkah berikut:
1.  Lakukan **Fork** pada repositori ini.
2.  Buat branch baru untuk fitur atau perbaikan Anda.
3.  Kirimkan **Pull Request** dengan penjelasan mengenai perubahan yang dilakukan.

---
**Informatics Lab - Telkom University** *Tahun Ajaran 2025/2026*