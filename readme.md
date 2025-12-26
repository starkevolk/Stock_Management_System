SISTEM MANAJEMEN GUDANG SPORTWEAR (LYVA)

Deskripsi:
Program berbasis Python untuk mengelola data stok barang sportwear di gudang.
Sistem ini dibuat untuk kebutuhan pembelajaran CRUD dan manajemen inventory.

Fitur Utama:
- Login user (admin & staff & owner)
- Lihat data barang (semua, per kategori, per rak, cari kode)
- Tambah barang baru
- Ubah stok barang
- Edit data barang (khusus admin)
- Hapus barang (khusus admin)
- Peringatan stok menipis & habis
- Mini laporan statistik gudang


Akun Login (Dummy):
- admin  | password: admin1234
- staff  | password: staff1234
- owner  | password: febriani

Struktur Data:
Inventory disimpan dalam bentuk list of dictionary dengan field:
- Kode Rak
- Kode Barang
- Nama Barang
- Kategori (Top, Bottom, Accessories)
- Stock

Aturan Kode:
- Top        : 11xxx (Rak TP01–TP03)
- Bottom     : 21xxx (Rak BT01–BT03)
- Accessories: 31xxx (Rak AS01–AS03)

Status Stok:
- 0            : HABIS
- 1–10         : SANGAT MENIPIS
- 11–20        : MENIPIS
- 21–150       : AMAN
- >150         : OVERLOAD

Cara Menjalankan Program:
1. Pastikan Python sudah terinstall
2. Install library tabulate (jika belum):
   pip install tabulate
3. Jalankan file:
   python stock_gudang_lyva.py

🎮 Panduan Penggunaan
1. Login Sistem
- Jalankan program dan masukkan username & password
- Maksimal 3 kali percobaan login

2. Menu Utama
Setelah login berhasil, tersedia 8 opsi menu:
   1. Lihat Data Barang - Tampilkan data dengan berbagai filter
   2. Tambah Barang Baru - Input data barang baru
   3. Ubah Stock Barang - Update jumlah stock
   4. Hapus Barang - Hapus barang dari inventory (admin only)
   5. Barang yang Harus Restock - Lihat barang dengan stok ≤10
   6. Mini Laporan Gudang - Statistik dan analisis
   7. Edit Data Barang - Edit detail barang (admin only)
   8. Keluar Program - Keluar dari sistem

3. Fitur Khusus Admin
   - Menu Edit Data Barang: Edit semua field termasuk kode rak dan kategori
   - Menu Hapus Barang: Hapus barang berdasarkan kategori atau rak
   - Akses penuh ke semua operasi

🔒 Keamanan dan Validasi
   - Login System: Autentikasi dengan username dan password
   - Input Validation: Validasi angka, format kode, dan pilihan menu
   - Confirmation Dialog: Konfirmasi untuk aksi kritis (hapus, edit)
   - unique Code Check: Validasi keunikan kode barang

📁 Data Awal
Program ini menggunakan data dummy 15 data dummy barang sportwear yang mencakup 3 kategori dan belum terhubung ke database.
   Top: Atasan, Jaket (5 barang)
   Bottom: Legging, Kulot, Rok (5 barang)
   Accessories: Hijab, Belt, Inner, Cap (5 barang)

⚠️ Catatan Penting
- Backup Data: Program menyimpan data di memori selama runtime
- Exit Program: Data tidak disimpan permanen (kecuali diimplementasikan fitur save/load)
- Case Sensitivity: Input username dan password bersifat case-sensitive
- Cancel Feature: Ketik "batal" untuk membatalkan operasi input


Pembuat:
Madina Febriani
