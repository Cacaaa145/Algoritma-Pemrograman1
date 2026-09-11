#Program Usia User, lalu di kategori
usia = int(input("Usia anda : "))
if usia <= 12 :
    print("Anak-anak")
elif 13 <= usia <= 17 :
    print("Remaja")
elif 18 <= usia <= 59 :
    print("Dewasa")
else :
    print("Lansia")
print()