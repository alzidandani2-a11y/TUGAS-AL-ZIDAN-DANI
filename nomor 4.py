def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol"
    return a / b

print("Pilih operasi:")
print("1. Tambah\n2. Kurang\n3. Kali\n4. Bagi")

pilih = input("Masukkan pilihan (1-4): ")
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilih == "1":
    print("Hasil:", tambah(a, b))
elif pilih == "2":
    print("Hasil:", kurang(a, b))
elif pilih == "3":
    print("Hasil:", kali(a, b))
elif pilih == "4":
    print("Hasil:", bagi(a, b))
else:
    print("Pilihan tidak valid")