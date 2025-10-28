
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):

    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ## if (year is not divisible by 4) then (it is a common Year)
    #else if (year is not divisable by 100) then (ut us a leap year)
    #else if (year is not disible by 400) then (it is a common year)
    #else(it is aleap year)
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0





def Count_Days(year1, month1, day1):
    if month1 ==2:
        if isLeapYear(year1):
            if day1 < daysOfMonths[month1-1]+1:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
        else: 
            if day1 < daysOfMonths[month1-1]:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
    else:
        if day1 < daysOfMonths[month1-1]:
             return year1, month1, day1+1
        else:
            if month1 ==12:
                return year1+1,1,1
            else:
                    return year1, month1 +1 , 1


def daysBetweenDates(y1, m1, d1, y2, m2, d2,end_day):

    if y1 > y2:
        m1,m2 = m2,m1
        y1,y2 = y2,y1
        d1,d2 = d2,d1
    days=0
    while(not(m1==m2 and y1==y2 and d1==d2)):
        y1,m1,d1 = Count_Days(y1,m1,d1)
        days+=1
    if end_day:
        days+=1
    return days



# Test Case

def test():

        print("Masukkan Tahun ")
        tahunmulaidata = raw_input("Tahun :");
        print("Tahun : ", tahunmulaidata)
        tahunmulai=int(tahunmulaidata);


        print("Masukkan Tanggal mulai!")

        bulanmulaidata = input("Bulan Mulai:");
        print("Bulan Mulai : ", bulanmulaidata)
        bulanmulai=int(bulanmulaidata);


        tanggalmulaidata = raw_input("Tanggal Mulai:");
        print("Tanggal Mulai : ", tanggalmulaidata)
        tanggalmulai=int(tanggalmulaidata);


        print("Masukkan Tanggal selesai!")

        bulanselesaidata = raw_input("Bulan Selesai:");
        print("Bulan Selesai: ", bulanselesaidata)
        bulanselesai=int(bulanselesaidata);

        tanggalselesaidata = raw_input("Tanggal Selesai:");
        print("Tanggal Selesai: ", tanggalselesaidata)
        tanggalselesai=int(tanggalselesaidata);
        
        result=daysBetweenDates(tahunmulai,bulanmulai,tanggalmulai,tahunmulai,bulanselesai,tanggalselesai,False)
        
        print("Jumlah Hari:", result);

test()



