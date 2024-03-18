def pgcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
        return num1
    
num1 =int(input("Entrez le premier nombre:"))
num2 =int(input("Entre le deuxime nombre:"))
resultat = pgcd(num1, num2)
print("Le plus grand commun diviseur de est :", resultat)