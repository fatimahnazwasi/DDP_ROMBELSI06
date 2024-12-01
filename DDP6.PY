#deklarsi fungsi hello

def hello():
    print("Hello, Saya Mahasiswa STT NF")
    print("Saya dari prodi Sistem informasi")


#panggil fungsi hello
hello()

def cetak(kata):
    print(kata)

cetak("hello world") 
cetak("saya prodi informatika")
cetak(1+2)  

def biodata(nama, alamat, umur):
    cetak("hello nama saya " +nama)
    cetak("alamat saya di "+alamat)
    cetak("umur saya " + str(umur))

biodata("nazwa", "padang",  "18 tahun" )

def perkalian(angka1, angka2,):
    cetak(angka1*angka2)
perkalian(4,5) 

def pangkat(angka1, angka2):
    cetak(angka1**angka2)
pangkat(2, 4) 

def fungsi1(x):
    return x*x

def fungsi2(y):
    return y**y

cetak(fungsi1(3)+fungsi2(4))