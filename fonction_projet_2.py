import os
import pickle
from random import *



def récup_nom_utilisateur(a):
    nom_utilisateur = input("Nom joueur 1 : ")
    nom_utilisateur = nom_utilisateur.capitalize()
    if a > 1:
        nom_utilisateur_2 = input("Nom joueur 2 : ")
        nom_utilisateur_2 = nom_utilisateur_2.capitalize()
        if nom_utilisateur == nom_utilisateur_2 or nom_utilisateur_2 == 'PC' :
            print("Veuillez choisir un pseudo différent.")
            return récup_nom_utilisateur(a)
        else:
            return nom_utilisateur,nom_utilisateur_2
    else:
        return (nom_utilisateur,'PC')


def choix_difficulte():
    print("Choisir un niveau de difficulté : 1 - 2 - 3 :")
    a = input()
    try:
        a = int(a)
    except ValueError:
        return choix_difficulte()
    if not 0<a<4:
        return choix_difficulte()
    else:
        return a


def nombre_joueur():
    print("Choisir le nombre de joueur : 1 - 2 :")
    a = input()
    try:
        a = int(a)
    except ValueError:
        return nombre_joueur()
    if not 0<a<3:
        return nombre_joueur()
    else:
        return a


def nombre_entier():
    a = input()
    try:
        a = int(a)
    except ValueError:
        print("Veuillez entrer un nombre entier")
        return nombre_entier()
    else:
        a = int(a)
        return a




def continuer_partie():
    a = input()
    if a != str('o') and a != str('n'):
        print("'o' = oui ; 'n' = non")
        return continuer_partie()
    else:
        return a


def saisie_combi_pc(nb_pion,nb_couleur,difficulte):
    combi = []
    for i in range(0,nb_pion):
        combi.append(randrange(0,nb_couleur))
    if difficulte == 3:
        a = randrange(0,10)
        b = randrange(0,15)
        c = randrange(0,25)
        d = randrange(0,45)
        if a == 8:
            e = randrange(0,nb_pion-1)
            combi[e] = ' '
        if a==8 and b == 13:
            e = randrange(0,nb_pion-1)
            combi[e] = ' '
            e = randrange(0,nb_pion-1)
            combi[e] = ' '

        if a==8 and b == 13 and c == 21:
            e = randrange(0,nb_pion-1)
            combi[e] = ' '
            e = randrange(0,nb_pion-1)
            combi[e] = ' '
            e = randrange(0,nb_pion-1)
            combi[e] = ' '

        if a==8 and b == 13 and c == 21 and d == 39:
            for i in range(nb_pion):
                combi[i] = ' '
    if difficulte == 1:
        e = 0
        while e < len(combi):
            for i in range (nb_pion):
                if combi[i] == combi[e] and i != e:
                    combi[i] = randrange(0,nb_pion-1)
                    i = 0
                    e = 0
            e += 1
            
    return combi
