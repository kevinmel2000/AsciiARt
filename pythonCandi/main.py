# File: main.py
from data import load
from data import saveF14
from data import login
from data import jincrud
from data import jinpembangun
from data import jinpengumpul
from data import probatchbangun
from data import probatchkumpul
from data import helpmod
from data import candicrud
from data import proexit
from data import laporancandi
from data import laporanjin
from data import loadfileF13
import os
import argparse
import sys

# Anggap semua fungsi yang dipanggil merupakan fungsi yang sudah dibuat sendiri pada modul lain
users = [] # Matriks data user
candi = [] # Matriks data candi
bahan_bangunan = [] # Data bahan bangunan

parser = argparse.ArgumentParser()
parser.add_argument("folderpathvar", help="folder path")
args = parser.parse_args()

folderpath=args.folderpathvar
folderpathawal=args.folderpathvar

jumlahpasir=0
jumlahbatu=0
jumlahair=0

statrole='tamu'
usernamedatamain='tamu'
tempbahanbagunan=[]

 
if len(folderpath)==0:
    print("Tidak ada nama folder yang diberikan!")
else:
    paramReturn=loadfileF13.loadfileProcess(users,candi,bahan_bangunan,folderpath)
    users=paramReturn[0]
    candi=paramReturn[1]
    bahan_bangunan=paramReturn[2]
    folderpath=paramReturn[3]


jumlahpasir=loadfileF13.loadMaterialBagunan(jumlahpasir,bahan_bangunan,1)
jumlahbatu=loadfileF13.loadMaterialBagunan(jumlahbatu,bahan_bangunan,2)
jumlahair=loadfileF13.loadMaterialBagunan(jumlahair,bahan_bangunan,3)


while True:
    masukan = input(">>> ")
    if masukan == 'login':
        usernamedatamain=login.loginprocess(users,statrole,usernamedatamain)
        statrole=login.getrole(usernamedatamain,users,statrole)
        print(" usernamemain :",usernamedatamain);
        print(" statrole :",statrole);
    elif masukan == 'logout':
        statrole=login.logout(statrole)
    elif masukan == 'summonjin':
        if statrole=='bandung_bondowoso':
            users=jincrud.summonjin(users,statrole)
        else :
            print("Hanya Bandung Bondowoso yang punya akses")
    elif masukan == 'hapusjin':
        if statrole=='bandung_bondowoso':
            tempdata=jincrud.hapusjin(users,candi,statrole)
            users=tempdata[0]
            candi=tempdata[1]
        else :
            print("Hanya Bandung Bondowoso yang punya akses")
    elif masukan == 'ubahjin':
        if statrole=='bandung_bondowoso':
            users=jincrud.ubahjin(users,statrole)
        else :
            print("Hanya Bandung Bondowoso yang punya akses")
    elif masukan == 'batchkumpul':
        if statrole=='bandung_bondowoso':
            tempbahanbagunan=probatchkumpul.batchkumpul(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,users)
            jumlahpasir=tempbahanbagunan[0]
            jumlahbatu=tempbahanbagunan[1]
            jumlahair=tempbahanbagunan[2]
            print("Jumlah Pasir :",jumlahpasir)
            print("Jumlah Batu :",jumlahbatu)
            print("Jumlah Air :",jumlahair)
        else :
            print("Hanya Bandung Bondowoso yang punya akses")
    elif masukan == 'batchbangun':
        if statrole=='bandung_bondowoso':
            tempdata=probatchbangun.batchPembangunanCandi(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi,users)
            candi=tempdata[0]
            tempbahanbagunan=tempdata[1]
            jumlahpasir=tempbahanbagunan[0]
            jumlahbatu=tempbahanbagunan[1]
            jumlahair=tempbahanbagunan[2]
            print("Jumlah Pasir :",jumlahpasir)
            print("Jumlah Batu :",jumlahbatu)
            print("Jumlah Air :",jumlahair)
            candicrud.printlistCandi(candi)
        else :
            print("Hanya Bandung Bondowoso yang punya akses")
    elif masukan == 'laporanjin':
        if statrole=='bandung_bondowoso':
            laporanjin.laporanjin(jumlahpasir,jumlahbatu,jumlahair,users,candi)
        else :
            print("Hanya Bandung Bondowoso yang punya akses")
    elif masukan == 'laporancandi':
        if statrole=='bandung_bondowoso':
            laporancandi.laporanCandiSum(jumlahpasir,jumlahbatu,jumlahair,users,candi)
        else :
            print("Hanya Bandung Bondowoso yang punya akses")
    elif masukan == 'kumpul':
        if statrole=='jin_pengumpul':
            tempbahanbagunan=jinpengumpul.kumpul(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,usernamedatamain)
            jumlahpasir=tempbahanbagunan[0]
            jumlahbatu=tempbahanbagunan[1]
            jumlahair=tempbahanbagunan[2]
            #print("Jumlah Pasir :",jumlahpasir)
            #print("Jumlah Batu :",jumlahbatu)
            #print("Jumlah Air :",jumlahair)
        else :
            print("Hanya Jin Pengumpul yang punya akses")
    elif masukan == 'bangun':
        if statrole=='jin_pembangun':
            tempdata=jinpembangun.pembangunancandi(usernamedatamain,jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi)
            candi=tempdata[0]
            tempbahanbagunan=tempdata[1]
            jumlahpasir=tempbahanbagunan[0]
            jumlahbatu=tempbahanbagunan[1]
            jumlahair=tempbahanbagunan[2]
            print("Jumlah Pasir :",jumlahpasir)
            print("Jumlah Batu :",jumlahbatu)
            print("Jumlah Air :",jumlahair)
            candicrud.printlistCandi(candi)
        else :
            print("Hanya Jin Pembangun yang punya akses")
    elif masukan == 'hancurkancandi':
        if statrole=='roro_jonggrang':
            candi=candicrud.hapuscandi(users,candi,statrole)
            print("Jumlah Pasir :",jumlahpasir)
            print("Jumlah Batu :",jumlahbatu)
            print("Jumlah Air :",jumlahair)
            candicrud.printlistCandi(candi)
        else :
            print("Hanya Roro Jonggrang yang punya akses")
    elif masukan == 'ayamberkokok':
        if statrole=='roro_jonggrang':
            candi=candicrud.ayamberkokok(users,candi,statrole)
            print("Jumlah Pasir :",jumlahpasir)
            print("Jumlah Batu :",jumlahbatu)
            print("Jumlah Air :",jumlahair)
            candicrud.printlistCandi(candi)
        else :
            print("Hanya Roro Jonggrang yang punya akses")
    elif masukan == 'help':
        helpmod.helplist(statrole)
    elif masukan == 'load':
        datareturn=loadfileF13.loadfileProcess(users,candi,bahan_bangunan,folderpath)
        users=datareturn[0]
        candi=datareturn[1]
        bahan_bangunan=datareturn[2]
        folderpath=datareturn[3]
    elif masukan == 'exit':
        proexit.exitfunc(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi,users)
    elif masukan == 'save':
        saveF14.saveProcess(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi,users)
    else :
        print("Menu :")
        #subprocess.run(masukan)
