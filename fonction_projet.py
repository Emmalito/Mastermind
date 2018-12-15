from fonction_projet_2 import *
from random import *

def saisie_de_couleur(nb_couleur):
    print("Entrez une couleur")
    e = nombre_entier()
    if ( e < 0 or e > (nb_couleur-1) ):
        print("Entrez une couleur entre 0 et",nb_couleur-1," : ")
        return saisie_de_couleur(nb_couleur)
    return e


def saisie_combi(nb_pion,nb_couleur,difficulte):
    combi = []
    for i in range (nb_pion):
        e = saisie_de_couleur(nb_couleur)
        for i in range (len(combi)):
            while combi[i] == e and difficulte == 1:
                print("Vous ne pouvez pas mettre 2 même couleurs. Choississez une autre")
                e = saisie_de_couleur(nb_couleur)
                i = 0
        combi.append(e)
    if difficulte == 3:
        print("Voulez-vous remplacer des cases par des cases vide ? : 0(non) - 1(oui)")
        a = nombre_entier()
        while a<0 or a>1:
            print("0 pour non et 1 pour oui")
            a = nombre_entier()
        if a == 1:
            print("Choississez le nombre de case que vous désirez vider")
            nb_case = nombre_entier()
            while nb_case<0 or nb_case>nb_pion:
                print("Veuillez choisir un nombre de case entre 0 et",nb_pion)
                nb_case = nombre_entier()
            if nb_case>0:
                print(combi)
                print("Quelles cases ?")
                for i in range(nb_pion):
                    print("La case",i+1,"?(o/n)")
                    a = input()
                    if a == 'o':
                        combi[i] = ' '
    return combi


def couleur_bien_place(combi_secret,combi_propose):
    a = 0
    for i in range (len(combi_secret)):
        if combi_secret[i] == combi_propose[i]:
            a = a+1
    return a


def couleur_mal_place(combi_secret,combi_propose):
    a = 0
    e = 0
    for i in range (len(combi_secret)):
        while e < len(combi_propose) :
            for i in range (len(combi_secret)):
                if combi_secret[i] == combi_propose[e] and i != e:
                    a = a+1
                    break
            e = e+1
    return a


def mastermind (nb_pion,nb_couleur,nb_coup,difficulte,j1,j2):
    print(j1,",entrez la combinaison secrète")
    secret = saisie_combi(nb_pion,nb_couleur,difficulte)
    print (secret)
    print("Valider ? (o-n)")
    valider = continuer_partie()
    if valider == 'n':
        return mastermind (nb_pion,nb_couleur,nb_coup,difficulte,j1,j2)
    a = 0
    while a < 60:
        print("")
        a = a+1
    print(j2,",proposez une combinaison")
    proposé = saisie_combi(nb_pion,nb_couleur,difficulte)
    print(proposé)
    bien = couleur_bien_place(secret,proposé)
    print("Vous avez ",bien,"pion bien placé")
    mal = couleur_mal_place(secret,proposé)
    print("Vous avez",mal,"pions mal placé")
    i = 1
    if bien == nb_pion :
        print("Félicitation, vous avez trouvé la combinaison secrète")
        a = 1
        return a
    while bien != nb_pion and i < nb_coup:
        print(j2,",il vous reste",nb_coup-i," coups. Proposez une combinaison,")
        proposé = saisie_combi(nb_pion,nb_couleur,difficulte)
        print(proposé)
        bien = couleur_bien_place(secret,proposé)
        print("Vous avez ",bien,"pion bien placé")
        mal = couleur_mal_place(secret,proposé)
        print("Vous avez",mal,"pions mal placé")
        if bien == nb_pion :
            print("Félicitation, vous avez trouvé la combinaison secrète")
            a = 1
            return a
        i += 1
    if bien != nb_pion :
        print("Vous avez perdu la combinaison était", secret)
        a = 0
        return a


def mastermind_solo (nb_pion,nb_couleur,nb_coup,difficulte,j1):
    secret = saisie_combi_pc(nb_pion,nb_couleur,difficulte)
    print(j1,",proposez une combinaison")
    proposé = saisie_combi(nb_pion,nb_couleur,difficulte)
    print(proposé)
    bien = couleur_bien_place(secret,proposé)
    print("Vous avez ",bien,"pion bien placé")
    mal = couleur_mal_place(secret,proposé)
    print("Vous avez",mal,"pions mal placé")
    i = 1
    if bien == nb_pion :
        print("Félicitation, vous avez trouvé la combinaison secrète")
        a = 1
        return a
    while bien != nb_pion and i < nb_coup:
        print(j1,",il vous reste",nb_coup-i," coups. Proposez une combinaison,")
        proposé = saisie_combi(nb_pion,nb_couleur,difficulte)
        print(proposé)
        bien = couleur_bien_place(secret,proposé)
        print("Vous avez ",bien,"pion bien placé")
        mal = couleur_mal_place(secret,proposé)
        print("Vous avez",mal,"pions mal placé")
        if bien == nb_pion :
            print("Félicitation, vous avez trouvé la combinaison secrète")
            a = 1
            return a
        i += 1
    if bien != nb_pion :
        print("Vous avez perdu la combinaison était", secret)
        a = 0
        return a
        



        
