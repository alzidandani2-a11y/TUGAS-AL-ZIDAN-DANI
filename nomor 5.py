nama_list = ["zidan, maylan"]
while True:
    print("\n=== MENU ===")
    print("1. Tambah nama")
    print("2. Hapus nama")
    print("3. Tampilkan semua nama")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1"
        nama = input("Masukkan nama yang ingin ditambahkan: ")
        nama_list.append(nama)
        print(f"Nama '{nama}' berhasil ditambahkan.")

    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in nama_list:
            nama_list.remove(nama)
            print(f"Nama '{nama}' berhasil dihapus.")
        else:
            print(f"Nama '{nama}' tidak ditemukan.")

    elif pilihan == "3":
        if len(nama_list) == 0:
            print("Belum ada nama yang tersimpan.")
        else:
            print("\nDaftar nama:")
            for n in nama_list:
                print("-", n)

    elif pilihan == "4":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid! Coba lagi.")