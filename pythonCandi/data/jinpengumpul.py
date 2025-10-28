from data import lcg
import random

def kumpul(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,usernamejin):
    
    jumlahPasirTemp=random.randrange(1,5)
    jumlahBatuTemp=random.randrange(1,5)
    jumlahAirTemp=random.randrange(1,5)

    #jumlahpasirtemp=lcg.randomlcg(10)
    #jumlahbatutemp=lcg.randomlcg(20)
    #jumlahairtemp=lcg.randomlcg(12)

    jumlahpasir=jumlahpasir+jumlahPasirTemp
    jumlahbatu=jumlahbatu+jumlahBatuTemp
    jumlahair=jumlahair+jumlahAirTemp
    
    print("Jin menemukan ",jumlahPasirTemp," pasir, ",jumlahBatuTemp," batu, dan ",jumlahAirTemp," air.")

    temptotalmaterial=[jumlahpasir,jumlahbatu,jumlahair]

    return temptotalmaterial

def jumlahJinPengumpul(usersdata):
    lenuserdata=len(usersdata)
    totalJinPengumpul=0
    
    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        passwordtemp=usertemp[1]
        roletemp=usertemp[2]
        if roletemp=='jin_pengumpul':
            totalJinPengumpul=totalJinPengumpul+1
    
    return totalJinPengumpul
