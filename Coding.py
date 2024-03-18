# Créez un dictionnaire appelé personne avec les clés "nom", "âge" et "ville" contenant vos propres informations.
personne = {
    "nom": "John Doe",
    "âge": 30,
    "ville": "New York"
}

# Affichez la valeur associée à la clé "âge".
print("Âge:", personne["âge"])

# Modifiez la valeur associée à la clé "ville" pour "Paris".
personne["ville"] = "Paris"

# Ajoutez une nouvelle paire clé-valeur au dictionnaire pour représenter le sexe de la personne.
personne["sexe"] = "masculin"

# Supprimez la clé "ville" du dictionnaire.
del personne["ville"]

# Affichez le dictionnaire résultant.
print("Dictionnaire résultant:", personne)