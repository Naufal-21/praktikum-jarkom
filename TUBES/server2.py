# server.py
import socket
import threading
import os

# Buat folder untuk menyimpan file jika belum ada
SAVE_DIR = "received_files"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    try:
        while True:
            # Terima header (contoh: "TEXT|Ini pesannya" atau "FILE|namafile.pdf|ukuran")
            header = conn.recv(1024).decode('utf-8')
            if not header:
                break
            
            data_type = header.split("|")[0]
            
            if data_type == "TEXT":
                message = header.split("|", 1)[1]
                print(f"[{addr}] Pesan Teks: {message}")
                conn.send("Pesan teks diterima server.".encode('utf-8'))
                
            elif data_type == "FILE":
                _, filename, filesize = header.split("|")
                filesize = int(filesize)
                filepath = os.path.join(SAVE_DIR, filename)
                
                # Kirim sinyal siap menerima file
                conn.send("READY".encode('utf-8'))
                
                print(f"[{addr}] Menerima file {filename} ({filesize} bytes)...")
                with open(filepath, "wb") as f:
                    bytes_received = 0
                    while bytes_received < filesize:
                        chunk = conn.recv(4096)
                        if not chunk:
                            break
                        f.write(chunk)
                        bytes_received += len(chunk)
                print(f"[{addr}] File {filename} berhasil disimpan di {filepath}")
                conn.send("File berhasil diunggah.".encode('utf-8'))
                
    except ConnectionResetError:
        print(f"[DISCONNECTED] {addr} terputus secara sepihak.")
    finally:
        conn.close()

def start_server():
    serverPort = 12000
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(5)
    print(f"[STARTING] Server siap menerima koneksi di port {serverPort}...")
    
    while True:
        conn, addr = serverSocket.accept()
        # Buat thread baru untuk setiap client yang masuk
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()