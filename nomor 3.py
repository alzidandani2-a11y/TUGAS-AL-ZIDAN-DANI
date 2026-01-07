def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    total_jam = 0
    for _ in range(hari_kerja):
        if jam_kerja_per_hari > 8:
            lembur = jam_kerja_per_hari - 8
            total_jam += 8 + (lembur * 1.5)
        else:
            total_jam += jam_kerja_per_hari
    return total_jam * tarif_per_jam

tarif = float(input("Tarif per jam: "))
jam = int(input("Jam kerja per hari: "))
hari = int(input("Jumlah hari kerja: "))

gaji = hitung_gaji(tarif, jam, hari)
print("Total gaji bulanan:", gaji)
