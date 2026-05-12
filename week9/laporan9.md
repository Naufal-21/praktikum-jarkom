# Modul 9 Web Server Sederhana
### Implementasi Web Server Berbasis TCP Socket Programming

Nama    : Naufal Fudhail 
NIM     : 103072400013  
Kelas   : IF-04-04

---

## 💻 Implementasi Kode ()

### 1. TCP Server (`web-server.py`)

Berikut adalah kode yang sudah saya kembangkan dari modul.

```python
# Import module socket
from socket import *
import sys 

# Inisialisasi socket server
serverSocket = socket(AF_INET, SOCK_STREAM)

# Menyiapkan server socket
serverPort = 9999
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    # Membangun koneksi
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        # Menerima pesan permintaan dari klien
        message = connectionSocket.recv(1024).decode()
        
        # Mengekstrak nama file dari pesan permintaan
        filename = message.split()[1]
        f = open(filename[1:]) 
        
        # Membaca isi file
        outputdata = f.read()
        
        # Mengirim baris respons HTTP standar ke socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        # Mengirim konten file yang diminta ke klien
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
        # Mengirim pesan respons jika file tidak ditemukan (404)
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        # Menutup socket klien
        connectionSocket.close()

serverSocket.close()
sys.exit()
```

Pertama-tama, saya meng-*import* semua yang ada pada *library* `socket`. Saya juga meng-*import* `syc` untuk keluar dari program. Lalu saya membuat `serverSocket` untuk menandai bahwa yang saya gunakan adalah IPv4 (AF_INET) dan menggunakan metode TCP (SOCK_STREAM).

Lalu saya menetapkan serverPort-nya bernilai 9999. Kemudian saya socket dengan nomor port tadi `serverSocket.bind(("", serverPort))` dan membuatnya hanya bisa memiliki 1 koneksi `serverSocket.listen(1)`.

Kemudian saya membuat looping terus menerus agar server bisa melayani permintaan tanpa henti. Lalu saya membuat `connectionSocket` yang digunakan untuk berkomunikasi dengan klien. Sedangkan addr berisi informasi alamat IP klien.



---

### 2. code html (`HelloWorld.html`)

Berikut adalah code html yang telah saya buat dan sengaja dibuat simpel untuk pembelajaran.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OWE</title>
</head>
<body>
    <h1>WI WOK DETOK NOT ONLY TOK DETOK</h1>
</body>
</html>
```