def creer_liste():
    liste = []
    #control de saisir pour la taille de la liste
    while True:
        try:
            taille = int(input("saisir la taille de votre liste"))
            if taille > 0:  
                break
            else:
                print("saisir un nombre positive")
        except ValueError:
           print("vellez entres un nombre")
          
 
    for i in range (0,taille):
         while True:
             try:
                 element = int(input(f"entrez votre {i+1} element "))
                 break 
             except ValueError:
                 print("on a besoin que des nombres")
         liste.append(element)
    return liste

def tri_croissant(liste):
    return sorted(liste)

liste = creer_liste()
liste_trie = tri_croissant(liste)
print(liste_trie)

