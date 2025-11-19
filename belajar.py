# Program kategori nilai mahasiswa

# 1. Menerima input list nilai mahasiswa (dipisahkan dengan koma)
data = input("Masukkan nilai (pisahkan dengan koma): ")

# 2. Ubah input menjadi list integer
nilai_list = [int(n.strip()) for n in data.split(",")]

# 3. Tampilkan kategori setiap nilai
for n in nilai_list:
    if n >= 85:
        kategori = "A"
    elif 70 <= n <= 84:
        kategori = "B"
    elif 55 <= n <= 69:
        kategori = "C"
    else:
        kategori = "D"
    print(f"Nilai {n} → Kategori {kategori}")
        