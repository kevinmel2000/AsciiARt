
def loginprocess(usersdata,statrole,usernamedatamain):
    
    if statrole=='tamu':
        usernamedata = input("Username :")
        passworddata = input("Password :")
        lenuserdata=len(usersdata);
        usernamestat=False
        passwordstat=False

        #print("Len User :",lenuserdata);
        for i in range(0,lenuserdata):
            usertemp=usersdata[i]
            usernametemp=usertemp[0]
            passwordtemp=usertemp[1]
            roletemp=usertemp[2]

            if usernamedata==usernametemp :
                usernamestat=True
                if passworddata==passwordtemp :
                        usernamedatamain=usernametemp
                        passwordstat=True
                        statrole=roletemp
                        break;
            
            #print(" User :",usersdata[i]);
            #print(" role :",usertemp[2]);
            print("")
        
        if usernamestat==False:
            print("Username tidak terdaftar!")
        elif passwordstat==False:
            print("Password salah!")
        else :
            print("Selamat datang,",usernametemp)
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
           
    else :
        print("Login gagal!")
        print("Anda telah login, silahkan lakukan “logout”")
        print("sebelum melakukan login kembali.")

    return usernamedatamain


def getrole(usernamedatamain,usersdata,statrole):
    lenuserdata=len(usersdata);
    
    #print("Len User :",lenuserdata);
    for i in range(0,lenuserdata):
        usertemp=usersdata[i]
        usernametemp=usertemp[0]
        roletemp=usertemp[2]

        if usernamedatamain==usernametemp :
            statrole=roletemp
            break;
    
    return statrole
                        

def logout(statrole):
    if statrole!='tamu':
        statrole='tamu'
        print(" Logout Berhasil")
    elif statrole=='tamu':
        print(" Logout gagal!")
        print(" Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout   ")
    
    return statrole