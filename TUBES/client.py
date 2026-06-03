# client.py
import socket
import os

def send_text(clientSocket, text):
    header = f"TEXT|{text}"
    clientSocket.send(header.encode('utf-8'))
    print("Server response:", clientSocket.recv(1024).decode('utf-8'))

def send_file(clientSocket, filepath):
    if not os.path.exists(filepath):
        print("[SYSTEM] File tidak ditemukan. Pastikan path tanpa tanda kutip ganda.")
        return
        
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    
    # Kirim header informasi file
    header = f"FILE|{filename}|{filesize}"
    clientSocket.send(header.encode('utf-8'))
    
    # Tunggu konfirmasi server siap menerima file
    response = clientSocket.recv(1024).decode('utf-8')
    if response == "READY":
        print(f"Mengirim {filename}...")
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                clientSocket.send(chunk)
        print("Server response:", clientSocket.recv(1024).decode('utf-8'))

def start_client():
    serverName = '127.0.0.1'
    serverPort = 12000
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print("[CONNECTED] Terhubung ke server.")
    
    while True:
        print("\n=== MENU UNICAST ===")
        print("1. Kirim Teks (Kata/Kalimat/Paragraf)")
        print("2. Kirim File (Dokumen/Gambar/Audio/Video)")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            teks = input("Masukkan teks yang ingin dikirim: ")
            send_text(clientSocket, teks)
        elif pilihan == '2':
            filepath = input("Masukkan lokasi file (contoh: Portofolio.pdf): ")
            send_file(clientSocket, filepath)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")
            
    clientSocket.close()

if __name__ == "__main__":
    start_client()