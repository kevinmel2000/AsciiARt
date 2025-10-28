import os

def saveProcess(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi,users):
    masukanfolder = input("Masukkan nama folder:")
    
    print("Saving...")

    if not os.path.exists('save'):
        os.makedirs('save')
        print("Membuat folder save...")

    path = "save/"+masukanfolder

    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print("Membuat folder ",path,"...")

    fileuser = open(path+"/user.csv", "w")

    lenUserData=len(users)
    for i in range(0,lenUserData):
        listUser=users[i]
        fileuser.write(listUser[0]+";"+listUser[1]+";"+listUser[2]+"\n")

    fileuser.close()

    filecandi = open(path+"/candi.csv", "w")

    lenCandiData=len(candi)
    for i in range(0,lenCandiData):
        listCandi=candi[i]
        filecandi.write(str(listCandi[0])+";"+listCandi[1]+";"+str(listCandi[2])+";"+str(listCandi[3])+";"+str(listCandi[4])+"\n")

    filecandi.close()

    fileBahan = open(path+"/bahan_bangunan.csv", "w")

    lenBahanData=len(bahan_bangunan)
    for i in range(0,lenBahanData):
        listBahan=bahan_bangunan[i]
        if listBahan[0]=='pasir':
            fileBahan.write(listBahan[0]+";"+listBahan[1]+";"+str(jumlahpasir)+"\n")
        elif listBahan[0]=='batu':
            fileBahan.write(listBahan[0]+";"+listBahan[1]+";"+str(jumlahbatu)+"\n")
        elif listBahan[0]=='air':
            fileBahan.write(listBahan[0]+";"+listBahan[1]+";"+str(jumlahair)+"\n")

    fileBahan.close()

    print("Berhasil menyimpan data di folder ",path,"!")