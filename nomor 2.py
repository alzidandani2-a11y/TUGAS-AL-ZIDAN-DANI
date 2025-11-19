# 1. Menerima input jumlah item belanja
jumlah_item = int(input("Masukkan jumlah item belanja: "))

# 2 & 3. Input harga tiap item dan simpan ke dalam list
harga_list = []
for i in range(jumlah_item):
    harga = int(input(f"Masukkan harga item ke-{i+1}: "))
    harga_list.append(harga)

# Tampilkan list harga (opsional)
print("Daftar harga:", harga_list)

# Hitung total
total = sum(harga_list)

# 4. Cek diskon
if total >= 300000:
    total_akhir = total * 0.9   # diskon 10%
else:
    total_akhir = total

# 5. Tampilkan total akhir
print("Total akhir:", int(total_akhir))