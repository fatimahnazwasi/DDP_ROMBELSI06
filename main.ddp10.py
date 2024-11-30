import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas persegi{sisi} * {sisi} = {luas}')
    print(f'Keliling persegi adalah{keliling}')
    
def l_persegi_panjang(panjang,lebar):
    luas = panjang*lebar  
    print(f'luas persegi panjang {panjang} * {lebar} = {luas}') 
    
def l_jajargenjang(alas, tinggi):
   luas = alas*tinggi 
   print(f'luas jajargenjang {alas} * {tinggi} = {luas}') 
   
def l_lingkaran(jari_jari):
   luas = math.pi * (jari_jari ** 2) 
   print(f'luas lingkaran {jari_jari} {jari_jari} = {luas}')
   
def l_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    print(f'Luas Segitiga {0.5} * {alas} * {tinggi} = {luas}')   