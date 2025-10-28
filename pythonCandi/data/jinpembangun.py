from data import lcg
import random

def pembangunancandi(usernamedatamain,jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,datacandi):

    jumlahCostPasirTemp=random.randrange(1,5)
    jumlahCostBatuTemp=random.randrange(1,5)
    jumlahCostAirTemp=random.randrange(1,5)

    StatEnough=True
    if jumlahCostPasirTemp>jumlahpasir:
        StatEnough=False
    elif jumlahCostBatuTemp>jumlahbatu:
        StatEnough=False
    elif jumlahCostAirTemp>jumlahair:
        StatEnough=False
    
    if StatEnough==False:
      print("Bahan bangunan tidak mencukupi.")
      print("Candi tidak bisa dibangun!")
    elif StatEnough==True:
      jumlahpasir=jumlahpasir-jumlahCostPasirTemp
      jumlahbatu=jumlahbatu-jumlahCostBatuTemp
      jumlahair=jumlahair-jumlahCostAirTemp

      print("Candi berhasil dibangun.")

      jumlahcandi=len(datacandi)
      jumlahIDcandi=jumlahcandi+1

      for i in range(0,jumlahcandi):
        canditemp=datacandi[i]
        candiIDtemp=canditemp[0]
        if candiIDtemp==jumlahIDcandi :
           jumlahIDcandi=jumlahcandi+1
       
      if jumlahcandi<101 :
        canditemp=[jumlahIDcandi,usernamedatamain,jumlahCostPasirTemp,jumlahCostBatuTemp,jumlahCostAirTemp]
        datacandi.append(canditemp)
        jumlahcandi=len(datacandi);
        sisacandi=100-jumlahcandi
        print("Sisa candi yang perlu dibangun:",sisacandi)
      else :
        sisacandi=100-100
        print("Sisa candi yang perlu dibangun:",sisacandi)

    temptotalmaterial=[jumlahpasir,jumlahbatu,jumlahair]

    datareturn=[]
    datareturn.append(datacandi)
    datareturn.append(temptotalmaterial)

    return datareturn


def jumlahJinPembangun(usersdata):
    lenuserdata=len(usersdata);
    totalJinPembangun=0
  
    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        passwordtemp=usertemp[1]
        roletemp=usertemp[2]
        if roletemp=='jin_pembangun':
            totalJinPembangun=totalJinPembangun+1
    
    return totalJinPembangun


        

 