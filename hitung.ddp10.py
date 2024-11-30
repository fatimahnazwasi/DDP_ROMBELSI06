import math

def pertambahan(bil1, bil2):
    hasil = bil1 + bil2
    print('hasil pertambahan dari', bil1, "+", bil2, "=", hasil)

def pengurangan(bil1, bil2):
    hasil = bil1 - bil2
    print('hasil pengurangan dari', bil1, "-", bil2, "=", hasil)

def perkalian(bil1, bil2):
    hasil = bil1 * bil2
    print('hasil perkalian dari', bil1, "*", bil2, "=", hasil)

def pembagian(bil1, bil2):
    hasil = bil1 / bil2
    print('hasil pembagian dari', bil1, "/", bil2, "=", hasil)

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)