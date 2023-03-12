#tugas membuat daftar gaji

print("====================")
nama = str(input("Nama karyawan = "))
KelJamKerja = float(input("Besar kelebihan jam kerja = "))
golongan = int(input("golongan karyawan = "))
gajipokok = golongan * 2000000
lembur = KelJamKerja * 500000
pendapatan = gajipokok + lembur
print("====================")
print("nama karyawan = ", nama)
print("golongan = ", golongan)
print("gaji pokok = ", gajipokok)
print("uang lembur = ", lembur)
print("gaji bersih = ", pendapatan)
print("====================")