

print("Masukkan Titik Origin ")
originxdata = input("Masukkan Titik origin X :");
print("Nilai origin X: ", originxdata)
originx=int(originxdata); 


originydata = input("Masukkan Titik origin Y :");
print("Nilai origin Y: ", originydata)
originy=int(originydata); 


print("Masukkan Titik Kordinat ")
kordinatxdata = input("Masukkan Titik Kordinat X :");
print("Nilai Kordinat X: ", kordinatxdata)
kordinatx=int(kordinatxdata); 


print("Masukkan Titik Kordinat ")
kordinatydata = input("Masukkan Titik Kordinat Y :");
print("Nilai Kordinat Y: ", kordinatydata)
kordinaty=int(kordinatydata); 



if kordinatx > originx and kordinaty > originy :
    print("Lokasi Beradi Di Kuadran I")
elif kordinatx < originx and kordinaty > originy:
    print("Lokasi Beradi Di Kuadran II")
elif kordinatx < originx and kordinaty < originy:
    print("Lokasi Beradi Di Kuadran III")
elif kordinatx > originx and kordinaty < originy:
    print("Lokasi Beradi Di Kuadran IV")

