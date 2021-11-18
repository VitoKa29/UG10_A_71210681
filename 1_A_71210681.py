ug = float(input("Masukan nilai rata-rata UG anda : "))
tts = float(input("Masukan nilai TTS anda : "))
tas = float(input("Masukan nilai TAS anda : "))
print("=========================")

total_ug = (70/100) * ug
total_tts = (15/100) * tts
total_tas = (15/100) * tas
nilai = total_tas + total_tts + total_ug



if (ug < 0 or tts < 0 or tas < 0):
    print("Maaf, nilai tidak boleh kurang dari 0")
else:
    print("Nilai anda:", nilai)
    if(nilai < 45):
        print("Nilai huruf anda: E")
    elif(nilai < 55):
        print("Nilai huruf anda: D")
    elif(nilai < 60):
        print("Nilai huruf anda: C")
    elif(nilai < 65):
        print("Nilai huruf anda: C+")
    elif(nilai < 70):
        print("Nilai huruf anda: B-")
    elif(nilai < 75):
        print("Nilai huruf anda: B")
    elif(nilai < 80):
        print("Nilai huruf anda: B+")
    elif(nilai < 85):
        print("Nilai huruf anda: A-")
    else:
        print("Nilai huruf anda: A")