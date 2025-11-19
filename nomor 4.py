# 1. Menerima input username
username = input("Masukkan username: ")

# 2–7. Mengecek syarat menggunakan if–elif–else
if len(username) < 5:
    print("Username tidak valid: minimal 5 karakter.")
elif " " in username:
    print("Username tidak valid: tidak boleh mengandung spasi.")
elif not username[0].isalpha():
    print("Username tidak valid: karakter pertama harus huruf.")
else:
    print("Username valid.")
    