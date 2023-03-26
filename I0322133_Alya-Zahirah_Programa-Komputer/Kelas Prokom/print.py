print ("==============================================")
kelas = ["Ali", "Budi", "Caca", "Dinda", "Elo" ]
kelas.append("Kala")
kelas.append("Lulu")
kelas.insert(1,"bandi")
kelas.remove("Ali")

pertanyaan = str(input("Apakah anda menambahkan data baru?"))
if pertanyaan == "Ya":
    data = str(input("Masukkan data"))
    kelas.append(data)
    for i in range(0,len(kelas)):
        print("no mahasiswa", i+1, "nama =", kelas[i])

else:
    for i in range(0,len(kelas)):
        print("no mahasiswa", i+1, "nama =", kelas[i])


