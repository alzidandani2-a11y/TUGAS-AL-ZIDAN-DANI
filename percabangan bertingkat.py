nilai = int(input('masukkan nilai: '))
usia = int(input('masukkan usia: '))

if nilai >= 75:
    if(usia< 15):
        print('selamat adek, kamu lulus!')
    else:
      print('selamat kakak, kamu lulus!')
else:
    if (usia< 15):
        print('mohon maaf dek, coba lagi ya!')
    else:
        print('mohon maaf kak, coba lagi ya!')
