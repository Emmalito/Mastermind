from fonction_projet import *
from fonction_projet_2 import *


nombre_joueur = nombre_joueur()

nom_utilisateur_1,nom_utilisateur_2 = récup_nom_utilisateur(nombre_joueur)

score_1 = {}

if nom_utilisateur_1 not in score_1.keys():
    score_1[nom_utilisateur_1] = 0
if nom_utilisateur_2 not in score_1.keys():
    score_1[nom_utilisateur_2] = 0

difficulte = choix_difficulte()

continuer_parti = 'o'


while continuer_parti == 'o':
    if nombre_joueur == 2 :
        print("Choississez le nombre de pion")
        nb_pion = nombre_entier()
        print("Choississez le nombre de couleur")
        nb_couleur = nombre_entier()
        print("Choississez le nombre de coups")
        nb_coups = nombre_entier()
        score_1[nom_utilisateur_2] += mastermind(nb_pion,nb_couleur,nb_coups,difficulte,nom_utilisateur_1,nom_utilisateur_2)
        score_1[nom_utilisateur_1] += mastermind(nb_pion,nb_couleur,nb_coups,difficulte,nom_utilisateur_2,nom_utilisateur_1)
        print(nom_utilisateur_1,"vous avez",score_1[nom_utilisateur_1],"point.",nom_utilisateur_2,"vous avez",score_1[nom_utilisateur_2],"point")
        print("Voulez-vous continuez ? (o-n)")
        continuer_parti = continuer_partie()

    if nombre_joueur == 1:
        print(nom_utilisateur_1,", choississez le nombre de pion")
        nb_pion = nombre_entier()
        print(nom_utilisateur_1,", choississez le nombre de couleur")
        nb_couleur = nombre_entier()
        print(nom_utilisateur_1,", choississez le nombre de coups")
        nb_coups = nombre_entier()
        score_1[nom_utilisateur_1] += mastermind_solo(nb_pion,nb_couleur,nb_coups,difficulte,nom_utilisateur_1)
        print("Voulez-vous continuez ? (o-n)")
        continuer_parti = continuer_partie()

if nombre_joueur == 2:
    if score_1[nom_utilisateur_1] < score_1[nom_utilisateur_2]:
        print(nom_utilisateur_2,"termine premier avec",score_1[nom_utilisateur_2],"suivi de",nom_utilisateur_1,"avec",score_1[nom_utilisateur_1],"point")
    elif score_1[nom_utilisateur_2] < score_1[nom_utilisateur_1]:
        print(nom_utilisateur_1,"termine premier avec",score_1[nom_utilisateur_1],"suivi de",nom_utilisateur_2,"avec",score_1[nom_utilisateur_2],"point")
    else:
        print(nom_utilisateur_1,"vous terminez avec",score_1[nom_utilisateur_1],"point.",nom_utilisateur_2,"vous terminez avec",score_1[nom_utilisateur_2],"point")

if nombre_joueur == 1:
    print(nom_utilisateur_1,"vous terminez avec",score_1[nom_utilisateur_1],"point.")


    
    
        
       
        

        
        
    
    



