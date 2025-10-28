from data import saveF14

def exitfunc(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi,users):
    statexit=False
    stateloop=True
    while stateloop:
            masukanexit = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
            if masukanexit == 'Y':
                stateloop=False
                saveF14.saveProcess(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi,users)
                statexit=True
            elif masukanexit == 'y':
                stateloop=False
                saveF14.saveProcess(jumlahpasir,jumlahbatu,jumlahair,bahan_bangunan,candi,users)
                statexit=True
            elif masukanexit == 'N':
                stateloop=False
                statexit=False
            elif masukanexit == 'n':
                stateloop=False
                statexit=False
    
    if statexit==True:
        exit(); 