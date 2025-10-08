
list_kosong = []
list_buah = ['pisang', 'nanas', 'melon', 'durian']
list_nilai = [80, 70, 90 , 60]
list_jawaban = [150, 33, 'presiden sukarno', False]
print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
print(list_buah[2:4])
# ubah data pertama 
list_buah[0] = 'jeruk'
# ubah data terakhir
list_buah[-1] = 'mangga'
# ubah data dalam range
list_buah[1:3] = ['naga', 'pepaya']
print(list_buah)
# tambah data di belakang list
list_buah.append('sirsak')
print(list_buah)
#tambah data di awal
list_buah.insert(0, 'jambu')
# tambah data di indek manapun dalam list
list_buah.insert(2, 'manggis')
print(list_buah)
print(list_nilai[0:1])
print(list_nilai[0:2])
print(list_nilai[1:3])
print(list_nilai[2:4])