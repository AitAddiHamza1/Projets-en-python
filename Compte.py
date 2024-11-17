
nomber = int(input("Entrez un nombre entre 0 et 100 : "))

# Vérifier si le nombre est dans la plage valide
if 0 <= nomber <= 1000:
    digit_sum = 0

    # Utiliser une boucle de durée pour ajouter tous les chiffres
    while nomber > 0:
        digit_sum += nomber % 10  # Ajouter le dernier chiffre
        nomber //= 10  # Supprimer le dernier chiffre

    print("La somme de tous les chiffres est:", digit_sum)
else:
    print("L'entrée est hors de la plage. Veuillez entrer un nombre compris entre 0 et 100.")
