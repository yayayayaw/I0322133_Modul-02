nama =[]
alamat=[]
notelp=[]

jawab = input("apakah anda akan menambahkan data base lagi?")

while jawab == "ya" :
    print("===========welkam=============")
    namabaru = input('nama konsumen adalah:')
    nama.append(namabaru)
    alamatbaru = input('alamat konsumen adalah:')
    alamat.append(alamatbaru)
    notelpbaru = int(input('nomor telepon konsumen adalah:'))
    notelp.append(notelpbaru)

    for i in range(0,len(nama)):
        print("no", i+1, "!!nama:",nama[i], "!!alamat:",alamat[i], "!!notelp:", notelp[i])
    jawab = input("apakah anda akan menambahkan data base lagi?")
print('=======trims=========')