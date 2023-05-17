queue = [] 

def tambah_buku(queue, buku_baru): 
    queue.append(buku_baru) 
    print(f" {buku_baru} berhasil ditambahkan ke dalam stack.") 

def tambah_pengarang(stack, pengarang_baru):
    queue.append(pengarang_baru) 
    print(f" {pengarang_baru} berhasil ditambahkan ke dalam stack.") 
    
def hapus_buku_terakhir(queue): 
    if len(queue) == 0: 
        print("Stack kosong, tidak ada buku yang dapat dihapus.") 
    else: 
        buku_terakhir = queue.pop() 
        print(f" {buku_terakhir} berhasil dihapus dari stack.") 
    
def tampilkan_buku_teratas(queue): 
    if len(queue)==0: 
        print("Stack kosong, tidak ada barang yang dapat ditampilkan.") 
    else: 
        buku_teratas = queue[-1] 
        print(f"Barang teratas di dalam stack adalah {buku_teratas}.") 
    
while True: 
    print("\nDaftar Transaksi saat ini:", queue) 
    print("Menu:") 
    print("1. Tambah Transaksi") 
    print("2. Hapus Transaksi Terakhir") 
    print("3. Tampilkan Transaksi Teratas") 
    print("4. Keluar") 
    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ") 
    
    if pilihan == "1": 
        buku_baru = input("Masukkan nama anda: ") 
        tambah_buku (queue, buku_baru)
        pengarang_baru = input("Jenis transaksi apa yang ingin anda gunakan? : (Cash/Kredit) ") 
        tambah_pengarang (queue, pengarang_baru) 
    elif pilihan == "2": 
        hapus_buku_terakhir(queue) 
    elif pilihan == "3": 
        tampilkan_buku_teratas(queue) 
    elif pilihan == "4": 
        print("Terima kasih telah menggunakan program ini.")
        break 
    else: 
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.") 
