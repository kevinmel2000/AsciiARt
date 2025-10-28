print("Program Geomteric Series: ");
print("-----------------------------");

nilaiadata = input("Masukkan nilai Koefisien a :");
print("nilai Koefisien a: ", nilaiadata)
nilaia=int(nilaiadata); 

print("-----------------------------");

nilairdata = input("Masukkan nilai Rasio r :");
print("nilai Rasio r: ", nilairdata)
nilair=int(nilairdata); 
print("-----------------------------");


nilaindata = input("Masukkan nilai Order n :");
print("nilai Order n: ", nilaindata)
nilain=int(nilaindata); 

print("-----------------------------");


total = 0
value = nilaia

if nilair>=1 :
    print("Nilai G Rasio Divergen");
    if nilain>1 :
        for i in range(nilain):
            print("" , value);
            total = total + value
            value = value * nilair
    elif nilain > 0 and nilain==1:
        total = value + (value * nilair);
    else :
        total=0;

    S_n = (nilaia*(nilair**nilain))/(nilair-1)

    print("The Sum of Geometric Progression Series Nilai G Divergen = " , total);
    print("Sum of n terms: = " , S_n);

elif nilair < 1 :
    print("Nilai G Rasio Konvergen");
    
    nilaigtotal= (nilaia*(nilair**nilain))/(1-nilair);
    print("Nilai G :" , nilaigtotal);

    nilaitemp=nilaia/(1-nilair);
    #print("Nilai Temp :" , nilaitemp);

    nilaierror=nilaitemp-nilaigtotal;
    print("Nilai G Error = " , nilaierror);
