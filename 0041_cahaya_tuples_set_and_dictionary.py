print("=== TUPLE ===\n")
print("a. (Nama,NPM,Prodi)")
mahasiswa = ("Caca",2605060041,"Teknologi Informasi")
print(mahasiswa)
print()
print("b. NIM dan Prodi dengan mengakses index")
print(f"NIM\t: {mahasiswa[1]}")
print(f"Prodi\t: {mahasiswa[2]}")
print()
print("c. Jalankan kode mahasiswa[2] = Teknologi Informasi")
#mahasiswa[2] = "Teknologi Informasi"
print("d. Membuat set")
nilai_angka = {10,4,3,2,4,10,7,5}
print(nilai_angka)
print("\n=== Manipulasi Dictionary ===\n")
print("a. Dictionary data_mahasiswa")
data_mahasiswa = {
    "NIM":"240101",
    "Nama":"Budi Santoso",
    "Prodi":"Teknologi Informasi"
}
print(data_mahasiswa)
print("\nb. Ubah nilai prodi menjadi Sastra Mesin dan tambah Angkatan 2026")
data_mahasiswa.update({"Prodi":"Sastra Mesin"})
data_mahasiswa.update({"Angkatan":"2026"})
print(data_mahasiswa)
print("\nc. Hapus data NIM")
del data_mahasiswa["NIM"]
print(data_mahasiswa)
print("\n=== Perulangan pada Dictionary ===")
print("\na. Buat dictionary")
data_hargabuah = {
    "Apel":5000,
    "Pisang":3000,
    "Jeruk":7000,
    "Anggur":15000
}
print(data_hargabuah)
print("\nb.Perulangan untuk menampilkan setiap barang dan harga")
items =data_hargabuah.items()
print(items)
for buah in data_hargabuah.items():
    print(buah)
for buah,harga in data_hargabuah.items():
    print(f"Harga {buah}\t: {harga}")
print("\nc. Menghitung total belanja")
totalbelanja = 0
for nominal in data_hargabuah.items():
    totalbelanja += harga
print(f"Total belanja\t: Rp{totalbelanja}\n")
