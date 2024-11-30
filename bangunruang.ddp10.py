import math

def l_kubus(sisi,):
    luas = 6 * sisi * sisi
    volume = sisi * sisi * sisi
    print(f'Luas kubus adalah {6} * {sisi} * {sisi} = {luas}')
    print(f'volume kubus adalah {volume}')
    
def l_balok(panjang, lebar, tinggi):
    luas = 2 * (panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)
    volume = panjang * lebar * tinggi
    print(f'hasil luas balok adalah {2} * {panjang * lebar} + {panjang * tinggi} + {lebar * tinggi} = {luas}')
    print(f'volume balok adalah {volume}')

def l_prisma(luas_alas, keliling_alas, tinggi):
    luas = 2 * (luas_alas) + (keliling_alas * tinggi)
    volume = luas_alas * tinggi
    print(f'hasil luas prisma adalah {2} * {luas_alas} + {keliling_alas * tinggi} = {luas}')
    print(f'volume prisma adalah {volume}')

def l_tabung(phi, jari2, tinggi,):
    luas = 2 * phi * jari2 * (tinggi + jari2)
    volume = phi * jari2 * jari2 * tinggi
    print(f'hasil luas tabung adalah {2} * {phi} * {jari2} * {tinggi + jari2} = {luas}')
    print(f'volume tabung adalah {volume}')

def l_kerucut(phi, jari2, garpe, tinggi):
    luas = phi * jari2 * (jari2 + garpe)
    volume = 1/3 * phi * jari2 * jari2 * tinggi 
    print(f'hasil luas kerucut adalah {phi} * {jari2} * {jari2 + garpe} = {luas}')
    print(f'volume kerucut adalah {volume}')   
     
    
