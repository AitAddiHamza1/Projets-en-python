chiffre = input("entrer nombre entier de 8 chiffres : ")
if len(chiffre) != 8:
    print("Errer! entrer nombre entier de 8 chiffres ") 

else:
    jour = chiffre[0:2]
    mois = chiffre[2:4]
    annee = chiffre[4:8]

    print(f"le jour de la semaine est : {jour}")
    print(f"le mois est : {mois}")
    print(f"l'année est : {annee}")