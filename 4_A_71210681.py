artikel = input("Masukkan artikel yang ingin dipindai: ")
klub = input("Masukkan nama klub favorit anda: ")
skor = input("Masukkan skor yang ingin dicari: ")

cek_klub = klub in artikel
cek_skor = skor in artikel

if(cek_klub and cek_skor):
    print("Hasil pencarian ditemukan")
elif(cek_klub and not cek_skor):
    print("Hanya kata",klub,"yang ditemukan pada artikel ini")
elif(not cek_klub and cek_skor):
    print("Hanya skor",skor,"yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian",klub,"dan",skor,"tidak ditemukan")