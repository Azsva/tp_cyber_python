class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self._titre = titre
        self._auteur = auteur
        self._genre = genre
        self._prix = prix
   
              #decorateur transforme la methode titre en get_titre
              #et l'attribut titre devient des lors prives
          # Getter pour l'attribut nom
    @property
    def titre(self):
        return self._titre
# Setter pour l'attribut nom
    @titre.setter
    def titre(self, titre):
        self._titre = titre

    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, auteur):
        self._auteur = auteur

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, genre):
        self._genre = genre

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, prix):
        self._prix = prix

    def afficher_details(self):
        print("----------------------------------------------------------------------------------")
        print(f"Titre: {self.titre}, Auteur: {self.auteur}, Genre: {self.genre}, Prix: {self.prix})")
print("----------------------------------------------------------------------------------")

l1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "Fantasy", 25.99)
l2 = Livre("Harry potter", "J.K. Rowling", "Fantasy", 15.99)
l3 = Livre("Dragon Ball", "r: Akira Toriyama", "anime", 19.99)

# Accès aux détails du premier livre
print("Détails du premier livre:")
l1.afficher_details()

# Accès aux détails du deuxième livre
print("\nDétails du deuxième livre:")
l2.afficher_details()

# Accès aux détails du troisième livre
print("\nDétails du troisième livre:")
l3.afficher_details()

class Librairie:
    def __init__(self):
        self.collection = []

    def ajouter_livre(self, livre):
        self.collection.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté à la librairie.")

    def chercher_livre(self, titre):
        for livre in self.collection:
            if livre.titre.lower() == titre.lower():
                livre.afficher_details()
                return
        print(f"Le livre '{titre}' n'a pas été trouvé dans la librairie.")

    def supprimer_livre(self, titre):
        for livre in self.collection:
            if livre.titre.lower() == titre.lower():
                self.collection.remove(livre)
                print(f"Le livre '{titre}' a été supprimé de la librairie.")
                return
        print(f"Le livre '{titre}' n'a pas été trouvé dans la librairie.")

# Création de la librairie
librairie = Librairie()

# Ajout de livres à la librairie
while True:
    titre = input("Entrez le titre du livre (ou appuyez sur Entrée pour changer a d'autre options) : ")
    if not titre:
        break  # Si l'utilisateur appuie sur Entrée sans saisir de titre, sortir de la boucle
    auteur = input("Entrez l'auteur du livre : ")
    genre = input("Entrez le genre du livre : ")
    prix = float(input("Entrez le prix du livre : "))
    livre = Livre(titre, auteur, genre, prix)
    librairie.ajouter_livre(livre)

# Recherche d'un livre par titre par l'utilisateur
titre_recherche = input("Entrez le titre du livre que vous recherchez : ")
librairie.chercher_livre(titre_recherche)

# Suppression d'un livre par l'utilisateur
titre_suppression = input("Entrez le titre du livre que vous voulez supprimer : ")
librairie.supprimer_livre(titre_suppression)

# Affichage de la collection de livres restante par l'utilisateur
print("\nLivres restants dans la librairie :")
for livre in librairie.collection:
    livre.afficher_details()