
from datetime import date
from turtle import end_fill


print("Masukkan Tanggal mulai!")
tahunmulaidata = raw_input("Tahun :");
print("Tahun Mulai : ", tahunmulaidata)
tahunmulai=int(tahunmulaidata);

bulanmulaidata = input("Bulan :");
print("Bulan Mulai  : ", bulanmulaidata)
bulanmulai=int(bulanmulaidata);


tanggalmulaidata = raw_input("Tanggal :");
print("Tanggal  Mulai  : ", tanggalmulaidata)
tanggalmulai=int(tanggalmulaidata);


print("Masukkan Tanggal selesai!")
tahunselesaidata = raw_input("Tahun :");
print("Tahun selesai: ", tahunselesaidata)
tahunselesai=int(tahunselesaidata);

bulanselesaidata = raw_input("Bulan :");
print("Bulan selesai: ", bulanselesaidata)
bulanselesai=int(bulanselesaidata);

tanggalselesaidata = raw_input("Tanggal :");
print("Tanggal selesai: ", tanggalselesaidata)
tanggalselesai=int(tanggalselesaidata);

f_date = date(tahunmulai, bulanmulai, tanggalmulai)
l_date = date(tahunselesai, bulanselesai, tanggalselesai)
delta = l_date - f_date
print("Result : ",delta.days," Day : ")