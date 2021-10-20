#PROGRAM KONVERSI MATA ASING KE IDR 
print("1. konversi IDR-USD")
print("2. konversi IDR-SGD")
print("3. konversi IDR-EUR")
print("4. konversi IDR-JPY")
mn=int(input("Masukan pilihan konversi="))
if mn==1:
    aString = input("Masukan jumlah USD = $")
    a = int(aString)
    bString = a * 14126
    b = int(bString)
    print("Nilai USD $", a," = Rp",b)
if mn==2:
    aString = input("Masukan jumlah SGD = S$")
    a = int(aString)
    bString = a * 10517
    b = int(bString)
    print("Nilai SGD S$", a," = Rp", b)
if mn==3:
    aString = input("Masukan jumlah EUR = €")
    a = int(aString)
    bString = a * 16460
    b = int(bString)
    print("Nilai EUR €", a," = Rp", b)
if mn==4:
    aString = input("Masukan jumlah JPY = ¥")
    a = int(aString)
    bString = a * 1236
    b = int(bString)
    print("Nilai JPY ¥", a," = Rp", b)