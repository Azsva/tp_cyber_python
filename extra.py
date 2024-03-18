
def convertir_en_cerlsius(tempF):
    #C=(F-32)x9/5
    tempC =(tempF - 32) * 9/5
    return tempC


try:
    tempF = int(input("Veillez inscrire votre Temperature en C a convertir"))
except ValueError:
        print("Entre Invalide")
tempC=convertir_en_cerlsius(tempF)
print("voici la temperature en C:",tempC)
