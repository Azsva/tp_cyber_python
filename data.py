def add (nom, prenom, matricule, date_naissance):
    etudiants= {
        "nom": nom,
        "prenom": prenom,
        "matricule": matricule,
        "date_naissance": date_naissance,
    }
    return etudiants
def get(matricule, etudiants):
    for k,v in etudiants.items():
        if matricule == v:
            print(f"{k} : {v}") 
            break

def get_all(etudiants):
    print("liste des etudiants : ")
    print("-----------------------------------------------")
    for k,v in etudiants.items():
        print(f"{k} : {v}")
        print("-----------------------------------------------")

