def afficher_menu():
    print("\nMenu:")
    print("1. Ajouter une personne")
    print("2. Afficher la liste des personnes")
    print("3. Rechercher une personne")
    print("4. Filtrer les personnes par âge")
    print("5. Ajouter une personne à la file d'attente")
    print("6. Supprimer une personne de la file d'attente")
    print("7. Afficher la file d'attente")
    print("8. Réserver une place dans la salle de cinéma")
    print("9. Afficher les places réservées dans la salle de cinéma")
    print("10. Afficher le nombre de places disponibles dans la salle de cinéma")
    print("11. Filtrer les réservations par personne dans la salle de cinéma")
    print("12. Annuler les réservations d'une personne dans la salle de cinéma")
    print("13. Réserver une place spéciale dans la salle de cinéma")
    print("0. Quitter")


liste_personnes = ListePersonnes()
file_attente = FileAttente()
salle_cinema = SalleCinema(capacite=50)

while True:
    afficher_menu()
    choix = input("Entrez votre choix: ")

    if choix == "1":
        nom = input("Entrez le nom de la personne: ")
        age = int(input("Entrez l'âge de la personne: "))
        liste_personnes.ajouter_personne(nom, age)
    elif choix == "2":
        liste_personnes.afficher_personnes()
    elif choix == "3":
        nom_recherche = input("Entrez le nom de la personne à rechercher: ")
        liste_personnes.rechercher_personne(nom_recherche)
    elif choix == "4":
        min_age = int(input("Entrez l'âge minimum : "))
        max_age = int(input("Entrez l'âge maximum : "))
        liste_personnes.filtrer_personnes_par_age(min_age, max_age)
    elif choix == "5":
        nom = input("Entrez le nom de la personne à ajouter à la file d'attente: ")
        file_attente.ajouter_personne_en_attente(nom)
    elif choix == "6":
        file_attente.supprimer_personne_de_attente()
    elif choix == "7":
        print("File d'attente : ", file_attente.attente)
    elif choix == "8":
        nom = input("Entrez votre nom : ")
        place = input("Entrez la place que vous voulez réserver : ")
        salle_cinema.reserver_place(nom, place)
    elif choix == "9":
        salle_cinema.afficher_places_reservées()
    elif choix == "10":
        salle_cinema.nombre_places_disponibles()
    elif choix == "11":
        nom = input("Entrez le nom de la personne pour filtrer les réservations : ")
        salle_cinema.filtrer_reservations_par_personne(nom)
    elif choix == "12":
        nom = input("Entrez le nom de la personne pour annuler ses réservations : ")
        salle_cinema.annuler_reservation(nom)
    elif choix == "13":
        nom = input("Entrez votre nom pour réserver une place spéciale : ")
        salle_cinema.reserver_place_speciale(nom)
    elif choix == "0":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro de choix valide.")
