def randomlcg(noOfRandomNums):
    
    Xo = 5
     
    # Modulus parameter
    m = 5
     
    # Multiplier term
    a = 3
     
    # Increment term
    c = 3
 
    # Number of Random numbers
    # to be generated
    #noOfRandomNums = 10
 
    # To store random numbers
    randomNums = [0] * (noOfRandomNums)
 
    # Function Call
    linearCongruentialMethod(Xo, m, a, c,randomNums,noOfRandomNums)

    # Print the generated random numbers
    for i in randomNums:
        if i ==0 :
           i=1
        print(i, end = " ")
        num_base = i

    return num_base


def linearCongruentialMethod(Xo, m, a, c, randomNums,noOfRandomNums):
 
    # Initialize the seed state
    randomNums[0] = Xo

    # Traverse to generate required
    # numbers of random numbers
    for i in range(1, noOfRandomNums):
         
        # Follow the linear congruential method
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m


def randomlcggen():
    seed_num = 5
    multiplier = 3
    increment = 3
    modulus = 5
    unit = 10

    num_base = seed_num
    for i in range(unit, 0, -1):
        rd = (multiplier * num_base + increment) % modulus
        #print(rd)
        num_base = rd
    
    return num_base
