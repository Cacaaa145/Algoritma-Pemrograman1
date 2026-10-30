print(1)
kendaraan = ['Motor','Mobil','Sepeda','Bus']
print(f"Data kendaraan awal = \n {kendaraan}")
print("a. Tambah Truk di akhir list")
kendaraan.append ("Truk")
print(f"Data kendaraan a = \n {kendaraan}")
print("b. Sisipkan becak di index 1")
kendaraan.insert(1,'Becak')
print(f"Data kendaraan b = \n {kendaraan}")
print("c.Hapus data yang di akhir list")
kendaraan.pop()
print(f"Data kendaraan c = \n {kendaraan}")
print("d. Ubah elemen sepeda menjadi skuter")
kendaraan[2] = "Skuter"
print(f"Data kendaraan d = \n {kendaraan}")
jumlah_data = len(kendaraan)
print(f"Jumlah kendaraan ada {jumlah_data}\n")
print(2)
angka = [75,80,90,75,85,100,65]
print("a. Index skor 100")
index_100 = angka.index (100)
print(f"100 berada di index {index_100}")
print("b. Banyak siswa skor 75")
skor_75 = angka.count(75)
print(f"Siswa yang mendapatkan skor 75 ada {skor_75} anak")
print("c. Skor nilai terkecil sampai terbesar")
angka.sort()
print(f"Data yang sudah terurut {angka}")
print("d. Balikkan urutan list yang sudah di urutkan")
angka.reverse()
print(f"Data terurut yang dibalik {angka}\n")
print(3)
menu_utama = ["Nasi Goreng","Mie Ayam"]
menu_tambahan = ["Kerupuk","Es Teh"]
print(f"Menu utama = {menu_utama}")
print(f"Menu tambahan = {menu_tambahan}")
menu_utama.extend(menu_tambahan)
print(f"Menu terbaru yaitu {menu_utama}\n")
print(4)
barang1 = ["Buku",5000]
barang2 = ["Pensil",2000]
barang3 = ["Penggaris",3000]
data_barang = [["Buku",5000],["Pensil",2000],["Penggaris",3000]]
print("a. Tampilkan harga Pensil")
print(data_barang[1][1])
print("b. Gunakan perulangan")
print(f"Data barang {data_barang}")
for barang in data_barang:
    print(f"Nama\t : {barang[0]}")
    print(f"Harga\t : {barang[1]}\n")