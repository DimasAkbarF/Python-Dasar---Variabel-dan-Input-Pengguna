# Program untuk memahami variabel dan input di Python

# Mendeklarasikan variabel
nama = "Dimas"
umur = 20

# Menampilkan nilai variabel
print("Nama:", nama)
print("Umur:", umur)

# Mengambil input dari pengguna
nama_pengguna = input("Masukkan nama Anda: ")
umur_pengguna = input("Masukkan umur Anda: ")

# Menampilkan hasil input
print("Nama Anda adalah", nama_pengguna)
print("Umur Anda adalah", umur_pengguna)

# Menggunakan input dalam perhitungan
tahun_lahir = 2024 - int(umur_pengguna)
print("Tahun kelahiran Anda adalah", tahun_lahir)