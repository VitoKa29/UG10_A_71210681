print("#############################")
print("Kalkulator Advanced Sederhana")
print("#############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

input_user = int(input("Masukkan menu yang anda dipilih: "))

if(input_user == 1):
    bil1 = float(input("Masukkan bilangan yang ingin dibagi: "))
    bil2 = float(input("Masukkan bilangan pembagi: "))
    modulo = bil1 % bil2
    print("Sisa hasil bagi",bil1,"dibagi dengan",bil2,"adalah",modulo)

elif(input_user == 2):
    bil1 = float(input("Masukkan bilangan yang ingin dibagi: "))
    bil2 = float(input("Masukkan bilangan pembagi: "))
    bagi = bil1 // bil2
    print("Hasil pembagian",bil1,"dibagi dengan",bil2,"dibulatkan kebawah adalah",bagi)

elif(input_user == 3):
    bil1 = float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    kubik = bil1 ** (1/3)
    print("Akar kubik dari",bil1,"adalah",kubik)

else:
    print("Menu yang anda pilih tidak tersedia")