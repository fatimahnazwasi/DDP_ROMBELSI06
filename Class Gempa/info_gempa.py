from Gempa import *

# Membuat objek dengan Lokasi dan Skala
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)





# info gempa
print("info gempa bumi")
print()
gempa1.dampak() # Memanggil Method dampak()

print("info gempa bumi")
print()
gempa2.dampak()

print("info gempa bumi")
print()
gempa3.dampak()

print("info gempa bumi")
print()
gempa4.dampak()

print("info gempa bumi")
print()
gempa5.dampak()





