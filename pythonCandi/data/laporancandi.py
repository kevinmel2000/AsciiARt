from data import probatchbangun
from data import probatchkumpul
from data import jincrud
from data import candicrud
from data import jinpembangun
from data import jinpengumpul

def laporanCandiSum(jumlahpasir,jumlahbatu,jumlahair,usersdata,candi):
    lencandidata=len(candi);
    totalpasir=0
    totalbatu=0
    totalair=0
    
    for i in range(0,lencandidata):
        canditemp=candi[i]
        candiIDtemp=canditemp[0]
        jinCanditemp=canditemp[1]
        pasirCanditemp=canditemp[2]
        batuCanditemp=canditemp[3]
        airCanditemp=canditemp[4]
        
        totalpasir=totalpasir+pasirCanditemp
        totalbatu=totalbatu+batuCanditemp
        totalair=totalair+airCanditemp

    dataCandiTermahal=candiTermahal(candi)
    dataCandiTermurah=candiTermurah(candi)

    print("Total Candi :",lencandidata)
    print("Total Pasir yang digunakan :",totalpasir)
    print("Total Batu yang digunakan :",totalbatu)
    print("Total Air yang digunakan :",totalair)
    print("ID Candi Termahal :",dataCandiTermahal[0]," (Rp ",dataCandiTermahal[1],")")
    print("ID Candi Termurah :",dataCandiTermurah[0]," (Rp ",dataCandiTermurah[1]
          ,")")


def candiTermahal(candi):
    lenCandiData=len(candi);
    maxHarga=0
    MaxIdCandi='-'

    for i in range(0,lenCandiData):
        canditemp=candi[i]
        candiIDtemp=canditemp[0]
        jinCanditemp=canditemp[1]
        pasirCanditemp=canditemp[2]
        batuCanditemp=canditemp[3]
        airCanditemp=canditemp[4]

        hargaTemp=10000 * int(pasirCanditemp)+ 15000 * int(batuCanditemp) + 7500 * int(airCanditemp)
        if hargaTemp>maxHarga:
           MaxIdCandi=candiIDtemp
           maxHarga=hargaTemp
   
    datareturn=[]
    datareturn.append(MaxIdCandi)
    datareturn.append(maxHarga)

    return datareturn


def candiTermurah(candi):
    lenCandiData=len(candi);
    minHarga=9999999999999999
    minIdCandi='-'

    for i in range(0,lenCandiData):
        canditemp=candi[i]
        candiIDtemp=canditemp[0]
        jinCanditemp=canditemp[1]
        pasirCanditemp=canditemp[2]
        batuCanditemp=canditemp[3]
        airCanditemp=canditemp[4]

        hargaTemp=10000 * int(pasirCanditemp)+ 15000 * int(batuCanditemp) + 7500 * int(airCanditemp)
        if hargaTemp<minHarga:
           minIdCandi=candiIDtemp
           minHarga=hargaTemp
    
    datareturn=[]
    if lenCandiData<2:
       minIdCandi='-'
       minHarga='-'
    
    datareturn.append(minIdCandi)
    datareturn.append(minHarga)

    return datareturn