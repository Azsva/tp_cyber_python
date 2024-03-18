ma_liste =[2,4,5,6] #0 - 3
mon_tube = ()
dict = { 
        'lion' :"est un mamifere", 
        'homme':"est un etre humain",
        'chat':"est un felin",
        1:"Devoir numero 1"
        }
#key:value; key : chaine, int, 
#print(dict)

print(dict['chat']) #0 -len(ma_liste)-1
mon_dictionnaire={
    "voiture":"vehicule a quatre roues",
    "velo": "vehicule a deux roues",
}
mon_dictionnaire["tricycle"] = "vehicule a trois roues"
print(type(mon_dictionnaire))

for element in ma_liste:
    print(element)

for i in range(0, len(ma_liste)):
    print(f"Index={i} de l'element {ma_liste[i]}")

print("--------------------------------------------------------")
print("........")

for element_dict in mon_dictionnaire:
    print(element_dict)
    print("........")

print("--------------------------------------------------------")
for i in mon_dictionnaire.items(): #mon_dictionnaire["key"]
    print(i)
print("--------------------------------------------------------")
for (key, value) in mon_dictionnaire.items():
    print(f"{key} est un{value}")

