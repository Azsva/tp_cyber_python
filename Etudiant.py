class Etudiant:
    #creation d'un constructeur - permet l'instanciation de la classe
    #constructeur est une fonction
    #self designe l'objet courant
    etudiant_cree = 0 # variable de classe , un variable independante de tout objet de cette classe
    def __init__(self, nom, prenom, age, niveau):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.niveau = niveau
        Etudiant.etudiant_cree += 1

        print(f"Creation de l'etudiant {Etudiant.etudiant_cree}")
    
    def infos(self):
         print(f"Nom : {self.nom}, prenom: {self.prenom}, age: {self.age}, niveau: {self.niveau}")
         print("------------------------------------------------------------------------------------")





#creation d'un objet: creation d'un etudiant
print("------------------------------------------------------------------------------------")
etudiant1 = Etudiant("Labrie", "stephane", 40,"AEC")
#print(f"Nom : {etudiant1.nom}, prenom: {etudiant1.prenom}, age: {etudiant1.age}, niveau: {etudiant1.niveau}")
#print("------------------------------------------------------------------------------------")
etudiant1.infos()
etudiant2 = Etudiant("Diallo", "Abdou", 48, "AEC")
#print(f"Nom : {etudiant2.nom}, prenom: {etudiant2.prenom}, age: {etudiant2.age}, niveau: {etudiant2.niveau}")
#print("------------------------------------------------------------------------------------")
etudiant2.infos()
etudiant3 = Etudiant("Bijou", "Jojo", 48, "BAcc")
#print(f"Nom : {etudiant3.nom}, prenom: {etudiant3.prenom}, age: {etudiant3.age}, niveau: {etudiant3.niveau}")
#print("------------------------------------------------------------------------------------")
etudiant3.infos()

etudiant4 = Etudiant("St-P{ierre", "Maxime", 40, "Doctorat")
etudiant4.infos()