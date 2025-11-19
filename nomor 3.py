# 1. Menerima input berupa 5 angka dari user
angka_list = []
for i in range(5):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)

# 2. List sudah tersimpan di angka_list
print("Data angka:", angka_list)

# 3. Hitung jumlah genap dan ganjil
jumlah_genap = 0
jumlah_ganjil = 0

for angka in angka_list:
    if angka % 2 == 0:
        jumlah_genap += 1
    else:
        jumlah_ganjil += 1

# Tampilkan hasil
print("Jumlah angka genap :", jumlah_genap)
print("Jumlah angka ganjil:", jumlah_ganjil)