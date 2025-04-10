# List untuk menyimpan barang dalam keranjang
keranjang = []

def tampilkan_menu():
    """Menampilkan menu utama"""
    print("\n===== APLIKASI KASIR SEDERHANA =====")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang")
    print("3. Hapus Barang dari Keranjang")
    print("4. Hitung Total & Diskon")
    print("5. Pembayaran")
    print("6. Keluar")

def tambah_barang():
    """Menambahkan barang ke dalam keranjang"""
    nama = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    keranjang.append((nama, harga))
    print(f"{nama} berhasil ditambahkan!")

def lihat_keranjang():
    """Menampilkan daftar barang dalam keranjang"""
    if not keranjang:
        print("Keranjang masih kosong.")
        return
    
    print("\n===== DAFTAR BARANG =====")
    for i, (nama, harga) in enumerate(keranjang, start=1):
        print(f"{i}. {nama} - Rp{harga:.2f}")

def hapus_barang():
    """Menghapus barang dari keranjang"""
    lihat_keranjang()
    if not keranjang:
        return

    try:
        indeks = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
        if 0 <= indeks < len(keranjang):
            barang_dihapus = keranjang.pop(indeks)
            print(f"{barang_dihapus[0]} berhasil dihapus dari keranjang.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Harap masukkan angka yang benar.")

def hitung_total():
    """Menghitung total harga dan memberikan diskon jika berlaku"""
    if not keranjang:
        print("Keranjang masih kosong.")
        return

    total = sum(harga for _, harga in keranjang)
    
    # Diskon 10% jika total lebih dari Rp100.000
    if total > 100000:
        diskon = total * 0.10
        total -= diskon
        print(f"Anda mendapatkan diskon 10%! Diskon: Rp{diskon:.2f}")

    print(f"Total harga yang harus dibayar: Rp{total:.2f}")
    return total

def pembayaran():
    """Memproses pembayaran dengan input uang pelanggan dan kembalian"""
    total = hitung_total()
    if not keranjang:
        return

    while True:
        try:
            uang_pelanggan = float(input("Masukkan jumlah uang pelanggan: "))
            if uang_pelanggan >= total:
                kembalian = uang_pelanggan - total
                print(f"Pembayaran berhasil! Kembalian Anda: Rp{kembalian:.2f}")
                keranjang.clear()  # Mengosongkan keranjang setelah pembayaran
                break
            else:
                print("Uang tidak cukup. Harap masukkan jumlah yang benar.")
        except ValueError:
            print("Harap masukkan angka yang valid.")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tambah_barang()
    elif pilihan == "2":
        lihat_keranjang()
    elif pilihan == "3":
        hapus_barang()
    elif pilihan == "4":
        hitung_total()
    elif pilihan == "5":
        pembayaran()
    elif pilihan == "6":
        print("Terima kasih telah menggunakan aplikasi kasir!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")