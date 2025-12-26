# PROGRAM SISTEM MANAJEMEN GUDANG SPORTWEAR
# Sistem untuk mengelola inventory barang di gudang sportwear
# Fitur: Login, CRUD, laporan, peringatan stok

import os
import platform
from tabulate import tabulate

# Fungsi untuk membersihkan layar terminal
def clear_screen():
    """Membersihkan layar terminal sesuai sistem operasi"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Data awal inventory (dummy data)
inventory = [
    {"Kode Rak": "BT02", "Kode Barang": "21003", "Nama Barang": "Legging Power", "Kategori": "Bottom", "Stock": 90},
    {"Kode Rak": "TP03", "Kode Barang": "11002", "Nama Barang": "Atasan Sport Training", "Kategori": "Top", "Stock": 15},
    {"Kode Rak": "AS01", "Kode Barang": "31005", "Nama Barang": "Sport Belt Pro", "Kategori": "Accessories", "Stock": 220},
    {"Kode Rak": "TP01", "Kode Barang": "11005", "Nama Barang": "Jaket Sport Extreme", "Kategori": "Top", "Stock": 10},
    {"Kode Rak": "BT01", "Kode Barang": "21001", "Nama Barang": "Legging Flex", "Kategori": "Bottom", "Stock": 0},
    {"Kode Rak": "AS03", "Kode Barang": "31002", "Nama Barang": "Sport Hijab Air", "Kategori": "Accessories", "Stock": 20},
    {"Kode Rak": "TP02", "Kode Barang": "11003", "Nama Barang": "Atasan Sport Active", "Kategori": "Top", "Stock": 60},
    {"Kode Rak": "BT03", "Kode Barang": "21005", "Nama Barang": "Kulot Sport Flow", "Kategori": "Bottom", "Stock": 180},
    {"Kode Rak": "AS02", "Kode Barang": "31001", "Nama Barang": "Sport Hijab Lite", "Kategori": "Accessories", "Stock": 4},
    {"Kode Rak": "TP01", "Kode Barang": "11001", "Nama Barang": "Atasan Sport Basic", "Kategori": "Top", "Stock": 0},
    {"Kode Rak": "BT02", "Kode Barang": "21004", "Nama Barang": "Rok Sport Glide", "Kategori": "Bottom", "Stock": 140},
    {"Kode Rak": "AS03", "Kode Barang": "31004", "Nama Barang": "Sport Cap Run", "Kategori": "Accessories", "Stock": 34},
    {"Kode Rak": "TP02", "Kode Barang": "11004", "Nama Barang": "Jaket Sport Wind", "Kategori": "Top", "Stock": 120},
    {"Kode Rak": "BT01", "Kode Barang": "21002", "Nama Barang": "Legging Motion", "Kategori": "Bottom", "Stock": 7},
    {"Kode Rak": "AS01", "Kode Barang": "31003", "Nama Barang": "Inner Sport Fit", "Kategori": "Accessories", "Stock": 75}
]

# Data kredensial login
credentials = {"admin": "admin1234", "staff": "staff1234","madina": "febriani"}
current_user = ""  # Menyimpan user yang sedang login

# Daftar kategori yang valid
kategori_list = ["Top", "Bottom", "Accessories"]  

# Fungsi untuk menampilkan garis pemisah
def garis():
    print("=" * 60)

# Fungsi untuk menentukan status stok berdasarkan jumlah
def hitung_status(stok):
    if stok == 0:
        return "HABIS"
    elif stok <= 10:
        return "SANGAT MENIPIS"
    elif stok <= 20:
        return "MENIPIS"
    elif stok <= 150:
        return "AMAN"
    else:
        return "OVERLOAD"

# Fungsi untuk validasi input angka
def input_angka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit():
            return int(nilai)
        else:
            print("Silakan masukkan angka yang benar!")

# Fungsi untuk konfirmasi aksi dari user (Ya/Tidak)
def konfirmasi(pesan):
    jawab = input(pesan + " (Y/T): ").upper()
    return jawab == "Y"

# Fungsi untuk mencari barang berdasarkan kode
def cari_barang_by_kode(kode):
    for barang in inventory:
        if barang["Kode Barang"].upper() == kode.upper():
            return barang       # Kembalikan objek barang jika ditemukan
    return None     # Kembalikan None jika tidak ditemukan

# Fungsi untuk mengecek keunikan kode barang
def cek_kode_unik(kode_barang):
    for barang in inventory:
        if barang["Kode Barang"].upper() == kode_barang.upper():
            return True  # Kode sudah ada
    return False # Kode belum ada/unik

# Fungsi untuk menghitung barang yang perlu restock (≤ 10 termasuk 0)
def hitung_perlu_restock():
    """Menghitung jumlah barang dengan stok ≤ 10 (termasuk stok 0)"""
    count = 0
    for barang in inventory:
        if barang["Stock"] <= 10:  # Sekarang termasuk stok 0
            count += 1
    return count # Kembalikan jumlah barang yang perlu restock

# ============================================
#                  FUNGSI LOGIN
# ============================================

def login():
    clear_screen()
    print("\n" + "="*60)
    print("                LOGIN SISTEM MANAJEMEN GUDANG LYVA")
    print("="*60)
    
    attempts = 3  # Maksimal 3 kali percobaan login
    while attempts > 0:
        username_input = input("\nMasukkan username: ")
        password_input = input("Masukkan password: ")

        # Cek apakah username dan password sesuai
        if username_input in credentials and password_input == credentials[username_input]:
            print(f"\nAutentikasi berhasil.\nSelamat datang di Manajemen Inventaris Lyva, {username_input.capitalize()}!")
            global current_user
            current_user = username_input  # Simpan pengguna yang login
            return True
        else:
            attempts -= 1
            print(f"Login gagal. Anda memiliki {attempts} percobaan tersisa.")

    print("\n" + "="*60)
    print("\nPercobaan maksimal tercapai. Program dihentikan sekarang.")
    print("-------  Silahkan restart program    ---------")

# --------------------------------------------
#           FUNGSI EDIT DATA BARANG
# --------------------------------------------

def edit_data_barang():                 # menu utama untuk mengedit data barang (hanya bisa diakses admin)
    # Cek apakah user adalah admin
    if current_user != "admin":
        print("\n Hanya admin yang dapat mengedit data!")
        input("\nTekan ENTER untuk melanjutkan...")
        return
    
    while True:
        clear_screen()
        print("\n" + "="*60)
        print("                EDIT DATA BARANG")
        print("="*60)
        print("1. Edit berdasarkan kategori")
        print("2. Edit berdasarkan rak")
        print("3. Kembali ke Menu Utama")
        print("="*60)
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            edit_by_kategori()
        elif pilihan == "2":
            edit_by_rak()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")
        
        input("\nTekan ENTER untuk melanjutkan...")

# Fungsi helper untuk menampilkan barang dalam format tabel
def tampilkan_barang_filter(barang_list, title, headers, columns): #Menampilkan daftar barang dalam format tabel
    if not barang_list:
        print(f"Tidak ada {title}")
        return None
    
    tabel_data = []
    # membuat tabel dengan nomor urut menggunakan range()
    for i in range(len(barang_list)):
        barang = barang_list[i]
        row = [i + 1]  # i dimulai dari 0, jadi +1 untuk nomor urut
        for col in columns:
            if col == "Stock" and "Status" in headers:
                row.append(barang[col])
                row.append(hitung_status(barang[col]))  # Tambah status
            else:
                row.append(barang[col])
        tabel_data.append(row)
    
    print(f"\n{title}")
    print(tabulate(tabel_data, headers=headers, tablefmt="rounded_grid"))
    return barang_list

# Edit barang berdasarkan kategori yang dipilih
def edit_by_kategori():
    clear_screen()
    print("\nKategori yang tersedia: Top, Bottom, Accessories")
    kategori = input("Masukkan kategori: ").title()
    
    # Validasi kategori
    if kategori not in kategori_list:
        print("Kategori tidak valid!")
        return
    
    # Filter barang berdasarkan kategori
    hasil = [barang for barang in inventory if barang["Kategori"].upper() == kategori.upper()]
    barang_list = tampilkan_barang_filter(hasil, f"BARANG KATEGORI: {kategori}", 
                                          ["NO", "KODE RAK", "KODE BARANG", "NAMA BARANG", "STOCK"],
                                          ["Kode Rak", "Kode Barang", "Nama Barang", "Stock"])
    
    if not barang_list:
        return
    
    # Minta user memilih barang
    pilih_input = input("\nPilih nomor barang yang akan diedit: ")
    if not pilih_input.isdigit():
        print("Input harus berupa angka!")
        return
    
    pilih = int(pilih_input)
    if pilih < 1 or pilih > len(barang_list):
        print("Nomor tidak valid!")
        return
    
    barang_edit = barang_list[pilih-1]
    print(f"\nBarang yang akan diedit: {barang_edit['Nama Barang']}")
    
    # menpampilkan pilihan field yang bisa diedit
    print("\nField yang dapat diedit:")
    print("1. Kode Rak")
    print("2. Nama Barang")
    print("3. Kategori")
    print("4. Stock")
    print("5. Batal")
    
    field = input("Pilih field yang akan diedit (1-5): ")
    
    if field == "1":
        kode_rak_baru = input("Masukkan kode rak baru: ").upper()
        if konfirmasi(f"Ubah kode rak dari '{barang_edit['Kode Rak']}' menjadi '{kode_rak_baru}'?"):
            barang_edit["Kode Rak"] = kode_rak_baru
            print("Kode rak berhasil diubah!")
    
    elif field == "2":
        nama_baru = input("Masukkan nama barang baru: ").title()
        if konfirmasi(f"Ubah nama barang dari '{barang_edit['Nama Barang']}' menjadi '{nama_baru}'?"):
            barang_edit["Nama Barang"] = nama_baru
            print("Nama barang berhasil diubah!")
    
    elif field == "3":
        print("\nPilih Kategori:")
        print("1. Top (Atasan)")
        print("2. Bottom (Bawahan)")
        print("3. Accessories (Aksesoris)")
        pilih_kategori = input("Masukkan pilihan (1-3): ")
        
        if pilih_kategori == "1":
            kategori_baru = "Top"
        elif pilih_kategori == "2":
            kategori_baru = "Bottom"
        elif pilih_kategori == "3":
            kategori_baru = "Accessories"
        else:
            print("Pilihan tidak valid!")
            return
        
        if konfirmasi(f"Ubah kategori dari '{barang_edit['Kategori']}' menjadi '{kategori_baru}'?"):
            barang_edit["Kategori"] = kategori_baru
            print("Kategori berhasil diubah!")
    
    elif field == "4":
        stock_baru = input_angka("Masukkan stock baru: ")
        if konfirmasi(f"Ubah stock dari {barang_edit['Stock']} menjadi {stock_baru}?"):
            barang_edit["Stock"] = stock_baru
            print("Stock berhasil diubah!")
    
    elif field == "5":
        print("Edit dibatalkan.")
    
    else:
        print("Pilihan tidak valid!")

# eedit barang berdasarkan kode rak
def edit_by_rak():
    clear_screen()
    rak = input("\nMasukkan kode rak: ").upper()
    
    # Filter barang berdasarkan kode rak
    hasil = [barang for barang in inventory if barang["Kode Rak"].upper() == rak.upper()]
    barang_list = tampilkan_barang_filter(hasil, f"BARANG DI RAK: {rak}", 
                                          ["NO", "KODE BARANG", "NAMA BARANG", "KATEGORI", "STOCK"],
                                          ["Kode Barang", "Nama Barang", "Kategori", "Stock"])
    
    if not barang_list:
        return
    
    # meminta user memilih barang
    pilih_input = input("\nPilih nomor barang yang akan diedit: ")
    if not pilih_input.isdigit():
        print("Input harus berupa angka!")
        return
    
    pilih = int(pilih_input)
    if pilih < 1 or pilih > len(barang_list):
        print("Nomor tidak valid!")
        return
    
    barang_edit = barang_list[pilih-1]
    print(f"\nBarang yang akan diedit: {barang_edit['Nama Barang']}")
    
    # Tampilkan pilihan field yang bisa diedit
    print("\nField yang dapat diedit:")
    print("1. Kode Rak")
    print("2. Nama Barang")
    print("3. Kategori")
    print("4. Stock")
    print("5. Batal")
    
    field = input("Pilih field yang akan diedit (1-5): ")
    
    if field == "1":
        kode_rak_baru = input("Masukkan kode rak baru: ").upper()
        if konfirmasi(f"Ubah kode rak dari '{barang_edit['Kode Rak']}' menjadi '{kode_rak_baru}'?"):
            barang_edit["Kode Rak"] = kode_rak_baru
            print("Kode rak berhasil diubah!")
    
    elif field == "2":
        nama_baru = input("Masukkan nama barang baru: ").title()
        if konfirmasi(f"Ubah nama barang dari '{barang_edit['Nama Barang']}' menjadi '{nama_baru}'?"):
            barang_edit["Nama Barang"] = nama_baru
            print("Nama barang berhasil diubah!")
    
    elif field == "3":
        print("\nPilih Kategori:")
        print("1. Top (Atasan)")
        print("2. Bottom (Bawahan)")
        print("3. Accessories (Aksesoris)")
        pilih_kategori = input("Masukkan pilihan (1-3): ")
        
        if pilih_kategori == "1":
            kategori_baru = "Top"
        elif pilih_kategori == "2":
            kategori_baru = "Bottom"
        elif pilih_kategori == "3":
            kategori_baru = "Accessories"
        else:
            print("Pilihan tidak valid!")
            return
        
        if konfirmasi(f"Ubah kategori dari '{barang_edit['Kategori']}' menjadi '{kategori_baru}'?"):
            barang_edit["Kategori"] = kategori_baru
            print("Kategori berhasil diubah!")
    
    elif field == "4":
        stock_baru = input_angka("Masukkan stock baru: ")
        if konfirmasi(f"Ubah stock dari {barang_edit['Stock']} menjadi {stock_baru}?"):
            barang_edit["Stock"] = stock_baru
            print("Stock berhasil diubah!")
    
    elif field == "5":
        print("Edit dibatalkan.")
    
    else:
        print("Pilihan tidak valid!")

# --------------------------------------------
#       FUNGSI LIHAT DATA (READ)
# --------------------------------------------

def tampilkan_semua_barang():
    clear_screen()
    if len(inventory) == 0:
        print("Tidak ada data barang.")
        return
    
    tabel_data = []
    total_stock = 0
    
    # Buat tabel semua barang
    for i in range(len(inventory)):
        barang = inventory[i]
        status = hitung_status(barang["Stock"])
        tabel_data.append([
            i + 1,  # i dimulai dari 0, jadi +1 untuk nomor urut
            barang["Kode Rak"],
            barang["Kode Barang"],
            barang["Nama Barang"],
            barang["Kategori"],
            barang["Stock"],
            status
        ])
        total_stock += barang["Stock"]
    
    headers = ["NO", "KODE RAK", "KODE BARANG", "NAMA BARANG", "KATEGORI", "STOCK", "STATUS"]
    print("\n" + "="*100)
    print("                                      DAFTAR SEMUA BARANG DI GUDANG")
    print("="*100)
    print(tabulate(tabel_data, headers=headers, tablefmt="rounded_grid"))

def tampilkan_barang_filter(barang_list, title, headers):
    """Menampilkan daftar barang dalam format tabel dengan status"""
    if not barang_list:
        print(f"Tidak ada {title}")
        return None
    
    tabel_data = []
    for i in range(len(barang_list)):
        barang = barang_list[i]
        row = [i + 1]  # Nomor urut
        
        # Tambahkan data sesuai header
        for header in headers[1:]:  # Skip "NO"
            if header == "KODE RAK":
                row.append(barang["Kode Rak"])
            elif header == "KODE BARANG":
                row.append(barang["Kode Barang"])
            elif header == "NAMA BARANG":
                row.append(barang["Nama Barang"])
            elif header == "KATEGORI":
                row.append(barang["Kategori"])
            elif header == "STOCK":
                row.append(barang["Stock"])
            elif header == "STATUS":
                row.append(hitung_status(barang["Stock"]))
        
        tabel_data.append(row)
    
    print(f"\n{title}")
    print(tabulate(tabel_data, headers=headers, tablefmt="rounded_grid"))
    return barang_list

def tampilkan_by_kategori():
    clear_screen()
    print("\nKategori yang tersedia: Top, Bottom, Accessories")
    kategori = input("Masukkan kategori: ").title()
    
    if kategori not in kategori_list:
        print("Kategori tidak valid!")
        return
    
    # Filter barang berdasarkan kategori
    hasil = [barang for barang in inventory if barang["Kategori"].upper() == kategori.upper()]
    
    tampilkan_barang_filter(hasil, f"BARANG KATEGORI: {kategori}", 
                           ["NO", "KODE RAK", "KODE BARANG", "NAMA BARANG", "STOCK", "STATUS"])

def tampilkan_by_rak():
    clear_screen()
    rak = input("\nMasukkan kode rak: ").upper()
    
    # Filter barang berdasarkan kode rak
    hasil = [barang for barang in inventory if barang["Kode Rak"].upper() == rak.upper()]
    
    tampilkan_barang_filter(hasil, f"BARANG DI RAK: {rak}", 
                           ["NO", "KODE BARANG", "NAMA BARANG", "KATEGORI", "STOCK", "STATUS"])

def cari_barang(): #mencari barang berdasarkan kode barang
    clear_screen()
    kode = input("\nMasukkan kode barang yang dicari: ").upper()
    barang = cari_barang_by_kode(kode)
    
    if barang:
        print("\n" + "="*50)
        print("         DATA BARANG DITEMUKAN")
        print("="*50)
        print(f"Kode Rak      : {barang['Kode Rak']}")
        print(f"Kode Barang   : {barang['Kode Barang']}")
        print(f"Nama Barang   : {barang['Nama Barang']}")
        print(f"Kategori      : {barang['Kategori']}")
        print(f"Stock         : {barang['Stock']}")
        print(f"Status        : {hitung_status(barang['Stock'])}")
        print("="*50)
    else:
        print(f"Barang dengan kode {kode} tidak ditemukan.")

def menu_lihat_data(): # Menu utama untuk melihat data barang
    while True:
        clear_screen()
        garis()
        print("                    MENU DATA BARANG")
        garis()
        print("1. Tampilkan semua barang")
        print("2. Tampilkan berdasarkan kategori")
        print("3. Tampilkan berdasarkan rak")
        print("4. Cari barang berdasarkan kode barang")
        print("5. Kembali ke menu utama")
        garis()
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tampilkan_semua_barang()
        elif pilihan == "2":
            tampilkan_by_kategori()
        elif pilihan == "3":
            tampilkan_by_rak()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")
        
        input("\nTekan ENTER untuk melanjutkan...")

# --------------------------------------------
#       FUNGSI TAMBAH BARANG (CREATE)
# --------------------------------------------

def menu_tambah_barang(): # menu untuk menambah barang baru ke inventory
    clear_screen()
    garis()
    print("                    TAMBAH BARANG BARU")
    garis()
    print("Ketik 'batal' kapan saja untuk membatalkan")
    
    # Input kode rak
    kode_rak = input("\nKode Rak (contoh: BT01): ").upper()
    if kode_rak.lower() == "batal":
        print("Penambahan barang dibatalkan.")
        return
    
    # Input kode barang dengan validasi
    while True:
        kode_barang = input("Kode Barang (5 angka): ").upper()
        if kode_barang.lower() == "batal":
            print("Penambahan barang dibatalkan.")
            return
        
        # Validasi format dan keunikan kode
        if len(kode_barang) != 5 or not kode_barang.isdigit():
            print("Kode barang harus 5 digit angka!")
            continue

        if cek_kode_unik(kode_barang):
            print("Kode barang sudah ada. Gunakan kode yang berbeda.")
        else:
            break
    
    # Input nama barang
    nama_barang = input("Nama Barang: ").title()
    if nama_barang.lower() == "batal":
        print("Penambahan barang dibatalkan.")
        return
    
    # input kategorii
    while True:
        print("\nPilih Kategori:")
        print("1. Top (Atasan)")
        print("2. Bottom (Bawahan)")
        print("3. Accessories (Aksesoris)")
        pilih = input("Masukkan pilihan (1-3): ")
        
        if pilih.lower() == "batal":
            print("Penambahan barang dibatalkan.")
            return
        
        if pilih == "1":
            kategori = "Top"
            break
        elif pilih == "2":
            kategori = "Bottom"
            break
        elif pilih == "3":
            kategori = "Accessories"
            break
        else:
            print("Pilihan tidak valid!")
    
    # Input stok awal
    stock = input_angka("Stock awal: ")
    
    # menaampilkan ringkasan data
    print("\n" + "="*50)
    print("RINGKASAN DATA BARANG BARU")
    print("="*50)
    print(f"Kode Rak      : {kode_rak}")
    print(f"Kode Barang   : {kode_barang}")
    print(f"Nama Barang   : {nama_barang}")
    print(f"Kategori      : {kategori}")
    print(f"Stock         : {stock}")
    print("="*50)
    
    # konfirmasi penyimpanan
    if konfirmasi("\nSimpan data barang ini?"):
        barang_baru = {
            "Kode Rak": kode_rak,
            "Kode Barang": kode_barang,
            "Nama Barang": nama_barang,
            "Kategori": kategori,
            "Stock": stock
        }
        inventory.append(barang_baru)
        print(f"\nBarang '{nama_barang}' berhasil ditambahkan!")
        print(f"Total barang di inventory: {len(inventory)}")
    else:
        print("\nPenambahan barang dibatalkan.")

# --------------------------------------------
#       FUNGSI MENGUUBAH STOCK (UPDATE)
# --------------------------------------------

def menu_ubah_stock():
    clear_screen()
    garis()
    print("UBAH STOCK BARANG")
    garis()
    
    # cross check apakah ada barang
    if len(inventory) == 0:
        print("Tidak ada barang.")
        return
    
    # show up daftar barang ringkas
    tabel_data = []
    for idx, barang in enumerate(inventory, 1):
        tabel_data.append([
            idx,
            barang["Kode Rak"],
            barang["Kode Barang"],
            barang["Nama Barang"],
            barang["Stock"]
        ])
    
    headers = ["NO", "KODE RAK", "KODE BARANG", "NAMA BARANG", "STOCK"]
    print(tabulate(tabel_data, headers=headers, tablefmt="rounded_grid"))
    
    garis()
    kode = input("Masukkan kode barang (atau 'batal'): ").upper()
    
    if kode.lower() == "batal":
        print("Perubahan dibatalkan.")
        return
    
    # find barang berdasarkan kode
    barang = cari_barang_by_kode(kode)
    if not barang:
        print(f"Barang dengan kode {kode} tidak ditemukan!")
        return
    
    # showup data barang saat ini
    print("\n" + "="*50)
    print("DATA BARANG SAAT INI")
    print("="*50)
    print(f"Kode Barang   : {barang['Kode Barang']}")
    print(f"Nama Barang   : {barang['Nama Barang']}")
    print(f"Stock saat ini: {barang['Stock']}")
    print(f"Status        : {hitung_status(barang['Stock'])}")
    print("="*50)
    
    # pilihan update stock
    print("\nPILIHAN UPDATE:")
    print("1. Tambah stock")
    print("2. Kurangi stock")
    print("3. Set stock baru")
    print("4. Batal")
    
    pilihan = input("Pilih opsi (1-4): ")
    
    if pilihan == "1":
        jumlah = input_angka("Jumlah yang ditambahkan: ")
        barang["Stock"] += jumlah
        print(f"Stock berhasil ditambah!")
        print(f"Stock baru: {barang['Stock']}")
        print(f"Status baru: {hitung_status(barang['Stock'])}")
    
    elif pilihan == "2":
        jumlah = input_angka("Jumlah yang dikurangi: ")
        if jumlah > barang["Stock"]:
            print(f"Stock tidak cukup! Stock saat ini: {barang['Stock']}")
        else:
            barang["Stock"] -= jumlah
            print(f"Stock berhasil dikurangi!")
            print(f"Stock baru: {barang['Stock']}")
            print(f"Status baru: {hitung_status(barang['Stock'])}")
    
    elif pilihan == "3":
        jumlah = input_angka("Stock baru: ")
        barang["Stock"] = jumlah
        print(f"Stock berhasil diubah!")
        print(f"Stock baru: {barang['Stock']}")
        print(f"Status baru: {hitung_status(barang['Stock'])}")
    
    elif pilihan == "4":
        print("Perubahan dibatalkan.")
    
    else:
        print("Pilihan tidak valid!")

# --------------------------------------------
#       FUNGSI HAPUS BARANG (DELETE)
# --------------------------------------------

def menu_hapus_barang(): # Menu untuk menghapus barang dari inventory
    # check apakah user adalah admin
    if current_user != "admin":
        print("\n⛔ Hanya admin yang dapat menghapus barang!")
        input("\nTekan ENTER untuk melanjutkan...")
        return
    
    while True:
        clear_screen()
        garis()
        print("                    HAPUS BARANG")
        garis()
        print("1. Hapus berdasarkan kategori")
        print("2. Hapus berdasarkan rak")
        print("3. Kembali ke menu utama")
        garis()
        
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == "1":
            hapus_by_kategori()
            input("\nTekan ENTER untuk melanjutkan...")
        elif pilihan == "2":
            hapus_by_rak()
            input("\nTekan ENTER untuk melanjutkan...")
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan ENTER untuk melanjutkan...")

def hapus_by_kategori(): # Menghapus barang berdasarkan kategori
    clear_screen()
    print("\nKategori yang tersedia: Top, Bottom, Accessories")
    kategori = input("Masukkan kategori: ").title()
    
    if kategori not in kategori_list:
        print("Kategori tidak valid!")
        return
    
    # Filter barang berdasarkan kategori
    hasil = [barang for barang in inventory if barang["Kategori"].upper() == kategori.upper()]
    barang_list = tampilkan_barang_filter(hasil, f"BARANG KATEGORI: {kategori}", 
                                          ["NO", "KODE RAK", "KODE BARANG", "NAMA BARANG", "STOCK"],
                                          ["Kode Rak", "Kode Barang", "Nama Barang", "Stock"])
    
    if not barang_list:
        return
    
    # Minta user memilih barang untuk dihapus
    pilih_input = input("\nPilih nomor barang yang akan dihapus: ")
    if not pilih_input.isdigit():
        print("Input harus berupa angka!")
        return
    
    pilih = int(pilih_input)
    if pilih < 1 or pilih > len(barang_list):
        print("Nomor tidak valid!")
        return
    
    barang_hapus = barang_list[pilih-1]
    
    # Konfirmasi penghapusan
    if konfirmasi(f"\nYakin ingin menghapus barang '{barang_hapus['Nama Barang']}'?"):
        inventory.remove(barang_hapus)
        print(f"Barang '{barang_hapus['Nama Barang']}' berhasil dihapus!")
        print(f"Sisa barang di inventory: {len(inventory)}")
    else:
        print("Penghapusan dibatalkan.")

def hapus_by_rak(): #Menghapus barang berdasarkan kode rak
    clear_screen()
    rak = input("\nMasukkan kode rak: ").upper()
    
    # Filter barang berdasarkan kode rak
    hasil = [barang for barang in inventory if barang["Kode Rak"].upper() == rak.upper()]
    barang_list = tampilkan_barang_filter(hasil, f"BARANG DI RAK: {rak}", 
                                          ["NO", "KODE BARANG", "NAMA BARANG", "KATEGORI", "STOCK"],
                                          ["Kode Barang", "Nama Barang", "Kategori", "Stock"])
    
    if not barang_list:
        return
    
    # Minta user memilih barang untuk dihapus
    pilih_input = input("\nPilih nomor barang yang akan dihapus: ")
    if not pilih_input.isdigit():
        print("Input harus berupa angka!")
        return
    
    pilih = int(pilih_input)
    if pilih < 1 or pilih > len(barang_list):
        print("Nomor tidak valid!")
        return
    
    barang_hapus = barang_list[pilih-1]
    
    # Konfirmasi penghapusan
    if konfirmasi(f"\nYakin ingin menghapus barang '{barang_hapus['Nama Barang']}'?"):
        inventory.remove(barang_hapus)
        print(f"Barang '{barang_hapus['Nama Barang']}' berhasil dihapus!")
        print(f"Sisa barang di inventory: {len(inventory)}")
    else:
        print("Penghapusan dibatalkan.")

# --------------------------------------------
#       FUNGSI PERINGATAN STOK MENIPIS
# --------------------------------------------

def menu_peringatan_stok(): #Menampilkan daftar barang dengan stok menipis (≤ 10) termasuk stok 0
    clear_screen()
    garis()
    print("⚠️  PERINGATAN STOK MENIPIS & HABIS  ⚠️")
    garis()
    
    # Cari barang dengan stok menipis (≤ 10) termasuk stok 0
    barang_menipis = []
    for barang in inventory:
        if barang["Stock"] <= 10:
            barang_menipis.append(barang)
    
    if len(barang_menipis) == 0:
        print("Tidak ada barang dengan stok menipis atau habis.")
        return
    
    tabel_data = []
    total_stock_menipis = 0
    barang_habis = 0
    barang_menipis_count = 0
    nomor = 1  # Counter manual
    
    # Buat tabel barang menipis
    for barang in barang_menipis:
        status = hitung_status(barang["Stock"])
        tabel_data.append([
            nomor,
            barang["Kode Barang"],
            barang["Nama Barang"],
            barang["Kategori"],
            barang["Stock"],
            status
        ])
        total_stock_menipis += barang["Stock"]
        
        # Hitung kategori barang
        if barang["Stock"] == 0:
            barang_habis += 1
        elif barang["Stock"] <= 10:
            barang_menipis_count += 1
        
        nomor += 1  # Naikkan counter
    
    headers = ["NO", "KODE BARANG", "NAMA BARANG", "KATEGORI", "STOCK", "STATUS"]
    print(f"\n⚠️  DAFTAR BARANG YANG PERLU PERHATIAN (≤ 10 pcs):")
    print(tabulate(tabel_data, headers=headers, tablefmt="rounded_grid"))
    
    # Tampilkan statistik detail
    print(f"\n📊 STATISTIK DETAIL:")
    print(f"   • Total barang yang perlu perhatian: {len(barang_menipis)}")
    print(f"   • Barang habis (stok 0): {barang_habis}")
    print(f"   • Barang stok menipis (1-10): {barang_menipis_count}")
    print(f"   • Total stok yang perlu restock: {total_stock_menipis} pcs")
    
    # Rekomendasi berbeda berdasarkan kondisi
    print("\n💡 REKOMENDASI:")
    if barang_habis > 0:
        print(f"   • Segera restock {barang_habis} barang yang sudah HABIS")
    if barang_menipis_count > 0:
        print(f"   • Prioritaskan restock {barang_menipis_count} barang dengan stok ≤ 10")
    print("   • Periksa dan update stok secara berkala")

# --------------------------------------------
#           FUNGSI LAPORAN STATISTIK
# --------------------------------------------

def menu_laporan_statistik(): #Menampilkan laporan statistik gudang
    clear_screen()
    garis()
    print("📊 LAPORAN STATISTIK GUDANG")
    garis()
    
    if len(inventory) == 0:
        print("Belum ada data barang.")
        return
    
    # Hitung statistik dasar
    total_barang = len(inventory)
    total_stock = 0
    barang_habis = 0
    barang_menipis = 0
    
    for barang in inventory:
        total_stock += barang["Stock"]
        if barang["Stock"] == 0:
            barang_habis += 1
        elif barang["Stock"] <= 10:
            barang_menipis += 1
    
    # Hitung distribusi per kategori
    kategori_data = {}
    for barang in inventory:
        kategori = barang["Kategori"]
        if kategori not in kategori_data:
            kategori_data[kategori] = {"jumlah": 0, "stock": 0}
        kategori_data[kategori]["jumlah"] += 1
        kategori_data[kategori]["stock"] += barang["Stock"]
    
    # laporan overview
    print(f"\n📈 OVERVIEW GUDANG:")
    print(f"   Total jenis barang  : {total_barang}")
    print(f"   Total semua stock   : {total_stock} pcs")
    
    # Tampilkan status stok
    print(f"\n📊 STATUS STOK:")
    print(f"   Barang habis (stok 0)      : {barang_habis}")
    print(f"   Barang stok menipis (≤10)  : {barang_menipis}")
    print(f"   Barang stok aman (>10)     : {total_barang - barang_habis - barang_menipis}")
    
    # tampilkan distribusi per kategori
    print(f"\n📊 DISTRIBUSI PER KATEGORI:")
    for kategori in kategori_list:
        if kategori in kategori_data:
            data = kategori_data[kategori]
            print(f"   {kategori:12} : {data['jumlah']:2} jenis ({data['stock']:4} pcs)")
        else:
            print(f"   {kategori:12} :  0 jenis (   0 pcs)")
    
    # mengurutkan dari terkecil ke terbesar
    sorted_barang = sorted(inventory, key=lambda x: x["Stock"])
    
    print(f"\n🏆 TOP 3 BARANG STOK TERBANYAK:")
    
    # mengambil 3 terakhir (yang terbesar) dalam urutan terbalik
    jumlah_tampil = min(3, len(sorted_barang))
    for i in range(jumlah_tampil):
        barang = sorted_barang[-(i+1)]
        nomor = i + 1
        print(f"   {nomor}. {barang['Nama Barang']:20} : {barang['Stock']:4} pcs ({barang['Kategori']})")

# --------------------------------------------
#               MENU UTAMA
# --------------------------------------------

def main_menu(): # Menu utama sistem manajemen gudang
    while True:
        clear_screen()
        print("\n" + "="*60)
        print("             🏪 SISTEM MANAJEMEN GUDANG LYVA")
        print("="*60)
        
        # Tampilkan informasi statistik awal
        total_stock = sum(barang["Stock"] for barang in inventory)
        print(f"\n DATA AWAL BARANG: {len(inventory)} barang, {total_stock} pcs total stock")
        
        # Tampilkan peringatan jika ada barang perlu restock
        perlu_restock = hitung_perlu_restock()
        if perlu_restock > 0:
            print(f" ⚠️  PERINGATAN: {perlu_restock} barang perlu restock segera!")

        # Tampilkan pilihan menu
        print("\n" + "="*60)
        print("                     MENU UTAMA")
        print("="*60)
        print("1. Lihat Data Barang")
        print("2. Tambah Barang Baru")
        print("3. Ubah Stock Barang")
        print("4. Hapus Barang")
        print("5. Barang yang Harus Restock")
        print("6. Mini Laporan Gudang")
        print("7. Edit Data Barang")
        print("8. Keluar Program")
        print("="*60)
        
        pilihan = input("Pilih menu (1-8): ")
        
        # Proses pilihan menu
        if pilihan == "1":
            menu_lihat_data()
        elif pilihan == "2":
            menu_tambah_barang()
            input("\nTekan ENTER untuk melanjutkan...")
        elif pilihan == "3":
            menu_ubah_stock()
            input("\nTekan ENTER untuk melanjutkan...")
        elif pilihan == "4":
            menu_hapus_barang()
            input("\nTekan ENTER untuk melanjutkan...")
        elif pilihan == "5":
            menu_peringatan_stok()
            input("\nTekan ENTER untuk melanjutkan...")
        elif pilihan == "6":
            menu_laporan_statistik()
            input("\nTekan ENTER untuk melanjutkan...")
        elif pilihan == "7":
            edit_data_barang()
        elif pilihan == "8":
            print("\n" + "="*60)
            print("             Program Selesai! Terimakasih")
            print("="*60)
            break
        else:
            print("Pilihan tidak valid!")
            input("\nTekan ENTER untuk melanjutkan...")

# --------------------------------------------
#               PROGRAM UTAMA
# --------------------------------------------

if __name__ == "__main__":                                     
    # running login terlebih dahulu
    if login():
        # Jika login berhasil, menjalankan menu utama
        main_menu()