inputan_user = input("Mendatar/Menurun?: ")

if (inputan_user == "Mendatar"):
    kolom = int(input("Masukkan kolom: "))
    print("#" * kolom)
elif (inputan_user == "Menurun"):
    baris = int(input("Masukkan baris: "))
    print("* \n" * baris)
else:
    print("Pola tidak dikenali")