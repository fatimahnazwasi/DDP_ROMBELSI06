#Soal nomor 1
angka= int(input("Masukkan bilangan bulat:"))

if angka % 2 ==0:
    print("Bilangan genap")
elif angka % 2!=0:
    print("Bilangan ganjil")
else:
    print("input tidak valid")

    #Soal nomor 2
nilaiujian = int(input("Masukkan nilai ujian"))
    
if nilaiujian  >=75:
     print("Lulus")
else:
     print("Tidak Lulus")

     #Soal Nomor 3

usia= int(input("Masukkan usia Anda")) 
if usia >= 18:
        print("Dewasa")
elif usia < 18 and usia > 13:
    print("Remaja")
else:
    print("Anak - anak")

    #Soal nomor 4 

Status= input("Masukkan status anggota:").lower()

if Status == "gold" or Status == "silver":
    print("Selamat Anda Mendapatkan Diskon")
elif Status == "bronze": 
    print("Maaf Anda Tidak Mendapat Diskon")
else:
    print("Input tidak valid") 

    #soal nmr 5
jumlah_pembelian= int(input("Masukkan jumlah pembelian:")) 

total_harga= jumlah_pembelian *  0,9 if jumlah_pembelian > 100 else jumlah_pembelian

print(f"Total harga setelah diskon: {total_harga}" if
     jumlah_pembelian >100 else f"Total harga tanpa diskon: {total_harga}" ) 
                        
    
    
     



       

    