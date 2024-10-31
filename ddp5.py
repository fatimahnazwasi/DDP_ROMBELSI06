#Soal nmr 1
kendaraan= ["Beat Deluxe, sepeda motor, 110, silver, 2"]
print(kendaraan)

#Tambahkan dari list tersebut di belakang dengan value : harga kendaraan, tipe kendaraan
kendaraan.append(19.300000)
kendaraan.append("matic")
print(kendaraan)

#tambahkan setelah jenis kendaraan dengan value[merk kendaraan]
kendaraan.insert(2, "honda")
print(kendaraan)

print("========================")

#Soal nmr 2
pilih = int(input("""Selamat datang di aplikasi menghitung
1. untuk menghitung luas persegi                  
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga

masukkan pilihan anda : """))

match pilih: 
    case 1:
     print("kamu memilih 1 untuk menghitung luas persegi")
     sisi = int(input("masukkan sisi persegi:"))
     luaspsg = sisi * sisi
     print("luas persegi  yang sisinya",sisi,"adalah",luaspsg) 

    case 2: 
      print("kamu memilih 2 untuk menghitung luas lingkaran")
      jari_jari = int(input("masukkan jari-jari:"))
      luaslkrn = 3.14 * jari_jari * jari_jari
      print("luas lingkaran  yang jari-jarinya",jari_jari,"adalah",luaslkrn) 

    case 3: 
     print("kamu memilih 3 untuk menghitung luas segitiga")
     alas = int(input("masukkan alas segitiga:"))
     tinggi =int(input("masukkan tinggi segitiga:"))
     luas_segitiga = 0.5 * alas * tinggi
     print("luas segitiga dengan alas",alas,"dan tinggi ",tinggi,"adalah",luas_segitiga ) 

    case _:
      print("Anda salah pilih")

