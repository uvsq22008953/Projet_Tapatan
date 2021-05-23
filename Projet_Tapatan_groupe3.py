""""
groupe MPCI 3
Bertuit Marlone   IA
Moreira Théo  Positionnement et plateau
Lopes Ferreira Lucas Sauvegarde
Baali Wassim Déplacement
Fernandez Sébastien Condition de victoire
https://github.com/uvsq22008953/Projet_Tapatan
"""

import tkinter as tk
import random
from tkinter.constants import RIDGE
from tkinter import messagebox
import pickle

#VARIABLES POSITIONS PIONS BLEU
x1b1, x2b1, y1b1, y2b1=0, 0, 0, 0
x1b2, x2b2, y1b2, y2b2=0, 0, 0, 0
x1b3, x2b3, y1b3, y2b3=0, 0, 0, 0
#VARIABLES POSITIONS PIONS ROUGE
x1r1, x2r1, y1r1, y2r1=0, 0, 0, 0
x1r2, x2r2, y1r2, y2r2=0, 0, 0, 0
x1r3, x2r3, y1r3, y2r3=0, 0, 0, 0

#VALEURS QUE L'ON VA MODIFIER
x1, x2, y1, y2=0, 0, 0, 0

nb_tours=1
# 0 si tour des rouges // 1 si tour des bleus
tourdejouer=random.randint(0, 1)
premiertour = tourdejouer
phase_placement, jel, selectionner, dx, dy = 1, 0, 0, 0, 0
nb_placements_bleu, nb_placements_rouge = 0, 0
case1_libre, case2_libre, case3_libre, case4_libre, case5_libre=True, True, True, True, True
case6_libre, case7_libre, case8_libre, case9_libre=True, True, True, True
case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure = -1, -1, -1, -1, -1
case6_couleure, case7_couleure, case8_couleure, case9_couleure = -1, -1, -1, -1
pion_b_1, pion_b_2, pion_b_3 = 0, 0, 0
pion_r_1, pion_r_2, pion_r_3 = 0, 0, 0
pionr1, pionr2, pionr3 = 0, 0, 0
pionb1, pionb2, pionb3 = 0, 0, 0
winner, score_bleu, score_rouge, check1, check2 = "", 0, 0, 0, 0
fichier_nul = open(r"Fichier_Nul.txt", "w")
emplacement = [case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure]

#Joueur contre ia
partie_bot = 0
valeur_alea = 0
pos_pionsR = []
pionc1, pionc2, pionc3, pionc4, pionc5, pionc6, pionc7, pionc8, pionc9 = 0, 0, 0, 0, 0, 0, 0, 0, 0


#FONCTIONS

def joueur_vs_ia():
    global partie_bot
    partie_bot = 1
    print ("mode joueur contre IA")

def positionnement(a, z, e, r):
    global nb_tours, tourdejouer, selectionner, nb_placements_bleu, nb_placements_rouge
    global jel, dx, dy
    global pionr1, pionr2, pionr3, pion_r_1, pion_r_2, pion_r_3
    global pionb1, pionb2, pionb3, pion_b_1, pion_b_2, pion_b_3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if nb_tours<=6:
                    if tourdejouer==1:
                        if nb_tours<=2:
                            x1b1=a
                            x2b1=z
                            y1b1=e
                            y2b1=r
                            pion_b_1= canvas.create_rectangle(x1b1, x2b1, y1b1, y2b1, fill="blue", width=2)
                            nb_placements_bleu+=1
                            tourdejouer=0
                        elif nb_tours<=4:
                            x1b2=a
                            x2b2=z
                            y1b2=e
                            y2b2=r
                            pion_b_2= canvas.create_rectangle(x1b2, x2b2, y1b2, y2b2, fill="blue", width=2)
                            nb_placements_bleu+=1
                            tourdejouer=0
                        elif nb_tours<=6:
                            x1b3=a
                            x2b3=z
                            y1b3=e
                            y2b3=r
                            pion_b_3= canvas.create_rectangle(x1b3, x2b3, y1b3, y2b3, fill="blue", width=2)
                            nb_placements_bleu+=1
                            tourdejouer=0
                    elif tourdejouer==0:
                        if nb_tours<=2:
                            x1r1=a
                            x2r1=z
                            y1r1=e
                            y2r1=r
                            pion_r_1= canvas.create_rectangle(x1r1, x2r1, y1r1, y2r1, fill="red", width=2)
                            nb_placements_rouge+=1
                            tourdejouer=1
                        elif nb_tours<=4:
                            x1r2=a
                            x2r2=z
                            y1r2=e
                            y2r2=r
                            pion_r_2= canvas.create_rectangle(x1r2, x2r2, y1r2, y2r2, fill="red", width=2)
                            nb_placements_rouge+=1
                            tourdejouer=1
                        elif nb_tours<=6:
                            x1r3=a
                            x2r3=z
                            y1r3=e
                            y2r3=r
                            pion_r_3= canvas.create_rectangle(x1r3, x2r3, y1r3, y2r3, fill="red", width=2)
                            nb_placements_rouge+=1
                            tourdejouer=1
    else:
                    if tourdejouer==1:
                        if pionb1==1:
                            x1b1=a
                            x2b1=z
                            y1b1=e
                            y2b1=r
                            if dx==x1b1:
                                dy=x2b1-dy
                                canvas.move(pion_b_1,0,dy)
                                tourdejouer=0
                                pionb1=0
                            elif dy==x2b1:
                                dx=x1b1-dx
                                canvas.move(pion_b_1,dx,0)
                                tourdejouer=0
                                pionb1=0
                            else:
                                dx=x1b1-dx
                                dy=x2b1-dy
                                canvas.move(pion_b_1,dx,dy)
                                tourdejouer=0
                                pionb1=0
                        elif pionb2==1:
                            x1b2=a
                            x2b2=z
                            y1b2=e
                            y2b2=r
                            if dx==x1b2:
                                dy=x2b2-dy
                                canvas.move(pion_b_2,0,dy)
                                tourdejouer=0
                                pionb2=0
                            elif dy==x2b2:
                                dx=x1b2-dx
                                canvas.move(pion_b_2,dx,0)
                                tourdejouer=0
                                pionb2=0
                            else:
                                dx=x1b2-dx
                                dy=x2b2-dy
                                canvas.move(pion_b_2,dx,dy)
                                tourdejouer=0
                                pionb2=0
                        elif pionb3==1:
                            x1b3=a
                            x2b3=z
                            y1b3=e
                            y2b3=r
                            if dx==x1b3:
                                dy=x2b3-dy
                                canvas.move(pion_b_3,0,dy)
                                tourdejouer=0
                                pionb3=0
                            elif dy==x2b3:
                                dx=x1b3-dx
                                canvas.move(pion_b_3,dx,0)
                                tourdejouer=0
                                pionb3=0
                            else:
                                dx=x1b3-dx
                                dy=x2b3-dy
                                canvas.move(pion_b_3,dx,dy)
                                tourdejouer=0
                                pionb3=0
                    elif tourdejouer==0:
                        if pionr1==1:
                            x1r1=a
                            x2r1=z
                            y1r1=e
                            y2r1=r
                            print(dx,x1r1)
                            if dx==x1r1:
                                dy=x2r1-dy
                                canvas.move(pion_r_1,0,dy)
                                tourdejouer=1
                                pionr1=0
                            elif dy==x2r1:
                                dx=x1r1-dx
                                canvas.move(pion_r_1,dx,0)
                                tourdejouer=1
                                pionr1=0
                            else:
                                dx=x1r1-dx
                                dy=x2r1-dy
                                canvas.move(pion_r_1,dx,dy)
                                tourdejouer=1
                                pionr1=0
                        elif pionr2==1:
                            x1r2=a
                            x2r2=z
                            y1r2=e
                            y2r2=r
                            if dx==x1r2:
                                dy=x2r2-dy
                                canvas.move(pion_r_2,0,dy)
                                tourdejouer=1
                                pionr2=0
                            elif dy==x2r2:
                                dx=x1r2-dx
                                canvas.move(pion_r_2,dx,0)
                                tourdejouer=1
                                pionr2=0
                            else:
                                dx=x1r2-dx
                                dy=x2r2-dy
                                canvas.move(pion_r_2,dx,dy)
                                tourdejouer=1
                                pionr2=0
                        elif pionr3==1:
                            x1r3=a
                            x2r3=z
                            y1r3=e
                            y2r3=r
                            if dx==x1r3:
                                dy=x2r3-dy
                                canvas.move(pion_r_3,0,dy)
                                tourdejouer=1
                                pionr3=0
                            elif dy==x2r3:
                                dx=x1r3-dx
                                canvas.move(pion_r_3,dx,0)
                                tourdejouer=1
                                pionr3=0
                            else:
                                dx=x1r3-dx
                                dy=x2r3-dy
                                canvas.move(pion_r_3,dx,dy)
                                tourdejouer=1
                                pionr3=0
    if nb_tours >= 6:
        Nul()


def ClicCase(event):
    global tourdejouer, nb_placements_bleu, nb_placements_rouge, nb_tours, selectionner
    global case1_libre, case2_libre, case3_libre, case4_libre, case5_libre
    global case6_libre, case7_libre, case8_libre, case9_libre
    global case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure
    global case6_couleure, case7_couleure, case8_couleure, case9_couleure
    global valeur_alea
    global pionc1, pionc2, pionc3, pionc4, pionc5, pionc6, pionc7, pionc8, pionc9

#joueur contre joueur
    if nb_tours<=6 and partie_bot == 0:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75 and case1_libre==True:
            #case1
            if tourdejouer==1:
                case1_couleure=1
                positionnement(25,25,75,75)
                nb_tours+=1
                case1_libre=False
            else:
                case1_couleure=0
                positionnement(25,25,75,75)
                nb_tours+=1
                case1_libre=False
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75 and case2_libre==True:
            #case2
            if tourdejouer==1:
                case2_couleure=1
                positionnement(375,25,425,75)
                nb_tours+=1
                case2_libre=False
            else:
                case2_couleure=0
                positionnement(375,25,425,75)
                nb_tours+=1
                case2_libre=False
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75 and case3_libre==True:
            #case3
            if tourdejouer==1:
                case3_couleure=1
                positionnement(725,25,775,75)
                nb_tours+=1
                case3_libre=False
            else:
                case3_couleure=0
                positionnement(725,25,775,75)
                nb_tours+=1
                case3_libre=False
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425 and case4_libre==True:
            #case4
            if tourdejouer==1:
                case4_couleure=1
                positionnement(25,375,75,425)
                nb_tours+=1
                case4_libre=False
            else:
                case4_couleure=0
                positionnement(25,375,75,425)
                nb_tours+=1
                case4_libre=False
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425 and case5_libre==True:
            #case5
            if tourdejouer==1:
                case5_couleure=1
                positionnement(375,375,425,425)
                nb_tours+=1
                case5_libre=False
            else:
                case5_couleure=0
                positionnement(375,375,425,425)
                nb_tours+=1
                case5_libre=False
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425 and case6_libre==True:
            #case6
            if tourdejouer==1:
                case6_couleure=1
                positionnement(725,375,775,425)
                nb_tours+=1
                case6_libre=False
            else:
                case6_couleure=0
                positionnement(725,375,775,425)
                nb_tours+=1
                case6_libre=False
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775 and case7_libre==True:
            #case7
            if tourdejouer==1:
                case7_couleure=1
                positionnement(25,725,75,775)
                nb_tours+=1
                case7_libre=False
            else:
                case7_couleure=0
                positionnement(25,725,75,775)
                nb_tours+=1
                case7_libre=False 
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775 and case8_libre==True:
            #case8
            if tourdejouer==1:
                case8_couleure=1
                positionnement(375,725,425,775)
                nb_tours+=1
                case8_libre=False
            else:
                case8_couleure=0
                positionnement(375,725,425,775)
                nb_tours+=1
                case8_libre=False
        elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775 and case9_libre==True:
            #case9
            if tourdejouer==1:
                case9_couleure=1
                positionnement(725,725,775,775)
                nb_tours+=1
                case9_libre=False
            else:
                case9_couleure=0
                positionnement(725,725,775,775)
                nb_tours+=1
                case9_libre=False
    elif nb_tours>6 and nb_tours%2==1:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75:
            if case1_libre==False and case1_couleure==tourdejouer:
                verification1(25,25,75,75)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75:
            if case2_libre==False and case2_couleure==tourdejouer:
                verification2(375,25,425,75)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75:
            if case3_libre==False and case3_couleure==tourdejouer:
                verification3(725,25,775,75)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
                print(43)
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425:
            if case4_libre==False and case4_couleure==tourdejouer:
                verification4(25,375,75,425)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425:
            if case5_libre==False and case5_couleure==tourdejouer:
                verification5(375,375,425,425)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2 
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425:
            if case6_libre==False and case6_couleure==tourdejouer:
                verification6(725,375,775,425)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775:
            if case7_libre==False and case7_couleure==tourdejouer:
                verification7(25,725,75,775)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775:
            if case8_libre==False and case8_couleure==tourdejouer:
                verification8(375,725,425,775)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        else:
            if case9_libre==False and case9_couleure==tourdejouer:
                verification9(725,725,775,775)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
    elif nb_tours>6 and nb_tours%2==0:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75 and (selectionner==2 or selectionner==4 or selectionner==5):
            if case1_libre==False:
                nb_tours+=1
            else:
                case1_couleure=tourdejouer
                positionnement(25,25,75,75)
                selectionner=0
                case1_libre=False
                nb_tours+=1
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75 and (selectionner==1 or selectionner==3 or selectionner==5) :
            if case2_libre==False:
                nb_tours+=1
            else:
                case2_couleure=tourdejouer
                positionnement(375,25,425,75)
                selectionner=0
                case2_libre=False
                nb_tours+=1
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75 and (selectionner==2 or selectionner==6 or selectionner==5):
            if case3_libre==False:
                nb_tours+=1
            else:
                case3_couleure=tourdejouer
                positionnement(725,25,775,75)
                selectionner=0
                case3_libre=False
                nb_tours+=1
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425 and (selectionner==1 or selectionner==7 or selectionner==5):
            if case4_libre==False:
                nb_tours+=1
            else:
                case4_couleure=tourdejouer
                positionnement(25,375,75,425)
                selectionner=0
                case4_libre=False
                nb_tours+=1
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425 and (selectionner==1 or selectionner==2 or selectionner==3 or selectionner==4 or selectionner==6 or selectionner==7 or selectionner==8 or selectionner==9):
            if case5_libre==False:
                nb_tours+=1
            else:
                case5_couleure=tourdejouer
                positionnement(375,375,425,425)
                selectionner=0
                case5_libre=False
                nb_tours+=1
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425 and (selectionner==3 or selectionner==9 or selectionner==5):
            if case6_libre==False:
                nb_tours+=1
            else:
                case6_couleure=tourdejouer
                positionnement(725,375,775,425)
                selectionner=0
                case6_libre=False
                nb_tours+=1
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775 and (selectionner==4 or selectionner==8 or selectionner==5):
            if case7_libre==False:
                nb_tours+=1
            else:
                case7_couleure=tourdejouer
                positionnement(25,725,75,775)
                selectionner=0
                case7_libre=False
                nb_tours+=1
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775 and (selectionner==7 or selectionner==9 or selectionner==5):
            if case8_libre==False:
                nb_tours+=1
            else:
                case8_couleure=tourdejouer
                positionnement(375,725,425,775)
                selectionner=0
                case8_libre=False
                nb_tours+=1
        elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775 and (selectionner==8 or selectionner==6 or selectionner==5):
            if case9_libre==False:
                nb_tours+=1
            else:
                case9_couleure=tourdejouer
                positionnement(725,725,775,775)
                selectionner=0
                case9_libre=False
                nb_tours+=1
#joueur contre ia
    if partie_bot==1:
        valeur_alea=random.randint(1,9)
    if nb_tours<=6 and partie_bot==1:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75 and case1_libre==True or (valeur_alea==1 and tourdejouer==0) and case1_libre==True:
            #case1
            if tourdejouer==1:
                positionnement(25,25,75,75)
                nb_tours+=1
                case1_couleure=1
                case1_libre=False
            else:
                positionnement(25,25,75,75)
                nb_tours+=1
                case1_couleure=0
                case1_libre=False
                pionc1 = valeur_alea
                pos_pionsR.append(pionc1)
                valeur_alea = 0
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75 and case2_libre==True or (valeur_alea==2 and tourdejouer==0) and case2_libre==True:
            #case2
            if tourdejouer==1:
                positionnement(375,25,425,75)
                nb_tours+=1
                case2_couleure=1
                case2_libre=False
            else:
                positionnement(375,25,425,75)
                nb_tours+=1
                case2_couleure=0
                case2_libre=False
                pionc2 = valeur_alea
                pos_pionsR.append(pionc2)
                valeur_alea = 0
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75 and case3_libre==True or (valeur_alea==3 and tourdejouer==0) and case3_libre==True:
            #case3
            if tourdejouer==1:
                positionnement(725,25,775,75)
                nb_tours+=1
                case3_couleure=1
                case3_libre=False
            else:
                positionnement(725,25,775,75)
                nb_tours+=1
                case3_couleure=0
                case3_libre=False
                pionc3 = valeur_alea
                pos_pionsR.append(pionc3)
                valeur_alea = 0
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425 and case4_libre==True or (valeur_alea==4 and tourdejouer==0) and case4_libre==True:
            #case4
            if tourdejouer==1:
                positionnement(25,375,75,425)
                nb_tours+=1
                case4_couleure=1
                case4_libre=False
            else:
                positionnement(25,375,75,425)
                nb_tours+=1
                case4_couleure=0
                case4_libre=False
                pionc4 = valeur_alea
                pos_pionsR.append(pionc4)
                valeur_alea = 0
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425 and case5_libre==True or (valeur_alea==5 and tourdejouer==0) and case5_libre==True:
            #case5
            if tourdejouer==1:
                positionnement(375,375,425,425)
                nb_tours+=1
                case5_couleure=1
                case5_libre=False
            else:
                positionnement(375,375,425,425)
                nb_tours+=1
                case5_couleure=0
                case5_libre=False
                pionc5 = valeur_alea
                pos_pionsR.append(pionc5)
                valeur_alea = 0
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425 and case6_libre==True or (valeur_alea==6 and tourdejouer==0) and case6_libre==True:
            #case6
            if tourdejouer==1:
                positionnement(725,375,775,425)
                nb_tours+=1
                case6_couleure=1
                case6_libre=False
            else:
                positionnement(725,375,775,425)
                nb_tours+=1
                case6_couleure=0
                case6_libre=False
                pionc6 = valeur_alea
                pos_pionsR.append(pionc6)
                valeur_alea = 0
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775 and case7_libre==True or (valeur_alea==7 and tourdejouer==0) and case7_libre==True:
            #case7
            if tourdejouer==1:
                positionnement(25,725,75,775)
                nb_tours+=1
                case7_couleure=1
                case7_libre=False
            else:
               positionnement(25,725,75,775)
               nb_tours+=1
               case7_couleure=0
               case7_libre=False
               pionc7 = valeur_alea
               pos_pionsR.append(pionc7)
               valeur_alea = 0
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775 and case8_libre==True or (valeur_alea==8 and tourdejouer==0) and case8_libre==True:
            #case8
            if tourdejouer==1:
                positionnement(375,725,425,775)
                nb_tours+=1
                case8_libre=False
                case8_couleure=1
            else:
                positionnement(375,725,425,775)
                nb_tours+=1
                case8_libre=False
                case8_couleure=1
                pionc8 = valeur_alea
                pos_pionsR.append(pionc8)
                valeur_alea = 0
        elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775 and case9_libre==True or (valeur_alea==9 and tourdejouer==0) and case9_libre==True:
            #case9
            if tourdejouer==1:
                positionnement(725,725,775,775)
                nb_tours+=1
                case9_couleure=1
                case9_libre=False
            else:
                positionnement(725,725,775,775)
                nb_tours+=1
                case9_couleure=0
                case9_libre=False
                pionc9 = valeur_alea
                pos_pionsR.append(pionc9)
                valeur_alea = 0
        print(pos_pionsR)

    elif nb_tours>6 and nb_tours%2==1:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75 or (pionc1 in pos_pionsR and tourdejouer == 0):
            if case1_libre==False and case1_couleure==tourdejouer:
                verification1(25,25,75,75)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75 or (pionc2 in pos_pionsR and tourdejouer == 0):
            if case2_libre==False and case2_couleure==tourdejouer:
                verification2(375,25,425,75)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75 or (pionc3 in pos_pionsR and tourdejouer == 0):
            if case3_libre==False and case3_couleure==tourdejouer:
                verification3(725,25,775,75)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
                print(43)
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425 or (pionc4 in pos_pionsR and tourdejouer == 0):
            if case4_libre==False and case4_couleure==tourdejouer:
                verification4(25,375,75,425)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425 or (pionc5 in pos_pionsR and tourdejouer == 0):
            if case5_libre==False and case5_couleure==tourdejouer:
                verification5(375,375,425,425)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2 
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425 or (pionc6 in pos_pionsR and tourdejouer == 0):
            if case6_libre==False and case6_couleure==tourdejouer:
                verification6(725,375,775,425)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775 or (pionc7 in pos_pionsR and tourdejouer == 0):
            if case7_libre==False and case7_couleure==tourdejouer:
                verification7(25,725,75,775)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775 or (pionc8 in pos_pionsR and tourdejouer == 0):
            if case8_libre==False and case8_couleure==tourdejouer:
                verification8(375,725,425,775)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2
        else:
            if case9_libre==False and case9_couleure==tourdejouer or (pionc9 in pos_pionsR and tourdejouer == 0):
                verification9(725,725,775,775)
                nb_tours+=1
            else:
                nb_tours=nb_tours+2

    
    elif nb_tours>6 and nb_tours%2==0:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75 and (selectionner==2 or selectionner==4 or selectionner==5) or (pionc1 in pos_pionsR and tourdejouer == 0) and (selectionner==2 or selectionner==4 or selectionner==5):
            if case1_libre==False:
                nb_tours+=1
            else:
                case1_couleure=tourdejouer
                positionnement(25,25,75,75)
                selectionner=0
                case1_libre=False
                nb_tours+=1
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75 and (selectionner==1 or selectionner==3 or selectionner==5) or (pionc2 in pos_pionsR and tourdejouer == 0) and (selectionner==1 or selectionner==3 or selectionner==5) :
            if case2_libre==False:
                nb_tours+=1
            else:
                case2_couleure=tourdejouer
                positionnement(375,25,425,75)
                selectionner=0
                case2_libre=False
                nb_tours+=1
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75 and (selectionner==2 or selectionner==6 or selectionner==5) or (pionc3 in pos_pionsR and tourdejouer == 0) and (selectionner==2 or selectionner==6 or selectionner==5):
            if case3_libre==False:
                nb_tours+=1
            else:
                case3_couleure=tourdejouer
                positionnement(725,25,775,75)
                selectionner=0
                case3_libre=False
                nb_tours+=1
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425 and (selectionner==1 or selectionner==7 or selectionner==5) or (pionc4 in pos_pionsR and tourdejouer == 0) and (selectionner==1 or selectionner==7 or selectionner==5):
            if case4_libre==False:
                nb_tours+=1
            else:
                case4_couleure=tourdejouer
                positionnement(25,375,75,425)
                selectionner=0
                case4_libre=False
                nb_tours+=1
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425 and (selectionner==1 or selectionner==2 or selectionner==3 or selectionner==4 or selectionner==6 or selectionner==7 or selectionner==8 or selectionner==9) or (pionc5 in pos_pionsR and tourdejouer == 0) and (selectionner==1 or selectionner==2 or selectionner==3 or selectionner==4 or selectionner==6 or selectionner==7 or selectionner==8 or selectionner==9):
            if case5_libre==False:
                nb_tours+=1
            else:
                case5_couleure=tourdejouer
                positionnement(375,375,425,425)
                selectionner=0
                case5_libre=False
                nb_tours+=1
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425 and (selectionner==3 or selectionner==9 or selectionner==5) or (pionc6 in pos_pionsR and tourdejouer==0) and (selectionner==3 or selectionner==9 or selectionner==5):
            if case6_libre==False:
                nb_tours+=1
            else:
                case6_couleure=tourdejouer
                positionnement(725,375,775,425)
                selectionner=0
                case6_libre=False
                nb_tours+=1
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775 and (selectionner==4 or selectionner==8 or selectionner==5) or (pionc7 in pos_pionsR and tourdejouer == 0) and (selectionner==4 or selectionner==8 or selectionner==5):
            if case7_libre==False:
                nb_tours+=1
            else:
                case7_couleure=tourdejouer
                positionnement(25,725,75,775)
                selectionner=0
                case7_libre=False
                nb_tours+=1
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775 and (selectionner==7 or selectionner==9 or selectionner==5) or (pionc8 in pos_pionsR and tourdejouer == 0) and (selectionner==7 or selectionner==9 or selectionner==5):
            if case8_libre==False:
                nb_tours+=1
            else:
                case8_couleure=tourdejouer
                positionnement(375,725,425,775)
                selectionner=0
                case8_libre=False
                nb_tours+=1
        elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775 and (selectionner==8 or selectionner==6 or selectionner==5) or (pionc9 in pos_pionsR and tourdejouer == 0) and (selectionner==8 or selectionner==6 or selectionner==5):
            if case9_libre==False:
                nb_tours+=1
            else:
                case9_couleure=tourdejouer
                positionnement(725,725,775,775)
                selectionner=0
                case9_libre=False
                nb_tours+=1
    ConditionVictoire()
                

def verification1(q,s,d,f):
    global tourdejouer, nb_tours, case1_couleure, selectionner, dx, dy, jel
    global case1_libre, case2_libre, case4_libre, case5_libre
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case2_libre==False and case5_libre==False and case4_libre==False:
        nb_tours+=1
    elif case1_libre==False and case1_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=1
            case1_libre=True
            case1_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=1
            case1_libre=True
            case1_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=1
            case1_libre=True
            case1_couleure=-1
            dx=q
            dy=s
    elif case1_libre==False and case1_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=1
            case1_libre=True
            case1_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=1
            case1_libre=True
            case1_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=1
            case1_libre=True
            case1_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1
    
def verification2(q,s,d,f):
    global case1_libre, case2_libre, case3_libre, case5_libre
    global tourdejouer, nb_tours, case2_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case1_libre==False and case3_libre==False and case5_libre==False:
        nb_tours+=1
    elif case2_libre==False and case2_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=2
            case2_libre=True
            case2_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=2
            case2_libre=True
            case2_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=2
            case2_libre=True
            case2_couleure=-1
            dx=q
            dy=s
    elif case2_libre==False and case2_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=2
            case2_libre=True
            case2_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=2
            case2_libre=True
            case2_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=2
            case2_libre=True
            case2_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1

def verification3(q,s,d,f):
    global case6_libre, case2_libre, case3_libre, case5_libre
    global tourdejouer, nb_tours, case3_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case6_libre==False and case2_libre==False and case5_libre==False:
        nb_tours+=1
    elif case3_libre==False and case3_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=3
            case3_libre=True
            case3_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=3
            case3_libre=True
            case3_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=3
            case3_libre=True
            case3_couleure=-1
            dx=q
            dy=s
    elif case3_libre==False and case3_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=3
            case3_libre=True
            case3_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=3
            case3_libre=True
            case3_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=3
            case3_libre=True
            case3_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1

def verification4(q,s,d,f):
    global case1_libre, case5_libre, case7_libre, case4_libre
    global tourdejouer, nb_tours, case4_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case1_libre==False and case5_libre==False and case7_libre==False:
        nb_tours+=1
    elif case4_libre==False and case4_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=4
            case4_libre=True
            case4_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=4
            case4_libre=True
            case4_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=4
            case4_libre=True
            case4_couleure=-1
            dx=q
            dy=s
    elif case4_libre==False and case4_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=4
            case4_libre=True
            case4_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=4
            case4_libre=True
            case4_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=4
            case4_libre=True
            case4_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1

def verification5(q,s,d,f):
    global case1_libre, case2_libre, case3_libre, case4_libre, case5_libre, case6_libre, case7_libre, case8_libre, case9_libre
    global tourdejouer, nb_tours, case5_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case1_libre==False and case2_libre==False and case3_libre==False and case4_libre==False and case6_libre==False and case7_libre==False and case8_libre==False and case9_libre==False:
        nb_tours+=1
    elif case5_libre==False and case5_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=5
            case5_libre=True
            case5_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=5
            case5_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=5
            case5_libre=True
            case5_couleure=-1
            dx=q
            dy=s
    elif case5_libre==False and case5_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=5
            case5_libre=True
            case5_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=5
            case5_libre=True
            case5_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=5
            case5_libre=True
            case5_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1

def verification6(q,s,d,f):
    global case3_libre, case5_libre, case6_libre, case9_libre
    global tourdejouer, nb_tours, case6_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    print(x2r2,s)
    if case3_libre==False and case5_libre==False and case9_libre==False:
        nb_tours+=1
    elif case6_libre==False and case6_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=6
            case6_libre=True
            case6_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=6
            case6_libre=True
            case6_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=6
            case6_libre=True
            case6_couleure=-1
            dx=q
            dy=s
    elif case6_libre==False and case6_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=6
            case6_libre=True
            case6_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=6
            case6_libre=True
            case6_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=6
            case6_libre=True
            case6_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1

def verification7(q,s,d,f):
    global case4_libre, case7_libre, case8_libre, case5_libre
    global tourdejouer, nb_tours, case7_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case4_libre==False and case8_libre==False and case5_libre==False:
        nb_tours+=1
    elif case7_libre==False and case7_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=7
            case7_libre=True
            case7_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=7
            case7_libre=True
            case7_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=7
            case7_libre=True
            case7_couleure=-1
            dx=q
            dy=s
    elif case7_libre==False and case7_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=7
            case7_libre=True
            case7_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=7
            case7_libre=True
            case7_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=7
            case7_libre=True
            case7_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1

def verification8(q,s,d,f):
    global case7_libre, case8_libre, case9_libre, case5_libre
    global tourdejouer, nb_tours, case8_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case7_libre==False and case9_libre==False and case5_libre==False:
        nb_tours+=1
    elif case8_libre==False and case8_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=8
            case8_libre=True
            case8_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=8
            case8_libre=True
            case8_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=8
            case8_libre=True
            case8_couleure=-1
            dx=q
            dy=s
    elif case8_libre==False and case8_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=8
            case8_libre=True
            case8_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=8
            case8_libre=True
            case8_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=8
            case8_libre=True
            case8_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1

def verification9(q,s,d,f):
    global case6_libre, case8_libre, case9_libre, case5_libre
    global tourdejouer, nb_tours, case9_couleure, selectionner, dx, dy, jel
    global pionr1, pionr2, pionr3, pionb1, pionb2, pionb3
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, x2b3, y1b3, y2b3
    global x1r1, x2r1, y1r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, x2r3, y1r3, y2r3
    if case6_libre==False and case8_libre==False and case5_libre==False:
        nb_tours+=1
    elif case9_libre==False and case9_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=9
            case9_libre=True
            case9_couleure=-1
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=9
            case9_libre=True
            case9_couleure=-1
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=9
            case9_libre=True
            case9_couleure=-1
            dx=q
            dy=s
    elif case9_libre==False and case9_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=9
            case9_libre=True
            case9_couleure=-1
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=9
            case9_libre=True
            case9_couleure=-1
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=9
            case9_libre=True
            case9_couleure=-1
            dx=q
            dy=s
    else:
        nb_tours+=1


def Sauvegarder():
    emplacement = [case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure, nb_tours]
    pickle.dump (emplacement, open("sauvegarde", "wb"))



def Charger ():
    global nb_tours, emplacement, tourdejouer
    global case1_libre, case2_libre, case3_libre, case4_libre, case5_libre, case6_libre, case7_libre, case8_libre, case9_libre
    Initialisation()
    emplacement = pickle.load (open("sauvegarde", "rb"))
    tourdejouer = emplacement [9]%2
    print("emplacement charger", emplacement)

    if emplacement[0] == 1 : 
        canvas.create_rectangle(25,25,75,75, fill="blue", width=2)
        case1_libre = False
        nb_tours += 1 
    elif emplacement[0] == 0 : 
        canvas.create_rectangle(25,25,75,75, fill="red", width=2)
        case1_libre = False
        nb_tours += 1 
    elif emplacement[0] == -1 :
        case1_libre = True


    if emplacement[1] == 1 :  
        canvas.create_rectangle(375,25,425,75, fill="blue", width=2)
        case2_libre = False
        nb_tours += 1 
    elif emplacement[1] == 0 :
        canvas.create_rectangle(375,25,425,75, fill="red", width=2)
        case2_libre = False
        nb_tours += 1
    elif emplacement[1] == -1 :
        case2_libre = True

    if emplacement[2] == 1 :
        canvas.create_rectangle(725,25,775,75, fill="blue", width=2)
        case3_libre = False
        nb_tours += 1
    elif emplacement[2] == 0 :
        canvas.create_rectangle(725,25,775,75, fill="red", width=2)
        case3_libre = False
        nb_tours += 1
    elif emplacement[2] == -1 :
        case3_libre = True
        
    if emplacement[3] == 1 :
        canvas.create_rectangle(25,375,75,425, fill="blue", width=2)
        case4_libre = False
        nb_tours += 1
    elif emplacement[3] == 0 : 
        canvas.create_rectangle(25,375,75,425, fill="red", width=2)
        case4_libre = False
        nb_tours += 1
    elif emplacement[3] == -1 :
        case4_libre = True

    if emplacement[4] == 1 :
        canvas.create_rectangle(375,375,425,425, fill="blue", width=2)
        case5_libre = False
        nb_tours += 1 
    elif emplacement[4] == 0 :
        canvas.create_rectangle(375,375,425,425, fill="red", width=2)
        case5_libre = False
        nb_tours += 1
    elif emplacement[4] == -1 :
        case5_libre = True

    if emplacement[5] == 1 :
        canvas.create_rectangle(725,375,775,425, fill="blue", width=2)
        case6_libre = False
        nb_tours += 1
    elif emplacement[5] == 0 :
        canvas.create_rectangle(725,375,775,425, fill="red", width=2)
        case6_libre = False
        nb_tours += 1
    elif emplacement[5] == -1 :
        case6_libre = True
    
    if emplacement[6] == 1 : 
        canvas.create_rectangle(25,725,75,775, fill="blue", width=2)
        case7_libre = False
        nb_tours+= 1
    elif emplacement[6] == 0 :
        canvas.create_rectangle(25,725,75,775, fill="red", width=2)
        case7_libre = False
        nb_tours +=1
    elif emplacement[6] == -1 :
        case7_libre = True

    if emplacement[7] == 1 :
        canvas.create_rectangle(375,725,425,775, fill="blue", width=2)
        case8_libre = False
        nb_tours += 1
    elif emplacement[7] == 0 :
        canvas.create_rectangle(375,725,425,775, fill="red", width=2)
        case8_libre = False
        nb_tours += 1
    elif emplacement[7] == -1 :
        case8_libre = True

    if emplacement[8] == 1 :
        canvas.create_rectangle(725,725,775,775, fill="blue", width=2)
        case9_libre = False
        nb_tours += 1
    elif emplacement[8] == 0 :
        canvas.create_rectangle(725,725,775,775, fill="red", width=2)
        case9_libre = False
        nb_tours += 1
    elif emplacement[8] == -1 :
        case9_libre = True
    
    return(emplacement)




def Initialisation():
    global x1, x2, y1, y2, nb_tours, tourdejouer, phase_placement, nb_placements_rouge, nb_placements_bleu, case1_libre, case2_libre, case3_libre
    global case4_libre, case5_libre, case6_libre, case7_libre, case8_libre, case9_libre, selectionner, winner, score_bleu, score_rouge, jel, dx, dy, canvas
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, y1b3, x2b3, y2b3
    global x1r1, y1r1, x2r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, y1r3, x2r3, y2r3
    global case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure
    global pionr1, pionr2, pionr3, pion_r_1, pion_r_2, pion_r_3, pionb1, pionb2, pionb3, pion_b_1, pion_b_2, pion_b_3, premiertour
    global fichier_nul, check1, check2, emplacement
    if premiertour == 1:
        tourdejouer, premiertour = 0, 0
    else:
        tourdejouer, premiertour = 1 , 1
    x1, x2, y1, y2=0, 0, 0, 0
    nb_placements_bleu, nb_placements_rouge, phase_placement, jel, selectionner, nb_tours, dx, dy = 0, 0, 1, 0, 0, 1, 0, 0
    case1_libre, case2_libre, case3_libre, case4_libre, case5_libre=True, True, True, True, True
    case6_libre, case7_libre, case8_libre, case9_libre=True, True, True, True
    case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure = -1, -1, -1, -1, -1
    case6_couleure, case7_couleure, case8_couleure, case9_couleure = -1, -1, -1, -1
    pion_b_1, pion_b_2, pion_b_3, pionb1, pionb2, pionb3 = 0, 0, 0, 0, 0, 0
    pion_r_1, pion_r_2, pion_r_3, pionr1, pionr2, pionr3 = 0, 0, 0, 0, 0, 0
    #VARIABLES POSITIONS PIONS BLEU
    x1b1, x2b1, y1b1, y2b1 = 0, 0, 0, 0
    x1b2, x2b2, y1b2, y2b2 = 0, 0, 0, 0
    x1b3, x2b3, y1b3, y2b3 = 0, 0, 0, 0
    #VARIABLES POSITIONS PIONS ROUGE
    x1r1, x2r1, y1r1, y2r1 = 0, 0, 0, 0
    x1r2, x2r2, y1r2, y2r2 = 0, 0, 0, 0
    x1r3, x2r3, y1r3, y2r3 = 0, 0, 0, 0
    canvas.bind('<ButtonPress-1>', ClicCase)
    affichage_rouge.config(text = score_rouge)
    affichage_bleu.config(text = score_bleu)
    fichier_nul = open(r"Fichier_Nul.txt", "w")
    check1, check2 = 0, 1
    ResetPion()


def ResetPion():
    canvas.delete("all")
    ligne1 = canvas.create_line(50, 50, 750, 750)
    ligne2 = canvas.create_line(400, 50, 400, 750)
    ligne3 = canvas.create_line(750, 50, 50, 750)
    ligne4 = canvas.create_line(50, 400, 750, 400)
    ligneh1 = canvas.create_line(50, 50, 750, 50)
    ligneh2 = canvas.create_line(50, 750, 750, 750)
    lignev1 = canvas.create_line(50, 50, 50, 750)
    lignev2 = canvas.create_line(750, 50, 750, 750)


def ConditionVictoire():
    global score_rouge, score_bleu
    if (x1b1 == x1b2 and x1b2 == x1b3 and x1b1 != 0 and y2b1 != y2b2) or (y2b1 == y2b2 and y2b2 == y2b3 and y2b1 != 0 and x1b1 != x1b2):
        score_bleu += 1
        tk.messagebox.showinfo("Manche", "Manche pour les bleus")
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1b1 == 25 and y2b1 == 75) and (x1b2 == 375 and y2b2 == 425) and (x1b3 == 725 and y2b3 == 775)):
        score_bleu += 1
        tk.messagebox.showinfo("Manche", "Manche pour les bleus")
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1b1 == 725 and y2b1 == 75) and (x1b2 == 375 and y2b2 == 425) and (x1b3 == 25 and y2b3 == 775)):
        score_bleu += 1
        tk.messagebox.showinfo("Manche", "Manche pour les bleus")
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif (x1r1 == x1r2 and x1r2 == x1r3 and x1r1 != 0 and y2r1 != y2r2) or (y2r1 == y2r2 and y2r2 == y2r3 and y2r1 != 0 and x1b1 != x1b2):
        score_rouge += 1
        tk.messagebox.showinfo("Manche", "Manche pour les rouges")
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1r1 == 25 and y2r1 == 75) and (x1r2 == 375 and y2r2 == 425) and (x1r3 == 725 and y2r3 == 775)):
        score_rouge += 1
        tk.messagebox.showinfo("Manche", "Manche pour les rouges")
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1r1 == 725 and y2r1 == 75) and (x1r2 == 375 and y2r2 == 425) and (x1r3 == 25 and y2r3 == 775)):
        score_rouge += 1
        tk.messagebox.showinfo("Manche", "Manche pour les rouges")
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    affichage_rouge.config(text = score_rouge)
    affichage_bleu.config(text = score_bleu)
    Victoire()


def Victoire():
    global winner
    if score_bleu == 3 :
        winner = "bleu"
    elif score_rouge == 3 :
        winner = "rouge"
    if winner != "":
        tk.messagebox.showinfo("Gagnant", "Les " + winner + " ont gagnés la partie !")
        canvas.bind('<ButtonPress-1>', NouvellePartie)


def Nul():
    global check1, check2
    cpt = 0
    if nb_tours >= 6:
        liste = str(str(case1_couleure) + str(case2_couleure) + str(case3_couleure) + str(case4_couleure) + str(case5_couleure)
        + str(case6_couleure) + str(case7_couleure) + str(case8_couleure) + str(case9_couleure) + "\n")
        fichier_nul = open(r"Fichier_Nul.txt", "a+")
        fichier_nul.write(liste)
        fichier_nul = open(r"Fichier_Nul.txt", "r")
        lignes = fichier_nul.readlines()
        for i in range(len(lignes)):
            for j in range(len(lignes)):
                if i != j:
                    check1, check2 = lignes[i], lignes[j]
                if check1 == check2:
                    cpt += 1
        cpt /= 2
        if cpt == 3:
            tk.messagebox.showinfo("Nul", "La manche est nul")
            canvas.bind('<ButtonPress-1>', NouvelleManche)


def NouvelleManche(event):
    Initialisation()


def NouvellePartie(event):
    NewGame()


def NewGame():
    global winner, score_bleu, score_rouge
    winner, score_bleu, score_rouge = "", 0, 0
    pos_pionsR.clear()
    Initialisation()


#FENETRE

root = tk.Tk()
root.title("Jeu du Tapatan")
canvas = tk.Canvas(root, width=800, height=800, borderwidth=0, highlightthickness=0, bg="grey")
canvas.pack(padx =1, pady =1)
canvas.grid(column = 0, row = 0, rowspan = 9, columnspan = 9)
canvas.bind('<ButtonPress-1>', ClicCase)
canvas2 = tk.Canvas(root, width=350, height=800, borderwidth=0, highlightthickness=0, bg="grey")
canvas2.grid(column = 10, row = 0, rowspan = 9, columnspan = 3)

ligne1 = canvas.create_line(50, 50, 750, 750)
ligne2 = canvas.create_line(400, 50, 400, 750)
ligne3 = canvas.create_line(750, 50, 50, 750)
ligne4 = canvas.create_line(50, 400, 750, 400)
ligneh1 = canvas.create_line(50, 50, 750, 50)
ligneh2 = canvas.create_line(50, 750, 750, 750)
lignev1 = canvas.create_line(50, 50, 50, 750)
lignev2 = canvas.create_line(750, 50, 750, 750)

frame1 = tk.Frame(root, relief = RIDGE, bd = 12)
frame1.grid(column = 10, row = 1)
frame2 = tk.Frame(root, relief = RIDGE, bd = 12)
frame2.grid(column = 10, row = 3)
frame3 = tk.Frame(root, relief = RIDGE, bd = 12)
frame3.grid(column = 10, row = 5)
frame4 = tk.Frame(root, relief = RIDGE, bd = 12)
frame4.grid(column = 10, row = 7)
frame5 = tk.Frame(root, relief = RIDGE, bd = 12)
frame5.grid(column = 10, row = 2)

score = tk.Label(frame1, width = 14, height = 1, text = "Score", font = ("helvetica", "20"))
score.grid(column = 0, row = 0, columnspan = 4)

rouge = tk.Label(frame1, width = 7, text = "Rouge", font = ("helvetica", "20"))
rouge.grid(column = 0, row = 1)
affichage_rouge = tk.Label(frame1, width = 7, text = score_rouge, font = ("helvetica", "20"))
affichage_rouge.grid(column = 1, row = 1)

bleu = tk.Label(frame1, width = 7, text = "Bleu", font = ("helvetica", "20"))
bleu.grid(column = 0, row = 2, columnspan = 1)
affichage_bleu = tk.Label(frame1, width = 7, text = score_bleu, font = ("helvetica", "20"))
affichage_bleu.grid(column = 1, row = 2)

new_game = tk.Button(frame2, width = 14, text = "Nouvelle Partie", font = ("helvetica", "20"), command = NewGame)
new_game.grid(column = 0, row = 0)

sauvegarde = tk.Button(frame3, width = 14, text= "Sauvegarder", font =("helvetica","20") , command=Sauvegarder)
charger = tk.Button(frame4, width = 14, text= "Charger", font =("helvetica","20"), command=Charger)
sauvegarde.grid(column = 0, row = 3)
charger.grid(column = 0, row = 2)

J_vs_Ia = tk.Button(frame5, width = 14, text = "Joueurs VS IA", font = ("helvetica", "20"), command = joueur_vs_ia)
J_vs_Ia.grid(column = 5, row = 0)

root.mainloop()