import socket
import os

# Buat folder untuk menyimpan file jika belum ada
SAVE_DIR = "received_files"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print(f"=== Server Berjalan (Single Thread) ===")
print(f"Menunggu koneksi di port {serverPort}...")

while True:
    # Server menunggu client masuk di sini
    conn, addr = serverSocket.accept()
    print(f"\n[KONEKSI MASUK] Terhubung dengan {addr}")
    
    try:
        # Loop ini akan terus berjalan mengurus SATU client ini saja
        while True:
            # Terima header
            header = conn.recv(1024).decode('utf-8')
            if not header:
                break # Jika client terputus/keluar, hentikan loop
            
            data_type = header.split("|")[0]
            
            if data_type == "TEXT":
                message = header.split("|", 1)[1]
                print(f"[TEKS DARI {addr[1]}] {message}")
                conn.send("Pesan teks berhasil diterima server.".encode('utf-8'))
                
            elif data_type == "FILE":
                _, filename, filesize = header.split("|")
                filesize = int(filesize)
                filepath = os.path.join(SAVE_DIR, filename)
                
                # Kirim sinyal siap menerima file
                conn.send("READY".encode('utf-8'))
                
                print(f"[FILE MASUK] Menerima {filename} ({filesize} bytes)...")
                with open(filepath, "wb") as f:
                    bytes_received = 0
                    while bytes_received < filesize:
                        chunk = conn.recv(4096)
                        if not chunk:
                            break
                        f.write(chunk)
                        bytes_received += len(chunk)
                        
                print(f"[SUKSES] File {filename} disimpan di folder '{SAVE_DIR}'")
                conn.send("File berhasil diunggah.".encode('utf-8'))
                
    except ConnectionResetError:
        print(f"[TERPUTUS] {addr} memutuskan koneksi secara sepihak.")
    finally:
        # Menutup koneksi client ini, lalu kembali ke atas (accept) untuk menunggu client baru
        conn.close()
        print(f"[KONEKSI DITUTUP] Selesai melayani {addr}")
        print("Menunggu client selanjutnya...")