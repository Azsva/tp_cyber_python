class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    def afficher_details(self):
        print(f"Nom: {self.nom}, Age: {self.age}")


class ListePersonnes:
    def __init__(self):
        self.liste = []

    def ajouter_personne(self, nom, age):
        personne = Personne(nom, age)
        self.liste.append(personne)

    def afficher_personnes(self):
        print("Liste des personnes:")
        for personne in self.liste:
            personne.afficher_details()

    def rechercher_personne(self, nom):
        for personne in self.liste:
            if personne.nom.lower() == nom.lower():
                print("Personne trouvée:")
                personne.afficher_details()
                return
        print(f"Aucune personne trouvée avec le nom '{nom}'.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        print(f"Personnes âgées entre {min_age} et {max_age} :")
        for personne in self.liste:
            if min_age <= personne.age <= max_age:
                personne.afficher_details()


class FileAttente:
    def __init__(self):
        self.attente = []

    def ajouter_personne_en_attente(self, nom):
        self.attente.append(nom)

    def supprimer_personne_de_attente(self):
        if self.attente:
            personne = self.attente.pop(0)
            print(f"{personne} a été supprimé de la file d'attente.")
        else:
            print("La file d'attente est vide.")


class FileAttentePrioritaire(FileAttente):
    def __init__(self):
        super().__init__()
        self.attente_prioritaire = []

    def ajouter_personne_prioritaire(self, nom):
        self.attente_prioritaire.append(nom)

    def supprimer_personne_de_attente(self):
        if self.attente_prioritaire:
            personne = self.attente_prioritaire.pop(0)
            print(f"{personne} (prioritaire) a été supprimé de la file d'attente.")
        elif self.attente:
            personne = self.attente.pop(0)
            print(f"{personne} a été supprimé de la file d'attente.")
        else:
            print("La file d'attente est vide.")


class SalleCinema:
    def __init__(self, capacite):
        self._capacite = capacite
        self._reservations = {}

    @property
    def capacite(self):
        return self._capacite

    @property
    def reservations(self):
        return self._reservations

    def reserver_place(self, nom, place):
        if place not in self.reservations.values() and len(self.reservations) < self.capacite:
            self.reservations[nom] = place
            print(f"{nom} a réservé la place {place}.")
        else:
            print("La place est déjà réservée ou la salle est pleine.")

    def afficher_places_reservées(self):
        print("Places réservées :")
        for personne, place in self.reservations.items():
            print(f"{personne}: Place {place}")

    def nombre_places_disponibles(self):
        disponibles = self.capacite - len(self.reservations)
        print(f"Il reste {disponibles} places disponibles.")

    def filtrer_reservations_par_personne(self, nom):
        print(f"Réservations de {nom} :")
        for personne, place in self.reservations.items():
            if personne == nom:
                print(f"{personne}: Place {place}")

    def annuler_reservation(self, nom):
        if nom in self.reservations:
            del self.reservations[nom]
            print(f"Toutes les réservations de {nom} ont été annulées.")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

    def reserver_place_speciale(self, nom):
        if "place spéciale" not in self.reservations.values() and len(self.reservations) < self.capacite:
            self.reservations[nom] = "place spéciale"
            print(f"{nom} a réservé une place spéciale.")
        else:
            print("La place spéciale est déjà réservée ou la salle est pleine.")
