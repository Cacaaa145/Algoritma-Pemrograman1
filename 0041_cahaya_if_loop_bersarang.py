print("---Nested If---") 
print() 
status_kartu_ATM = "aktif"
saldo = 10000000
nominal_tarik = 760000
if status_kartu_ATM == "aktif":     
    if nominal_tarik <= saldo:         
        if nominal_tarik >= 100000:             
            saldo = saldo - nominal_tarik             
            print(f"Penarikan berhasil: Rp{nominal_tarik:,}")
            print(f"Sisa saldo: Rp{saldo:,} ")
        else:             
            print("Gagal: Penarikan minimal Rp100,000. ")     
    else:         
        print("Gagal: Saldo tidak mencukupi.") 
else:     
    print("Akses ditolak: Akun sedang terblokir.") 
print()
print("---Nested While---")
print("Contoh 1")
i = 5 
while i <= 7: 
    j = 6 
    while j <= 7: 
        print("Teknologi Informasi") 
        j += 1 
    print("Kosong\n")  
    i += 1 
print()
print("---Nested While---")
print("Contoh 2")
i = 5
N = 7
while i <= 8:
    j = 4
    while j <= 8:
        print(N)
        N = N + 1
        j += 1
    i += 1 
print()
print("Nested For")
for i in range(1, 6):          
    for j in range(1, 5):      
        print(f"[{i},{j}]", end=" ") 
    print()  # Pindah baris 
print()
print("---For in While---")
sesi = 1
while sesi <= 4: 
    print(f"Sesi ke-{sesi}:") 
    for antrean in range(1, 6):
        print(f"Mengerjakan soal nomor : {antrean}") 
    sesi += 1
    print("---") 
print()