from data import jinpengumpul

def batchkumpul(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,usersdata):
    
    jumlahPasirTemp=0
    jumlahBatuTemp=0
    jumlahAirTemp=0

    lenuserdata=len(usersdata)
    totaljinpengumpul=jinpengumpul.jumlahJinPengumpul(usersdata)

    if totaljinpengumpul>0:
        print("Mengerahkan ",totaljinpengumpul," jin untuk mengumpulkan bahan.")

        for i in range(0,lenuserdata):
            usertemp=usersdata[i]
            usernametemp=usertemp[0]
            passwordtemp=usertemp[1]
            roletemp=usertemp[2]
            if roletemp=='jin_pengumpul':
                tempbahanbagunan=jinpengumpul.kumpul(jumlahPasirTemp,jumlahBatuTemp,jumlahAirTemp,bahan_bangunan,usernametemp)
                jumlahPasirTemp=jumlahPasirTemp+tempbahanbagunan[0]
                jumlahBatuTemp=jumlahBatuTemp+tempbahanbagunan[1]
                jumlahAirTemp=jumlahAirTemp+tempbahanbagunan[2]
        

        
        print("Jin menemukan total ",jumlahPasirTemp," pasir, ",jumlahBatuTemp," batu, dan ",jumlahAirTemp," air.")
    else :
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    
    
    jumlahpasir=jumlahpasir+jumlahPasirTemp
    jumlahbatu=jumlahbatu+jumlahBatuTemp
    jumlahair=jumlahair+jumlahAirTemp

    temptotalmaterial=[jumlahpasir,jumlahbatu,jumlahair]

    return temptotalmaterial