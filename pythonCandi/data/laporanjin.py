from data import probatchbangun
from data import probatchkumpul
from data import jincrud
from data import jinpembangun
from data import jinpengumpul

def laporanjin(jumlahpasir,jumlahbatu,jumlahair,usersdata,candi):
    jumlahJinPembangun=jinpembangun.jumlahJinPembangun(usersdata)
    jumlahJinPengumpul=jinpengumpul.jumlahJinPengumpul(usersdata)
    totalJin=jumlahJinPembangun+jumlahJinPengumpul
    usernameJinTermalas=jincrud.jinTermalas(usersdata,candi)
    usernameJinTerajin=jincrud.jinTerajin(usersdata,candi)

    print(" Total Jin :",totalJin)
    print("Total Jin Pengumpul :",jumlahJinPengumpul)
    print("Total Jin Pembangun :",jumlahJinPembangun)
    print("Jin Terajin :",usernameJinTerajin)
    print("Jin Termalas :",usernameJinTermalas)
    print("Jumlah Pasir :",jumlahpasir," Unit")
    print("Jumlah Air :",jumlahair," Unit")
    print("Jumlah Batu :",jumlahbatu," Unit")
    