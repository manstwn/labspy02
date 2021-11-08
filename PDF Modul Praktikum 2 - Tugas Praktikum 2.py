#Program Menampilkan Bilangan Terbesar

#Input Bilangan
num1 = int(input("Masukan angka ke-1: "))
num2 = int(input("Masukan angka ke-2: "))
num3 = int(input("Masukan angka ke-3: "))

#Proses dan Output
if num1 > num2 and num1 > num3:
    print("Bilangan Terbesar Adalah :",num1)
elif num2 > num1 and num2 > num3:
    print("Bilangan Terbesar Adalah :", num2)
else:
    print("Bilangan Terbesar Adalah :", num3)
