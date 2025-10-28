
skalagempadata = input("Masukkan Skala Gempa Bumi :");
print("Skala Gempa Bumi: ", skalagempadata)
skalagempa=float(skalagempadata); 



if skalagempa < 2.0  :
    print("Skala Gempa Bumi Micro")
elif skalagempa > 2.0 and  skalagempa <= 3.9:
    print("Skala Gempa Bumi Minor")
elif skalagempa > 3.9 and  skalagempa <= 4.9:
    print("Skala Gempa Bumi Light")
elif skalagempa > 4.9 and  skalagempa <= 5.9:
    print("Skala Gempa Bumi Moderate")
elif skalagempa > 5.9 and  skalagempa <= 6.9:
    print("Skala Gempa Bumi Strong")
elif skalagempa > 6.9 and  skalagempa <= 7.9:
    print("Skala Gempa Bumi Major")
elif skalagempa > 7.9 :
    print("Skala Gempa Bumi Great")
