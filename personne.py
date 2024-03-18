class Personne:
    personne_creee = 0

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        Personne.personne_creee += 1  # Correction de l'incrémentation
       

        # acceder a l'attribut age a l'exterieur de la classe
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    #mutatteur de l'attribut age
    def infos(self):
        print("............................................................................")
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Age: {self.age}")

# Main -> programme principal 
# Instanciation de la classe Personne pour créer des objets Personne : p1, p2, p3
print("----------------------------------------------------------------------------------")
p1= Personne("Doe", "John", 30)
p1.infos()
#non recommander en POO
#encapulation ...
p1.set_age = (45)
print("age access: ", p1.age)
print("\nApres modification de l'age de stephane\n")
p1.prenom = "Joe"
p2 = Personne("Smith", "Alice", 25)
p2.infos()
p3 = Personne("Brown", "Emma", 35)
p3.infos()
# Appel de la méthode infos pour afficher les informations des personnes
print("----------------------------------------------------------------------------------")
