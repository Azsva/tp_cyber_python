def est_present(ma_liste):
    while(True):
        try:
            valeur_rechercer= int(input("Quel valeur rechercher vous"))
            break
        except ValueError:
            print("Saissir une valeur numerique")
    return valeur_rechercer in ma_liste


def creer_liste():
    ma_liste= []
    while(True):
        try:
            taille= int(input("Donner la taille de la liste"))
            if taille > 0:
                break
            else:
                print("Saissir une valeur positive")
                continue
        except ValueError:
            print("Saissir une valeur numerique")
        
    for i in range(0, taille):
        while(True):
            try:
                en =  int(input(f"Saisir  l'element {i + 1} de la liste: "))
                break
            except ValueError:
                print("Saissir une valeur numerique ")
         
        ma_liste.append(en)
    return ma_liste
ma_liste = creer_liste()
if est_present(ma_liste):
    print(f" La valeur est present dans la liste :{ma_liste}")
else:
    print(f"La valeur  n'est pas dans la liste: {ma_liste}")

        