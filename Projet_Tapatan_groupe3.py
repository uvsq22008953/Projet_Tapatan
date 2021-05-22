""""
groupe MPCI 3
Bertuit Marlone
Moreira Théo  testdvx
Lopes Ferreira Lucas test
Baali Wassim 
Fernandez Sébastien 
https://github.com/uvsq22008953/Projet_Tapatan
"""

import tkinter as tk
import random
import pickle
from tkinter.constants import RIDGE
from tkinter import messagebox

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
winner, score_bleu, score_rouge, score_perdant, score_gagnant = "", 0, 0, 0, 0


emplacement = [case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure]

#FONCTIONS

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
                                print("gg")
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


def ClicCase(event):
    global tourdejouer, nb_placements_bleu, nb_placements_rouge, nb_tours, selectionner
    global case1_libre, case2_libre, case3_libre, case4_libre, case5_libre
    global case6_libre, case7_libre, case8_libre, case9_libre
    global case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure
    global case6_couleure, case7_couleure, case8_couleure, case9_couleure
    if nb_tours<=6:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75:
            #case1
            if tourdejouer==1:
                positionnement(25,25,75,75)
                nb_tours+=1
                case1_couleure=1
                emplacement [0] = 1
                case1_libre=False
            else:
                positionnement(25,25,75,75)
                nb_tours+=1
                case1_couleure=0
                emplacement [0] = 0
                case1_libre=False
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75:
            #case2
            if tourdejouer==1:
                positionnement(375,25,425,75)
                nb_tours+=1
                case2_couleure=1
                emplacement [1] = 1
                case2_libre=False
            else:
                positionnement(375,25,425,75)
                nb_tours+=1
                case2_couleure=0
                emplacement [1] = 0
                case2_libre=False
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75:
            #case3
            if tourdejouer==1:
                positionnement(725,25,775,75)
                nb_tours+=1
                case3_couleure=1
                emplacement [2] = 1
                case3_libre=False
            else:
                positionnement(725,25,775,75)
                nb_tours+=1
                case3_couleure=0
                emplacement [2] = 0
                case3_libre=False
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425:
            #case4
            if tourdejouer==1:
                positionnement(25,375,75,425)
                nb_tours+=1
                case4_couleure=1
                emplacement [3] = 1
                case4_libre=False
            else:
                positionnement(25,375,75,425)
                nb_tours+=1
                case4_couleure=0
                emplacement [3] = 0
                case4_libre=False
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425:
            #case5
            if tourdejouer==1:
                positionnement(375,375,425,425)
                nb_tours+=1
                case5_couleure=1
                emplacement [4] = 1
                case5_libre=False
            else:
                positionnement(375,375,425,425)
                nb_tours+=1
                case5_couleure=0
                emplacement [4] = 0
                case5_libre=False
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425:
            #case6
            if tourdejouer==1:
                positionnement(725,375,775,425)
                nb_tours+=1
                case6_couleure=1
                emplacement [5] = 1
                case6_libre=False
            else:
                positionnement(725,375,775,425)
                nb_tours+=1
                case6_couleure=0
                emplacement [5] = 0
                case6_libre=False
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775:
            #case7
            if tourdejouer==1:
                positionnement(25,725,75,775)
                nb_tours+=1
                case7_couleure=1
                emplacement [6] = 1
                case7_libre=False
            else:
               positionnement(25,725,75,775)
               nb_tours+=1
               case7_couleure=0
               emplacement [6] = 0
               case7_libre=False 
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775:
            #case8
            if tourdejouer==1:
                positionnement(375,725,425,775)
                nb_tours+=1
                case8_libre=False
                case8_couleure=1
                emplacement [7] = 1
            else:
                positionnement(375,725,425,775)
                nb_tours+=1
                case8_libre=False
                case8_couleure=0
                emplacement [7] = 0
        elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775:
            #case9
            if tourdejouer==1:
                positionnement(725,725,775,775)
                nb_tours+=1
                case9_couleure=1
                emplacement [8] = 1
                case9_libre=False
            else:
                positionnement(725,725,775,775)
                nb_tours+=1
                case9_couleure=0
                emplacement [8] = 0
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
                print("fut")
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75:
            if case3_libre==False and case3_couleure==tourdejouer:
                verification3(725,25,775,75)
                nb_tours+=1
                print("42euh")
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
                print("ash22")
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
                print("ash223")
            else:
                nb_tours=nb_tours+2
                print("ash24")
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
            print("fr")
            if case6_libre==False:
                nb_tours+=1
                print("fr")
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=1
            case1_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=1
            case1_libre=True
            dx=q
            dy=s
    elif case1_libre==False and case1_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=1
            case1_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=1
            case1_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=1
            case1_libre=True
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=2
            case2_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=2
            case2_libre=True
            dx=q
            dy=s
    elif case2_libre==False and case2_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=2
            case2_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=2
            case2_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=2
            case2_libre=True
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=3
            case3_libre=True
            dx=q
            dy=s
            print(44)
        else :
            pionb3=1
            selectionner=3
    elif case3_libre==False and case3_couleure== 0:
            case3_libre=True
            dx=q
            dy=s
    elif case3_libre==False and case3_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=3
            case3_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=3
            case3_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=3
            case3_libre=True
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=4
            case4_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=4
            case4_libre=True
            dx=q
            dy=s
    elif case4_libre==False and case4_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=4
            case4_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=4
            case4_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=4
            case4_libre=True
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
    print("capasse")
    if case1_libre==False and case2_libre==False and case3_libre==False and case4_libre==False and case6_libre==False and case7_libre==False and case8_libre==False and case9_libre==False:
        nb_tours+=1
    elif case5_libre==False and case5_couleure==1:
        print(923)
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=5
            case5_libre=True
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
            dx=q
            dy=s
    elif case5_libre==False and case5_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=5
            case5_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=5
            case5_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=5
            case5_libre=True
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=6
            case6_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=6
    elif case6_libre==False and case6_couleure== 0:
            case6_libre=True
            dx=q
            dy=s
    elif case6_libre==False and case6_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=6
            case6_libre=True
            dx=q
            dy=s
            print("capaaaas")
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=6
            case6_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=6
            case6_libre=True
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=7
            case7_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=7
            case7_libre=True
            dx=q
            dy=s
    elif case7_libre==False and case7_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=7
            case7_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=7
            case7_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=7
            case7_libre=True
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=8
            case8_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=8
            case8_libre=True
            dx=q
            dy=s
    elif case8_libre==False and case8_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=8
            case8_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=8
            case8_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=8
            case8_libre=True
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
            dx=q
            dy=s
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=9
            case9_libre=True
            dx=q
            dy=s
        else :
            pionb3=1
            selectionner=9
            case9_libre=True
            dx=q
            dy=s
    elif case9_libre==False and case9_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=9
            case9_libre=True
            dx=q
            dy=s
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=9
            case9_libre=True
            dx=q
            dy=s
        else :
            pionr3=1
            selectionner=9
            case9_libre=True
            dx=q
            dy=s
    else:
        nb_tours+=1

emplacement = [case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure]

def Sauvegarder():
    pickle.dump (emplacement, open("sauvegarde", "wb"))

def Charger ():
    global nb_tours
    global emplacement
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3

    emplacement = pickle.load (open("sauvegarde", "rb"))

    if emplacement[0] == 0: 
        positionnement(25,25,75,75)
        canvas.create_rectangle(x1b1,x2b1,y1b1,y2b1, fill="blue", width=2)
        nb_tours += 1 
    if emplacement[0] == 1 : 
        positionnement(25,25,75,75)
        canvas.create_rectangle(x1r1,x2r1,y1r1,y2r1, fill="red", width=2)
        nb_tours += 1 
  

    if emplacement[1] == 0 :  
        positionnement(375,25,425,75)
        canvas.create_rectangle(x1b2,x2b2,y1b2,y2b2, fill="blue", width=2)
        nb_tours += 1 
    if emplacement[1] == 1 :
        positionnement(375,25,425,75)
        canvas.create_rectangle(x1r2,x1r2,y1r2,y2r2, fill="red", width=2)
        nb_tours += 1
   

    if emplacement[2] == 0:
        positionnement(725,25,775,75)
        canvas.create_rectangle(x1b3,x2b3,y1b3,y2b3, fill="blue", width=2)
        nb_tours += 1
    if emplacement[2]== 1:
        positionnement(725,25,775,75)
        canvas.create_rectangle(x1r3,x2r3,y1r3,y2r3, fill="red", width=2)
        nb_tours += 1
  
    
    if emplacement[3]  == 0:
        positionnement(25,375,75,425)
        canvas.create_rectangle(x1b1,x2b1,y1b1,y2b1, fill="blue", width=2)
        nb_tours += 1
    if emplacement[3]  == 1: 
        positionnement(25,375,75,425)
        canvas.create_rectangle(x1r1,x2r1,y1r1,y2r1, fill="red", width=2)
        nb_tours += 1
 

    if emplacement[4] == 0 :
        positionnement(375,375,425,425)
        canvas.create_rectangle(x1b2,x2b2,y1b2,y2b2, fill="blue", width=2)
        nb_tours += 1 
    if emplacement[4]  == 1:
        positionnement(375,375,425,425)
        canvas.create_rectangle(x1r2,x1r2,y1r2,y2r2, fill="red", width=2)
        nb_tours += 1
   

    if emplacement[5]  == 0 :
        positionnement(725,375,775,425)
        canvas.create_rectangle(x1b3,x2b3,y1b3,y2b3, fill="blue", width=2)
        nb_tours += 1
    if emplacement[5]  == 1:
        positionnement(725,375,775,425)
        canvas.create_rectangle(x1r3,x2r3,y1r3,y2r3, fill="red", width=2)
        nb_tours += 1
  
    
    if emplacement[6]  == 0:
        positionnement(25,725,75,775)
        canvas.create_rectangle(x1b1,x2b1,y1b1,y2b1, fill="blue", width=2)
        nb_tours+= 1
    if emplacement[6]  == 1 :
        positionnement(25,725,75,775)
        canvas.create_rectangle(x1r1,x2r1,y1r1,y2r1, fill="red", width=2)
        nb_tours +=1
 

    if emplacement[7]  == 0:
        positionnement(375,725,425,775)
        canvas.create_rectangle(x1b2,x2b2,y1b2,y2b2, fill="blue", width=2)
        nb_tours += 1
    if emplacement[7]  == 1 :
        positionnement(375,725,425,775)
        canvas.create_rectangle(x1r2,x1r2,y1r2,y2r2, fill="red", width=2)
        nb_tours += 1
   

    if emplacement[8] == 0 :
        positionnement(725,725,775,775)
        canvas.create_rectangle(x1b3,x2b3,y1b3,y2b3, fill="blue", width=2)
        nb_tours += 1
    if emplacement[8] == 1:
        positionnement(725,725,775,775)
        canvas.create_rectangle(x1r3,x2r3,y1r3,y2r3, fill="red", width=2)
        nb_tours += 1

    return(emplacement)

def Initialisation():
    global x1, x2, y1, y2, nb_tours, tourdejouer, phase_placement, nb_placements_rouge, nb_placements_bleu, case1_libre, case2_libre, case3_libre
    global case4_libre, case5_libre, case6_libre, case7_libre, case8_libre, case9_libre, selectionner, winner, score_bleu, score_rouge, jel, dx, dy, canvas
    global x1b1, x2b1, y1b1, y2b1, x1b2, x2b2, y1b2, y2b2, x1b3, y1b3, x2b3, y2b3
    global x1r1, y1r1, x2r1, y2r1, x1r2, x2r2, y1r2, y2r2, x1r3, y1r3, x2r3, y2r3
    global case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure
    global pionr1, pionr2, pionr3, pion_r_1, pion_r_2, pion_r_3, pionb1, pionb2, pionb3, pion_b_1, pion_b_2, pion_b_3 , score_perdant, score_gagnant, premiertour
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
    if (x1b1 == x1b2 and x1b2 == x1b3 and x1b1 != 0) or (y2b1 == y2b2 and y2b2 == y2b3 and y2b1 != 0):
        score_bleu += 1
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1b1 == 25 and y2b1 == 75) and (x1b2 == 375 and y2b2 == 425) and (x1b3 == 725 and y2b3 == 775)):
        score_bleu += 1
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1b1 == 725 and y2b1 == 75) and (x1b2 == 375 and y2b2 == 425) and (x1b3 == 25 and y2b3 == 775)):
        score_bleu += 1
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif (x1r1 == x1r2 and x1r2 == x1r3 and x1r1 != 0) or (y2r1 == y2r2 and y2r2 == y2r3 and y2r1 != 0):
        score_rouge += 1
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1r1 == 25 and y2r1 == 75) and (x1r2 == 375 and y2r2 == 425) and (x1r3 == 725 and y2r3 == 775)):
        score_rouge += 1
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    elif ((x1r1 == 725 and y2r1 == 75) and (x1r2 == 375 and y2r2 == 425) and (x1r3 == 25 and y2r3 == 775)):
        score_rouge += 1
        canvas.bind('<ButtonPress-1>', NouvelleManche)
    affichage_rouge.config(text = score_rouge)
    affichage_bleu.config(text = score_bleu)
    print("score bleu ", score_bleu, "   score rouge ", score_rouge)
    print("x1b1 ", x1b1, "x1b2 ", x1b2, "x1b3 ", x1b3)
    print("y2b1 ", y2b1, "y2b2 ", y2b2, "y2b3 ", y2b3)
    Victoire()


def Victoire():
    global winner, score_bleu, score_rouge, score_gagnant, score_perdant
    if score_bleu == 3 :
        winner = "bleu"
        score_gagnant = score_bleu
        score_perdant = score_rouge
    elif score_rouge == 3 :
        winner = "rouge"
        score_gagnant = score_rouge
        score_perdant = score_bleu
    if winner != "":
        tk.messagebox.showinfo("Gagnant", "Les " + winner + " ont gagnés")
        canvas.bind('<ButtonPress-1>', NouvellePartie)


def NouvelleManche(event):
    Initialisation()


def NouvellePartie(event):
    NewGame()


def NewGame():
    global winner, score_bleu, score_rouge, score_perdant, score_gagnant
    winner, score_bleu, score_rouge, score_perdant, score_gagnant = "", 0, 0, 0, 0
    Initialisation()


def Nul():
    if nb_tours > 6:
        liste = []
        fichier_nul = open(r"Fichier_Nul", "a")
        fichier_nul.write(liste)

    pass



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
sauvegarde = tk.Button(root, text= "Sauvegarder", bg = "grey", command=Sauvegarder)
charger = tk.Button(root, text= "Charger", bg = "grey", command=Charger)
canvas.grid(row=0, column=0, columnspan=4, rowspan=6)
sauvegarde.grid(row=6, column=1)
charger.grid(row=6, column=2)

frame1 = tk.Frame(root, relief = RIDGE, bd = 12)
frame1.grid(column = 10, row = 2)
frame2 = tk.Frame(root, relief = RIDGE, bd = 12)
frame2.grid(column = 10, row = 4)

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


root.mainloop()
