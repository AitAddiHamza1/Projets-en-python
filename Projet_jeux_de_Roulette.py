import random
import os


roue_roulette = []
for i in range(1,37):
    roue_roulette.append(i)
# print(roue_roulette) 


def budget_zero(Budget):
    if Budget <= 0:
        print("J'ai fait faillite. Rechargez votre solde!")
        return True
    return False    

def Nbr_parier():
    while True:
        try:
            nbr_parier = int(input("Sur quel numéro souhaitez-vous parier (0-36) ? "))
            if nbr_parier >= 0 and nbr_parier <= 36:
                return nbr_parier
        except ValueError:            
            print("Ce numéro n'existe pas !")    
        


def Montant_parier(Budget):
    while True:
        try:
            montant_parier = int(input("Entrez le montant que vous souhaitez parier sur ce numéro : "))
            if 0< montant_parier and montant_parier <= Budget :
                return montant_parier 
            print(f"le montant doit etre entre 1 et {Budget}")    
        except ValueError:       
            print("Le montant proposé pour un pari dépasse le budget actuel : ")
        

def tourner_roue():
    result = random.choice(roue_roulette)
    print("\nLa roue tourne...")
    print(f"le numéro tire est : {result}\n")
    return result


def Gain_Perte( Budget ,nbr_parier , result , montant_parier):
    if nbr_parier == result:
        print("Félicitations, j'ai gagné le match.")
        Budget += montant_parier * 35
        print(f"Votre solde est maintenant est : {Budget} MAD")
    else:
        print("Dommage, j'ai perdu le match.")
        Budget -= montant_parier
        print(f"Votre solde est maintenant est : {Budget} MAD")
    return Budget

def informations(Budget,P):
    print("\n--- Récapitulatif Final ---")
    print(f"Votre budget est actuellement : {Budget} MAD")
    print(f"Nombre de tours que vous avez joués : {P}")

def Terminer_le_Jeu():
    while True:
        desir_du_jouer = input("Souhaitez-vous continuer à jouer ? (oui/non) : \n").strip().lower()
        if desir_du_jouer in ["oui", "non"]:
            return desir_du_jouer == "oui"
        print("Veuillez répondre par 'oui' ou 'non' : ")    
       
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')    

def main(): 
    Budget = 1000
    print("\n")
    print("***** Bienvenue dans le jeu de la roulette *****")
    print(f"Budget est : {Budget} MAD")
    print("Votr objectif est de maximiser vos gains. Bonne chance : ")
    print("\n")
    P=0
    while True:
        if budget_zero(Budget):
            break
        
        print("********************************")
        nbr_parier = Nbr_parier()
        montant_parier = Montant_parier(Budget)
        result = tourner_roue()
        Budget = Gain_Perte(Budget,nbr_parier, result, montant_parier)
        print("\n********************************")
        
        P+=1
        if not Terminer_le_Jeu():
            clear_screen()
            informations(Budget,P)
            break
        clear_screen()
        print(f"Votre budget actuel est de {Budget} MAD.")
    print("Merci d'avoir joué avec nous. A bientot !\n")        

main()