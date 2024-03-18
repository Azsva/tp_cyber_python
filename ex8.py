def factorielle(n):
    if n ==0:
        return 1
    elif n < 0:
        return False 
    else:
        #return factoriel (n-1) #4, 3, 2, 1
        fact = 1
        return n*factorielle(n-1)
        for i in range(2, n+ 1):
            fact = fact * i # 1= fact =2; fact = 2*3=6
        return fact
    
print(f"le factorielle est :{factorielle(5)}")