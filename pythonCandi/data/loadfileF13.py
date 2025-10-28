from data import load
import os
import argparse
import sys

def loadfileProcess(users,candi,bahan_bangunan,inputparam):
    
    datareturn=[]
    
    if inputparam=='':
        masukanfolder=input("Masukkan nama folder:")
    else:
        masukanfolder=inputparam
    
    if len(masukanfolder)==0:
        print("Tidak ada nama folder yang diberikan!")
    else:
        folderpath='save/'+masukanfolder
        isExist = os.path.exists(folderpath)
        if not isExist:   
            print("Folder “",masukanfolder,"” tidak ditemukan.")
        else:
            print("Loading...")
    
            users=load.load(folderpath+"/user.csv", users)
            candi=load.load(folderpath+"/candi.csv", candi)
            bahan_bangunan=load.load(folderpath+"/bahan_bangunan.csv", bahan_bangunan)

           
            datareturn.append(users)
            datareturn.append(candi)
            datareturn.append(bahan_bangunan)
            datareturn.append(masukanfolder)

            print("Selamat datang di program “Manajerial Candi")
    
    return datareturn


def loadMaterialBagunan(jumlahdata,bahan_bangunan,tipematerial):
        jumlahtotal=0
        if tipematerial==1 :
            materialtemp=bahan_bangunan[0]
        elif tipematerial==2 :
            materialtemp=bahan_bangunan[1]
        elif tipematerial==3 :
            materialtemp=bahan_bangunan[2]
        
        namatemp=materialtemp[0]
        desctemp=materialtemp[1]
        jumlahtemp=materialtemp[2]
        jumlahtotal=int(jumlahdata)+int(jumlahtemp)

        return jumlahtotal


def loadfileProcess2():
    masukanfolder = input("Masukkan nama folder:")

    if len(masukanfolder)==0:
        print("Tidak ada nama folder yang diberikan!")
    else:
        folderpath='save/'+masukanfolder
        isExist = os.path.exists(folderpath)
        if not isExist:   
            print("Folder “",masukanfolder,"” tidak ditemukan.")
        else:
            print("Loading...")
    
            users=load.load(folderpath+"/user.csv", users)
            candi=load.load(folderpath+"/candi.csv", candi)
            bahan_bangunan=load.load(folderpath+"/bahan_bangunan.csv", bahan_bangunan)

    datareturn=[]
    datareturn.append(users)
    datareturn.append(candi)
    datareturn.append(bahan_bangunan)
    return datareturn
