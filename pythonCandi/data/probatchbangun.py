from data import jinpembangun
import random

def batchPembangunanCandi(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,datacandi,usersdata):

    jumlahCostPasirTemp=0
    jumlahCostBatuTemp=0
    jumlahCostAirTemp=0
    jumlahCostPasir=0
    jumlahCostBatu=0
    jumlahCostAir=0

    candidata=datacandi

    lenuserdata=len(usersdata)
    totaljinpembangun=jinpembangun.jumlahJinPembangun(usersdata)
    
    jumlahcandi=len(candidata)
    jumlahIDcandi=jumlahcandi+1
    StatEnough=True
    StatGagal=False
    jumlahbangun=0

    if totaljinpembangun>0:
        for i in range(0,lenuserdata):
            usertemp=usersdata[i]
            usernametemp=usertemp[0]
            passwordtemp=usertemp[1]
            roletemp=usertemp[2]
            if roletemp=='jin_pembangun':
                 jumlahCostPasirTemp=random.randrange(1,5)
                 jumlahCostBatuTemp=random.randrange(1,5)
                 jumlahCostAirTemp=random.randrange(1,5)

                 if jumlahCostPasirTemp>jumlahpasir:
                    StatEnough=False
                 elif jumlahCostBatuTemp>jumlahbatu:
                    StatEnough=False
                 elif jumlahCostAirTemp>jumlahair:
                    StatEnough=False
                 
                 if StatEnough==False:
                    StatGagal=True
                 elif StatEnough==True:
                    
                    #jumlahpasir=jumlahpasir-jumlahCostPasirTemp
                    #jumlahbatu=jumlahbatu-jumlahCostBatuTemp
                    #jumlahair=jumlahair-jumlahCostAirTemp

                    jumlahCostPasir=jumlahCostPasir+jumlahCostPasirTemp
                    jumlahCostBatu=jumlahCostBatu+jumlahCostBatuTemp
                    jumlahCostAir=jumlahCostAir+jumlahCostAirTemp
                 
                    for i in range(0,jumlahcandi):
                        canditemp=candidata[i]
                        candiIDtemp=canditemp[0]
                        if candiIDtemp==jumlahIDcandi :
                            jumlahIDcandi=jumlahcandi+1

                    jumlahbangun=jumlahbangun+1
                    if jumlahcandi<101 :
                        canditemp=[jumlahIDcandi,usernametemp,jumlahCostPasirTemp,jumlahCostBatuTemp,jumlahCostAirTemp]
                        candidata.append(canditemp)
                        jumlahcandi=len(candidata)
                        
                        sisacandi=100-jumlahcandi
                        #print("Sisa candi yang perlu dibangun:",sisacandi)
                    else :
                        sisacandi=100-100
                        break
                        #print("Sisa candi yang perlu dibangun:",sisacandi)

        print("Mengerahkan ",totaljinpembangun," jin untuk membangun candi dengan total bahan ",jumlahCostPasir," pasir, ",jumlahCostBatu," batu, dan ",jumlahCostAir," air.")
        
        if StatGagal==True:
            jumlahpasircal=abs(jumlahCostPasir-jumlahpasir)
            jumlahbatucal=abs(jumlahCostBatu-jumlahbatu)
            jumlahaircal=abs(jumlahCostAir-jumlahair)
            print("Bangun gagal. Kurang ",jumlahpasircal," pasir,",jumlahbatucal," batu, dan ",jumlahaircal," air.")
            print("Candi yang terbangun 0") 
        else:
            jumlahpasir=jumlahpasir-jumlahCostPasir
            jumlahbatu=jumlahbatu-jumlahCostBatu
            jumlahair=jumlahair-jumlahCostAir
            print("Jin berhasil membangun total ",jumlahbangun," candi.")  
            datacandi=candidata  
        

    else :
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

    temptotalmaterial=[jumlahpasir,jumlahbatu,jumlahair]

    datareturn=[]
    datareturn.append(datacandi)
    datareturn.append(temptotalmaterial)

    return datareturn
