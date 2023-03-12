#diskon
print("=======================")
hargaBaju = int(input("masukkan harga baju"))

Total_Harga = hargaBaju
potongan_Harga = 0

if hargaBaju > 100000 :
    potongan_Harga = hargaBaju * 10/100
    Total_Harga = hargaBaju-potongan_Harga

print("nilai pembayaran anda adalah =", Total_Harga)
print("nilai discount yang diperoleh =", potongan_Harga)