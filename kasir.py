keranjang=[]
def tampilan_menu():
    print("\n=== Selamat Datang Di Toko Kami ===")
    print("\n1. Tambah barang\n2. Lihat keranjang\n3. Hitung total\n4. Hapus barang\n5. Pembayaran\n6. Keluar")

def tambah():
    nama=input("masukkan nama produk: ")
    harga=float(input("masukkan harga barang:"))
    try:
        keranjang.append((nama,harga))
        print(f"{nama} seharga Rp {harga:.2f} berhasil di tambahkan ke keranjang.")
    except ValueError:
        print("harga harus berupa angka")

def lihat_keranjang():
    if not keranjang:
        print("keranjang masih kosong.")
    else:
        print("\n=== Daftar Belanja ===")
        for i, (nama, harga) in enumerate(keranjang, start=1):
            print(f"{i}. {nama} - Rp{harga:,.2f}")
    
def hitung_total():
    total=sum(harga for _,harga in keranjang)
    if total > 100000:
        diskon=total * 0.10
        total_setelah_diskon=total - diskon
        print(f"Total: Rp{total:,.2f}") 
        print(f"diskon 10%: Rp{diskon:,.2f}")
        print(f"Total seteleah Diskon Rp{total_setelah_diskon:.2f}")
    else:
        print(f"total: RP{total:,.2f}")
    return total
        
def hapus_barang():
    lihat_keranjang()
    if not keranjang:
        return

    try:
        i=int(input("masukkan no barang yang ingin dihapus: ")) - 1
        if 0 <= len(keranjang):
            barang_dihapus=keranjang.pop(i)
            print(f"{barang_dihapus[0]} berhasil dihapus dari keranjang")
        else:
            print('no barang tidak valid')
    except ValueError:
        print("masukkan angka yang benar")

def pembayaran():
    total = hitung_total()
    if not keranjang :
        return
    while True:
        try:
            uang_pelanggan = float(input("masukkan jumlah uangmu: "))
            if uang_pelanggan >= total :
                kembalian = uang_pelanggan - total
                print (f"pembayaran berhasil! kembalian anda: Rp{kembalian:,.2f}")
                keranjang.clear ()
                break
            else:
                print("uang tidak cukup.")
        except ValueError:
            print("Masukkan Angka yang Valid")
            
def main():
    while True:
        tampilan_menu()
        pilihan=input("Masukkan Angka: ")
        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            lihat_keranjang()
        elif pilihan == "3":
            hitung_total()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan =="5":
            pembayaran()
        elif pilihan == "6":
            print("Terima Kasih Sudah Mampir")
            break
main()