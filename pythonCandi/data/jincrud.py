
from data import candicrud

def summonjin(usersdata,statrole):
    
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")
    nomorjin = int(input("Masukkan nomor jenis jin yang ingin dipanggil:"))
    
    tipejin='jin_pengumpul'
    if nomorjin==1:
        tipejin='jin_pengumpul'
        print("Memilih jin “Pengumpul”.")
    elif nomorjin==2:
        tipejin='jin_pembangun'
        print("Memilih jin “Pembangun”.")
    else :
        print("Tidak ada jenis jin bernomor “,",nomorjin,"”!")
    
    if nomorjin==1 or nomorjin==2 :
        
        statusernamejin=False
        usernamejin = input("Masukkan username jin:")
        
        lenuserdata=len(usersdata);
        
        for i in range(0,lenuserdata):
            usertemp=usersdata[i]
            usernametemp=usertemp[0]
            passwordtemp=usertemp[1]
            roletemp=usertemp[2]

            if usernamejin==usernametemp :
                statusernamejin=True
                print("Username “,usernamejin,” sudah diambil!")
                break;

        if statusernamejin==False:
            passwordjin = input("Masukkan password jin:")
            lenpasswordjin=len(passwordjin)

            if lenpasswordjin<5:
                print("Password panjangnya harus 5-25 karakter!")
            else :

                print("Mengumpulkan sesajen...")
                print("Menyerahkan sesajen...")
                print("Membacakan mantra...")
                print("Jin ",usernamejin," berhasil dipanggil!")

                usertempjin=[usernamejin,passwordjin,tipejin]
                usersdata.append(usertempjin)        
    
    #printlistjin(usersdata)

    return usersdata


def ubahjin(usersdata,statrole):
    usernamejin = input("Masukkan username jin:")
        
    lenuserdata=len(usersdata);
    statusernamejin=False

    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        passwordtemp=usertemp[1]
        roletemp=usertemp[2]

        if usernamejin==usernametemp :
            statusernamejin=True
            
            if roletemp=='jin_pengumpul':
                confirmjin=input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?")
                if confirmjin=='Y':
                    tipejin='jin_pembangun'
                    usertempjin=[usernamejin,passwordtemp,tipejin]
                    usersdata[i]=usertempjin
            
            elif roletemp=='jin_pembangun':
                confirmjin=input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?")
                if confirmjin=='Y':
                    tipejin='jin_pengumpul'
                    usertempjin=[usernamejin,passwordtemp,tipejin]
                    usersdata[i]=usertempjin
            break;

    if statusernamejin==False:
        print("Tidak ada jin dengan username tersebut.")

    printlistjin(usersdata)

    return usersdata


def hapusjin(usersdata,candidata,statrole):
    usernamejin = input("Masukkan username jin:")
        
    lenuserdata=len(usersdata);
    statusernamejin=False

    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        passwordtemp=usertemp[1]
        roletemp=usertemp[2]

        if usernamejin==usernametemp :
            statusernamejin=True
            confirmjin=input("Apakah anda yakin ingin menghapus jin dengan username ",usernamejin," (Y/N)?")
            if confirmjin=='Y':
                del usersdata[i]
                candidata=candicrud.hapusCandiByJin(candidata,usernamejin)
                break

    if statusernamejin==False:
        print("Tidak ada jin dengan username tersebut.")

    #printlistjin(usersdata)
    datareturn=[]
    datareturn.append(usersdata)
    datareturn.append(candidata)

    return datareturn


def printlistjin(usersdata):
    lenuserdata=len(usersdata);
    
    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        passwordtemp=usertemp[1]
        roletemp=usertemp[2]

        print("User :",usertemp)


def jinTermalas(usersdata,candi):
    lenuserdata=len(usersdata)
    lencandi=len(candi)
    usernamejinTermalas='-'

    listJinPembangun=[]

    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        passwordtemp=usertemp[1]
        roletemp=usertemp[2]
        if roletemp=='jin_pembangun':
            jumlahCandiJin=0
            for i in range(0,lencandi):
                canditemp=candi[i]
                candiIDtemp=canditemp[0]
                jinCanditemp=canditemp[1]
                if jinCanditemp==usernametemp:
                    jumlahCandiJin=jumlahCandiJin+1
            
            dataJumlahJin=[usernametemp,jumlahCandiJin]
            listJinPembangun.append(dataJumlahJin)
                    
    lenlistJin=len(listJinPembangun)
    minjumlah=9999999999999999
    minusernameJin='-'
   
    for i in range(0,lenlistJin):
        listjin=listJinPembangun[i]
        usernamejin=listjin[0]
        jumlahcandi=listjin[1]
        if jumlahcandi<minjumlah:
            minjumlah=jumlahcandi
            minusernameJin=usernamejin
    
    if lenlistJin>1:
        usernamejinTermalas=minusernameJin
    else:
        usernamejinTermalas='-'

    return usernamejinTermalas




def jinTerajin(usersdata,candi):
    lenuserdata=len(usersdata)
    lencandi=len(candi)
    usernamejinTerajin='-'

    listJinPembangun=[]

    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        passwordtemp=usertemp[1]
        roletemp=usertemp[2]
        if roletemp=='jin_pembangun':
            jumlahCandiJin=0
            for i in range(0,lencandi):
                canditemp=candi[i]
                candiIDtemp=canditemp[0]
                jinCanditemp=canditemp[1]
                if jinCanditemp==usernametemp:
                    jumlahCandiJin=jumlahCandiJin+1
            
            dataJumlahJin=[usernametemp,jumlahCandiJin]
            listJinPembangun.append(dataJumlahJin)
                    
    lenlistJin=len(listJinPembangun)
    maxjumlah=0
    #maxusernameJin='-'
   
    for i in range(0,lenlistJin):
        listjin=listJinPembangun[i]
        usernamejin=listjin[0]
        jumlahcandi=listjin[1]
        if jumlahcandi>maxjumlah:
            maxjumlah=jumlahcandi
            usernamejinTerajin=usernamejin
 
    return usernamejinTerajin

