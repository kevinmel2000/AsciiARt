
def hapusCandiByJin(candidata,idjin):
    lencandidata=len(candidata);
    
    for i in range(0,lencandidata):
        canditemp=candidata[i]
        candiIDtemp=canditemp[0]
        jinCanditemp=canditemp[1]
        pasirCanditemp=canditemp[2]

        if idjin==jinCanditemp :
            del candidata[i]
            break
            #print("Candi :",canditemp)
    
    return candidata

def printlistCandi(candidata):
    lencandidata=len(candidata);
    
    for i in range(0,lencandidata):
        canditemp=candidata[i]
        candiIDtemp=canditemp[0]
        jinCanditemp=canditemp[1]
        pasirCanditemp=canditemp[2]

        print("Candi :",canditemp)



def hapuscandi(usersdata,candidata,statrole):
    candiID = input("Masukkan ID candi:")
        
    lencandidata=len(candidata);
    statusIDCandi=False

    for i in range(0,lencandidata):
        canditemp=candidata[i]
        IDCanditemp=canditemp[0]
        JinCanditemp=canditemp[1]
        pasirCanditemp=canditemp[2]

        if candiID==IDCanditemp :
            statusIDCandi=True
            confirmcandi=input("Apakah anda yakin ingin menghancurkan candi ID: ",candiID," (Y/N)?")
            if confirmcandi=='Y':
                del candidata[i]
                break

    if statusIDCandi==False:
        print("Tidak ada Candi dengan ID tersebut.")

    #printlistCandi(candidata)
    
    return candidata


def ayamberkokok(usersdata,candidata,statrole):
    lenCandidata=len(candidata);
    
    print("Kukuruyuk.. Kukuruyuk..")
    print("Jumlah Candi: ",lenCandidata)
    
    if lenCandidata > 99:
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    elif lenCandidata < 100:
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        