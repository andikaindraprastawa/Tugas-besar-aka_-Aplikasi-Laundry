import time

# Variabel Global
BIAYA_PER_KG = 5000  # Biaya per kilogram
NAMA_PELANGGAN = [
    "Andi", "Budi", "Citra", "Diana", "Eka", "Fajar", "Gilang", "Hilda", "Indra", "Joko",
    "Kiki", "Lina", "Maya", "Nina", "Oka", "Putra", "Qori", "Rina", "Siti", "Tito"
]
JENIS_BARANG = [
    "Pakaian", "Selimut", "Handuk", "Bedcover", "Karpet", "Gorden", "Jas", "Boneka", "Sepatu", "Sarung"
]

# Data Pesanan Statis (20 data)
data_pesanan = [
    {"nama": "Andi", "jenis": "Pakaian", "berat": 3.5, "total": 3.5 * BIAYA_PER_KG},
    {"nama": "Budi", "jenis": "Selimut", "berat": 2.0, "total": 2.0 * BIAYA_PER_KG},
    {"nama": "Citra", "jenis": "Handuk", "berat": 1.8, "total": 1.8 * BIAYA_PER_KG},
    {"nama": "Diana", "jenis": "Bedcover", "berat": 5.0, "total": 5.0 * BIAYA_PER_KG},
    {"nama": "Eka", "jenis": "Karpet", "berat": 7.2, "total": 7.2 * BIAYA_PER_KG},
    {"nama": "Fajar", "jenis": "Gorden", "berat": 4.1, "total": 4.1 * BIAYA_PER_KG},
    {"nama": "Gilang", "jenis": "Jas", "berat": 3.3, "total": 3.3 * BIAYA_PER_KG},
    {"nama": "Hilda", "jenis": "Boneka", "berat": 2.2, "total": 2.2 * BIAYA_PER_KG},
    {"nama": "Indra", "jenis": "Sepatu", "berat": 1.2, "total": 1.2 * BIAYA_PER_KG},
    {"nama": "Joko", "jenis": "Sarung", "berat": 2.5, "total": 2.5 * BIAYA_PER_KG},
    {"nama": "Kiki", "jenis": "Pakaian", "berat": 6.5, "total": 6.5 * BIAYA_PER_KG},
    {"nama": "Lina", "jenis": "Karpet", "berat": 4.7, "total": 4.7 * BIAYA_PER_KG},
    {"nama": "Maya", "jenis": "Handuk", "berat": 3.2, "total": 3.2 * BIAYA_PER_KG},
    {"nama": "Nina", "jenis": "Bedcover", "berat": 5.6, "total": 5.6 * BIAYA_PER_KG},
    {"nama": "Oka", "jenis": "Sarung", "berat": 2.4, "total": 2.4 * BIAYA_PER_KG},
    {"nama": "Putra", "jenis": "Gorden", "berat": 3.8, "total": 3.8 * BIAYA_PER_KG},
    {"nama": "Aditya", "jenis": "Pakaian", "berat": 5.1, "total": 5.1 * BIAYA_PER_KG},
    {"nama": "Bella", "jenis": "Karpet", "berat": 3.6, "total": 3.6 * BIAYA_PER_KG},
    {"nama": "Cahya", "jenis": "Selimut", "berat": 4.3, "total": 4.3 * BIAYA_PER_KG},
    {"nama": "Darto", "jenis": "Boneka", "berat": 2.8, "total": 2.8 * BIAYA_PER_KG},
    {"nama": "Erik", "jenis": "Sepatu", "berat": 1.9, "total": 1.9 * BIAYA_PER_KG},
    {"nama": "Fiona", "jenis": "Handuk", "berat": 2.4, "total": 2.4 * BIAYA_PER_KG},
    {"nama": "Geri", "jenis": "Jas", "berat": 3.7, "total": 3.7 * BIAYA_PER_KG},
    {"nama": "Hana", "jenis": "Pakaian", "berat": 6.0, "total": 6.0 * BIAYA_PER_KG},
    {"nama": "Iwan", "jenis": "Bedcover", "berat": 5.5, "total": 5.5 * BIAYA_PER_KG},
    {"nama": "Jati", "jenis": "Gorden", "berat": 4.0, "total": 4.0 * BIAYA_PER_KG},
    {"nama": "Kiran", "jenis": "Karpet", "berat": 3.2, "total": 3.2 * BIAYA_PER_KG},
    {"nama": "Lia", "jenis": "Sarung", "berat": 2.7, "total": 2.7 * BIAYA_PER_KG},
    {"nama": "Milan", "jenis": "Sepatu", "berat": 1.6, "total": 1.6 * BIAYA_PER_KG},
    {"nama": "Nanda", "jenis": "Pakaian", "berat": 7.0, "total": 7.0 * BIAYA_PER_KG},
    {"nama": "Omar", "jenis": "Boneka", "berat": 3.0, "total": 3.0 * BIAYA_PER_KG},
    {"nama": "Putu", "jenis": "Selimut", "berat": 4.5, "total": 4.5 * BIAYA_PER_KG},
    {"nama": "Qina", "jenis": "Handuk", "berat": 2.2, "total": 2.2 * BIAYA_PER_KG},
    {"nama": "Raka", "jenis": "Karpet", "berat": 5.8, "total": 5.8 * BIAYA_PER_KG},
    {"nama": "Sela", "jenis": "Gorden", "berat": 3.4, "total": 3.4 * BIAYA_PER_KG},
    {"nama": "Tasya", "jenis": "Jas", "berat": 4.9, "total": 4.9 * BIAYA_PER_KG},   
    {"nama": "Alya", "jenis": "Handuk", "berat": 2.9, "total": 2.9 * BIAYA_PER_KG},
    {"nama": "Bastian", "jenis": "Selimut", "berat": 4.1, "total": 4.1 * BIAYA_PER_KG},
    {"nama": "Cici", "jenis": "Sepatu", "berat": 1.7, "total": 1.7 * BIAYA_PER_KG},
    {"nama": "Dinda", "jenis": "Pakaian", "berat": 6.3, "total": 6.3 * BIAYA_PER_KG},
    {"nama": "Elma", "jenis": "Gorden", "berat": 3.3, "total": 3.3 * BIAYA_PER_KG},
    {"nama": "Farhan", "jenis": "Boneka", "berat": 2.6, "total": 2.6 * BIAYA_PER_KG},
    {"nama": "Gina", "jenis": "Karpet", "berat": 4.4, "total": 4.4 * BIAYA_PER_KG},
    {"nama": "Hendra", "jenis": "Jas", "berat": 4.2, "total": 4.2 * BIAYA_PER_KG},
    {"nama": "Irma", "jenis": "Bedcover", "berat": 5.4, "total": 5.4 * BIAYA_PER_KG},
    {"nama": "Jovan", "jenis": "Sarung", "berat": 3.1, "total": 3.1 * BIAYA_PER_KG},
    {"nama": "Karla", "jenis": "Pakaian", "berat": 7.4, "total": 7.4 * BIAYA_PER_KG},
    {"nama": "Lukas", "jenis": "Sepatu", "berat": 1.5, "total": 1.5 * BIAYA_PER_KG},
    {"nama": "Mira", "jenis": "Handuk", "berat": 2.0, "total": 2.0 * BIAYA_PER_KG},
    {"nama": "Nadia", "jenis": "Gorden", "berat": 3.0, "total": 3.0 * BIAYA_PER_KG},
    {"nama": "Oki", "jenis": "Boneka", "berat": 2.3, "total": 2.3 * BIAYA_PER_KG},
    {"nama": "Penny", "jenis": "Karpet", "berat": 4.0, "total": 4.0 * BIAYA_PER_KG},
    {"nama": "Qita", "jenis": "Sepatu", "berat": 1.8, "total": 1.8 * BIAYA_PER_KG},
    {"nama": "Rudi", "jenis": "Selimut", "berat": 3.8, "total": 3.8 * BIAYA_PER_KG},
    {"nama": "Sinta", "jenis": "Pakaian", "berat": 5.9, "total": 5.9 * BIAYA_PER_KG},
]





# Fungsi Sequential Search (Iteratif)
def sequential_search_iterative(data, nama):
    for pesanan in data:
        if pesanan['nama'].lower() == nama.lower():
            return pesanan
    return None

# Fungsi Sequential Search (Rekursif)
def sequential_search_recursive(data, nama, index=0):
    if index >= len(data):
        return None
    if data[index]['nama'].lower() == nama.lower():
        return data[index]
    return sequential_search_recursive(data, nama, index + 1)

# Fungsi Cari Pesanan
def cari_pesanan():
    nama = input("\nMasukkan nama pelanggan yang ingin dicari: ")

    # Sequential Search Iteratif
    start_iterative = time.perf_counter()  # Mulai waktu iteratif dengan presisi tinggi
    hasil_iteratif = sequential_search_iterative(data_pesanan, nama)
    end_iterative = time.perf_counter()  # Waktu selesai iteratif
    
    # Sequential Search Rekursif
    start_recursive = time.perf_counter()  # Mulai waktu rekursif dengan presisi tinggi
    hasil_rekursif = sequential_search_recursive(data_pesanan, nama)
    end_recursive = time.perf_counter()  # Waktu selesai rekursif
    
    # Output Hasil Pencarian
    print("\n=== Hasil Pencarian ===")
    if hasil_iteratif:
        print(f"Nama: {hasil_iteratif['nama']}")
        print(f"Jenis Barang: {hasil_iteratif['jenis']}")
        print(f"Berat: {hasil_iteratif['berat']} kg")
        print(f"Total Harga: Rp{hasil_iteratif['total']}")
    else:
        print("Data pelanggan tidak ditemukan.")
    
    # Tampilkan Running Time dalam milidetik (ms)
    print("\n=== Running Time ===")
    print(f"Sequential Search Iteratif: {(end_iterative - start_iterative) * 1000:.6f} ms")
    print(f"Sequential Search Rekursif: {(end_recursive - start_recursive) * 1000:.6f} ms")

# Fungsi Tampilkan Semua Pesanan
def tampilkan_pesanan():
    print("\n=== Daftar Semua Pesanan ===")
    if not data_pesanan:
        print("Belum ada pesanan.")
        return
    for i, pesanan in enumerate(data_pesanan, start=1):
        print(f"{i}. Nama: {pesanan['nama']}, Jenis: {pesanan['jenis']}, Berat: {pesanan['berat']} kg, Total: Rp{pesanan['total']}")

# Fungsi untuk Menambah Pesanan
def tambah_pesanan():
    nama = input("\nMasukkan nama pelanggan: ")
    jenis = input("Masukkan jenis barang: ")
    berat = float(input("Masukkan berat barang (kg): "))
    total = berat * BIAYA_PER_KG

    pesanan_baru = {"nama": nama, "jenis": jenis, "berat": berat, "total": total}
    data_pesanan.append(pesanan_baru)
    print("\nPesanan berhasil ditambahkan!")

# Menu Utama
def menu():
    while True:
        print("\n=== Aplikasi Laundry ===")
        print("1. Tambah Pesanan")
        print("2. Cari Pesanan")
        print("3. Tampilkan Semua Pesanan")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            tambah_pesanan()
        elif pilihan == '2':
            cari_pesanan()
        elif pilihan == '3':
            tampilkan_pesanan()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi laundry!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi!")


# Menjalankan Program
if __name__ == "__main__":
    menu()