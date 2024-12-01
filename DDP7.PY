print("Soal nomor 1")

def celcuis_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32 )
celcuis_ke_fahrenheit(0)

print("Soal nomor 2")

def is_genap(genap):
    print(genap %2 == 0)

is_genap(4)
is_genap(5)

print("Soal nomor 3")
# rata" nilai kelulusan 70
def skor(nilai):
    if nilai >=70:
        print("Lulus")
    else:
        print("gagal") 
skor(50)
skor(90)

print("Soal nomor 4")
def bil_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end= " ")
bil_ganjil(20)        






