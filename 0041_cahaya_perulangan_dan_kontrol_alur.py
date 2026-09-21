print("Latihan Perulangan dan Kontrol Alur")
print()
print("Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan!")
angka = 1
while angka <= 50 : 
    if angka % 2 == 0 :
        print(f"Angka {angka} adalah bilangan genap")
    else:
        print(f"Angka {angka} adalah bilangan ganjil")
    angka += 1
print("\nEnd Program")
print()
print("Buat program yang menampilkan bilangan prima dari 1-100")
for angka in range(1, 101):
    pembagi = 0
    for i in range(1,101) :
        if angka % i == 0:
            pembagi += 1
    if pembagi == 2:
        print(f"Angka {angka} adalah bilangan prima")
    else : 
        print(f"Angka {angka} bukan bilangan prima")
print("\nEnd Program")
print()
