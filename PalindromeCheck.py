
print("Masukkan Input Data String atau Number")
inputstrnumdata = raw_input("Input Data String atau Number :");

try:
    valdata = int(inputstrnumdata)
    print("int data")
    temp=valdata
    rev=0
    while(valdata>0):
        dig=valdata%10
        rev=rev*10+dig
        valdata=valdata//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("Not a palindrome!")
except ValueError:
    print("That's not an int!")
    string=inputstrnumdata
    if(string==string[::-1]):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")