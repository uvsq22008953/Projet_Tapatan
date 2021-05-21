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
#VARIABLES POSITIONS PIONS
x1b1=0
x2b1=0
y1b1=0
y2b1=0
""""""
x1b2=0
x2b2=0
y1b2=0
y2b2=0
""""""
x1b3=0
x2b3=0
y1b3=0
y2b3=0
""""""
x1r1=0
x2r1=0
y1r1=0
y2r1=0
""""""
x1r2=0
x2r2=0
y1r2=0
y2r2=0
""""""
x1r3=0
x2r3=0
y1r3=0
y2r3=0
""""""
#VALEURS QUE L'ON VA MODIFIER
x1=0
x2=0
y1=0
y2=0
""""""
nb_tours=1
# 0 si tour des rouges // 1 si tour des bleus
tourdejouer=random.randint(0, 1)
print(tourdejouer)
phase_placement=1
nb_placements_bleu=0
nb_placements_rouge=0
case1_libre=True
case2_libre=True
case3_libre=True
case4_libre=True
case5_libre=True
case6_libre=True
case7_libre=True
case8_libre=True
case9_libre=True
case1_couleure=0
case2_couleure=0
case3_couleure=0
case4_couleure=0
case5_couleure=0
case6_couleure=0
case7_couleure=0
case8_couleure=0
case9_couleure=0
pionr1=0
pionr2=0
pionr3=0
pionb1=0
pionb2=0
pionb3=0

selectionner=0

#FONCTIONS

def positionnement(a, z, e, r):
    global nb_tours
    global tourdejouer
    global selectionner
    global nb_placements_bleu
    global nb_placements_rouge
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
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
                            pion_b_1= canvas.create_rectangle(x1b1, x2b1, y1b1, y2b1, fill="blue", width=2)
                        elif pionb2==1:
                            x1b2=a
                            x2b2=z
                            y1b2=e
                            y2b2=r
                            pion_b_2= canvas.create_rectangle(x1b2, x2b2, y1b2, y2b2, fill="blue", width=2)
                        elif pionb3==1:
                            x1b3=a
                            x2b3=z
                            y1b3=e
                            y2b3=r
                            pion_b_3= canvas.create_rectangle(x1b3, x2b3, y1b3, y2b3, fill="blue", width=2)
                    elif tourdejouer==0:
                        if pionr1==1:
                            x1r1=a
                            x2r1=z
                            y1r1=e
                            y2r1=r
                            pion_r_1= canvas.create_rectangle(x1r1, x2r1, y1r1, y2r1, fill="red", width=2)
                        elif pionr2==1:
                            x1r2=a
                            x2r2=z
                            y1r2=e
                            y2r2=r
                            pion_r_2= canvas.create_rectangle(x1r2, x2r2, y1r2, y2r2, fill="red", width=2)
                        elif pionr3==1:
                            x1r3=a
                            x2r3=z
                            y1r3=e
                            y2r3=r
                            pion_r_3= canvas.create_rectangle(x1r3, x2r3, y1r3, y2r3, fill="red", width=2)


def ClicCase(event):
    global tourdejouer
    global nb_placements_bleu
    global nb_placements_rouge
    global nb_tours
    global case1_libre
    global case2_libre
    global case3_libre
    global case4_libre
    global case5_libre
    global case6_libre
    global case7_libre
    global case8_libre
    global case9_libre
    global case1_couleure
    global case2_couleure
    global case3_couleure
    global case4_couleure
    global case5_couleure
    global case6_couleure
    global case7_couleure
    global case8_couleure
    global case9_couleure
    global selectionner
    if nb_tours<=6:
        if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75:
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
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75:
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
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75:
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
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425:
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
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425:
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
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425:
            #case6
            if tourdejouer==1:
                positionnement(725,375,775,425)
                nb_tours+=1
                case6_couleure=1
                case6_libre=False
            else:
                positionnement(725,375,775,425)
                nb_tours+=1
                case5_couleure=0
                case5_libre=False
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775:
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
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775:
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
        elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775:
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
                positionnement(25,25,75,75)
                selectionner=0  
        elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75 and (selectionner==1 or selectionner==3 or selectionner==5) :
            if case2_libre==False:
                nb_tours+=1
            else:
                positionnement(375,25,425,75)
                selectionner=0
        elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75 and (selectionner==2 or selectionner==6 or selectionner==5):
            if case3_libre==False:
                nb_tours+=1
            else:
                positionnement(725,25,775,75)
                selectionner=0
        elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425 and (selectionner==1 or selectionner==7 or selectionner==5):
            if case4_libre==False:
                nb_tours+=1
            else:
                positionnement(25,375,75,425)
                selectionner=0
        elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425 and (selectionner==1 or selectionner==2 or selectionner==3 or selectionner==4 or selectionner==6 or selectionner==7 or selectionner==8 or selectionner==9):
            if case5_libre==False:
                nb_tours+=1
            else:
                positionnement(375,375,425,425)
                selectionner=0
        elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425 and (selectionner==4 or selectionner==9 or selectionner==5):
            if case6_libre==False:
                nb_tours+=1
            else:
                positionnement(725,375,775,425)
                selectionner=0
        elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775 and (selectionner==4 or selectionner==8 or selectionner==5):
            if case7_libre==False:
                nb_tours+=1
            else:
                positionnement(25,725,75,775)
                selectionner=0
        elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775 and (selectionner==7 or selectionner==9 or selectionner==5):
            if case8_libre==False:
                nb_tours+=1
            else:
                positionnement(375,725,425,775)
                selectionner=0
        elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775 and (selectionner==8 or selectionner==6 or selectionner==5):
            if case9_libre==False:
                nb_tours+=1
            else:
                positionnement(725,725,775,775)
                selectionner=0



def verification1(q,s,d,f):
    global tourdejouer, nb_tours
    global case1_libre, case2_libre, case4_libre, case5_libre
    global case1_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case2_libre==False and case5_libre==False and case4_libre==False:
        nb_tours+=1
    elif case1_libre==False and case1_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=1
            print(57)
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=1
            print(55)
        else :
            pionb3=1
            selectionner=1
            print(56)
    elif case1_libre==False and case1_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=1
            print(58)
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=1
            print(59)
        else :
            pionr3=1
            selectionner=1
            print(60)
    else:
        nb_tours+=1
        print(54)
    
def verification2(q,s,d,f):
    global tourdejouer, nb_tours
    global case1_libre, case2_libre, case3_libre, case5_libre
    global case2_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case1_libre==False and case3_libre==False and case5_libre==False:
        nb_tours+=1
    elif case2_libre==False and case2_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=2
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=2
        else :
            pionb3=1
            selectionner=2
    elif case2_libre==False and case2_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=2
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=2
        else :
            pionr3=1
            selectionner=2
    else:
        nb_tours+=1

def verification3(q,s,d,f):
    global tourdejouer, nb_tours
    global case6_libre, case2_libre, case3_libre, case5_libre
    global case3_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case6_libre==False and case2_libre==False and case5_libre==False:
        nb_tours+=1
    elif case3_libre==False and case3_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=3
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=3
        else :
            pionb3=1
            selectionner=3
    elif case3_libre==False and case3_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=3
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=3
        else :
            pionr3=1
            selectionner=3
    else:
        nb_tours+=1

def verification4(q,s,d,f):
    global tourdejouer, nb_tours
    global case1_libre, case5_libre, case7_libre, case4_libre
    global case4_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case1_libre==False and case5_libre==False and case7_libre==False:
        nb_tours+=1
    elif case4_libre==False and case4_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=4
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=4
        else :
            pionb3=1
            selectionner=4
    elif case4_libre==False and case4_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=4
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=4
        else :
            pionr3=1
            selectionner=4
    else:
        nb_tours+=1

def verification5(q,s,d,f):
    global tourdejouer, nb_tours
    global case1_libre, case2_libre, case3_libre, case4_libre, case5_libre, case6_libre, case7_libre, case8_libre, case9_libre
    global case5_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case1_libre==False and case2_libre==False and case3_libre==False and case4_libre==False and case6_libre==False and case7_libre==False and case8_libre==False and case9_libre==False:
        nb_tours+=1
    elif case5_libre==False and case5_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=5
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=5
        else :
            pionb3=1
            selectionner=5
    elif case5_libre==False and case5_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=5
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=5
        else :
            pionr3=1
            selectionner=5
    else:
        nb_tours+=1

def verification6(q,s,d,f):
    global tourdejouer, nb_tours
    global case3_libre, case5_libre, case6_libre, case9_libre
    global case6_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case3_libre==False and case5_libre==False and case9_libre==False:
        nb_tours+=1
    elif case6_libre==False and case6_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=6
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=6
        else :
            pionb3=1
            selectionner=6
    elif case6_libre==False and case6_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=6
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=6
        else :
            pionr3=1
            selectionner=6
    else:
        nb_tours+=1

def verification7(q,s,d,f):
    global tourdejouer, nb_tours
    global case4_libre, case7_libre, case8_libre, case5_libre
    global case7_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case4_libre==False and case8_libre==False and case5_libre==False:
        nb_tours+=1
    elif case7_libre==False and case7_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=7
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=7
        else :
            pionb3=1
            selectionner=7
    elif case7_libre==False and case7_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=7
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=7
        else :
            pionr3=1
            selectionner=7
    else:
        nb_tours+=1

def verification8(q,s,d,f):
    global tourdejouer, nb_tours
    global case7_libre, case8_libre, case9_libre, case5_libre
    global case8_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case7_libre==False and case9_libre==False and case5_libre==False:
        nb_tours+=1
    elif case8_libre==False and case8_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=8
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=8
        else :
            pionb3=1
            selectionner=8
    elif case8_libre==False and case8_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=8
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=8
        else :
            pionr3=1
            selectionner=8
    else:
        nb_tours+=1


def verification9(q,s,d,f):
    global tourdejouer, nb_tours
    global case6_libre, case8_libre, case9_libre, case5_libre
    global case9_couleure
    global pionr1, pionr2, pionr3
    global pionb1,pionb2,pionb3
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    global selectionner
    if case6_libre==False and case8_libre==False and case5_libre==False:
        nb_tours+=1
    elif case9_libre==False and case9_couleure==1:
        if x1b1==q and x2b1==s and y1b1==d and y2b1==f:
            pionb1=1
            selectionner=9
        elif x1b2==q and x2b2==s and y1b2==d and y2b2==f:
            pionb2=1
            selectionner=9
        else :
            pionb3=1
            selectionner=9
    elif case9_libre==False and case9_couleure==0:
        if x1r1==q and x2r1==s and y1r1==d and y2r1==f:
            pionr1=1
            selectionner=9
        elif x1r2==q and x2r2==s and y1r2==d and y2r2==f:
            pionr2=1
            selectionner=9
        else :
            pionr3=1
            selectionner=9
    else:
        nb_tours+=1

emplacement = [[case1_libre, case2_libre, case3_libre, case4_libre, case5_libre, case6_libre, case7_libre, case8_libre, case9_libre],[case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure]]

def Sauvegarder():
    pickle.dump (emplacement, open("sauvegarde", "wb"))

def Charger ():
    global case1_libre, case2_libre, case3_libre, case4_libre, case5_libre, case6_libre, case7_libre, case8_libre, case9_libre
    global case1_couleure, case2_couleure, case3_couleure, case4_couleure, case5_couleure, case6_couleure, case7_couleure, case8_couleure, case9_couleure
    global nb_tours
    global emplacement
    global x1b1,x2b1,y1b1,y2b1
    global x1b2,x2b2,y1b2,y2b2
    global x1b3,x2b3,y1b3,y2b3
    global x1r1,x2r1,y1r1,y2r1
    global x1r2,x1r2,y1r2,y2r2
    global x1r3,x2r3,y1r3,y2r3
    

    

    emplacement = pickle.load (open("sauvegarde", "rb"))

    if case1_couleure == 0 : 
        positionnement(25,25,75,75)
        pion_b_1 = canvas.create_rectangle(x1b1,x2b1,y1b1,y2b1, fill="blue", width=2)
        nb_tours += 1 
    elif case1_couleure == 1 : 
        positionnement(25,25,75,75) 
        pion_r_1 = canvas.create_rectangle(x1r1,x2r1,y1r1,y2r1, fill="red", width=2)
        nb_tours += 1 

    if case2_couleure == 0 :
        positionnement(375,25,425,75)  
        pion_b_2 = canvas.create_rectangle(x1b2,x2b2,y1b2,y2b2, fill="blue", width=2)
        nb_tours += 1 
    elif case2_couleure == 1 :
        positionnement(375,25,425,75)
        pion_r_2 = canvas.create_rectangle(x1r2,x1r2,y1r2,y2r2, fill="red", width=2)
        nb_tours += 1

    if case3_couleure == 0 :
        positionnement(725,25,775,75)
        pion_b_3 = canvas.create_rectangle(x1b3,x2b3,y1b3,y2b3, fill="blue", width=2)
        nb_tours += 1
    elif case3_couleure == 1 :
        positionnement(725,25,775,75)
        pion_r_3 = canvas.create_rectangle(x1r3,x2r3,y1r3,y2r3, fill="red", width=2)
        nb_tours += 1
    
    if case4_couleure  == 0 :
        positionnement(25,375,75,425)
        pion_b_1 = canvas.create_rectangle(x1b1, x2b1, y1b1, y2b1, fill="blue", width=2)
        nb_tours += 1
    elif case4_couleure  == 1 : 
        positionnement(25,375,75,425)
        pion_r_1 = canvas.create_rectangle(x1r1, x2r1, y1r1, y2r1, fill="red", width=2)
        nb_tours += 1

    if case5_couleure == 0 :
        positionnement(375,375,425,425)
        pion_b_2 = canvas.create_rectangle(x1b2, x2b2, y1b2, y2b2, fill="blue", width=2)
        nb_tours += 1 
    elif case5_couleure  == 1 :
        positionnement(375,375,425,425)
        pion_r_2 = canvas.create_rectangle(x1r2, x2r2, y1r2, y2r2, fill="red", width=2)
        nb_tours += 1

    if case6_couleure  == 0 :
        positionnement(725,375,775,425)
        pion_b_3 = canvas.create_rectangle(x1b3, x2b3, y1b3, y2b3, fill="blue", width=2)
        nb_tours += 1
    elif case6_couleure  == 1 :
        positionnement(725,375,775,425)
        pion_r_3 = canvas.create_rectangle(x1r3, x2r3, y1r3, y2r3, fill="red", width=2)
        nb_tours += 1
    
    if case7_couleure  == 0 :
        positionnement(25,725,75,775)
        pion_b_1 = canvas.create_rectangle(x1b1, x2b1, y1b1, y2b1, fill="blue", width=2)
        nb_tours+= 1
    elif case7_couleure  == 1 :
        positionnement(25,725,75,775)
        pion_r_1 = canvas.create_rectangle(x1r1, x2r1, y1r1, y2r1, fill="red", width=2)
        nb_tours +=1
    
    if case8_couleure  == 0 :
        positionnement(375,725,425,775)
        (375,725,425,775)
        pion_b_2 = canvas.create_rectangle(x1b2, x2b2, y1b2, y2b2, fill="blue", width=2)
        nb_tours += 1
    elif case8_couleure  == 1 :
        positionnement(375,725,425,775)
        (375,725,425,775)
        pion_r_2 = canvas.create_rectangle(x1r2, x2r2, y1r2, y2r2, fill="red", width=2)
        nb_tours += 1

    if case9_couleure == 0 :
        positionnement(725,725,775,775)
        pion_b_3 = canvas.create_rectangle(x1b3, x2b3, y1b3, y2b3, fill="blue", width=2)
        nb_tours += 1
    elif case9_couleure == 1 :
        positionnement(725,725,775,775)
        pion_r_3 = canvas.create_rectangle(x1r3, x2r3, y1r3, y2r3, fill="red", width=2)
        nb_tours += 1
    

    return(emplacement)

root = tk.Tk()
root.title("Jeu du Tapatan")
canvas = tk.Canvas(root, width=800, height=800, borderwidth=0, highlightthickness=0, bg="grey")
canvas.pack(padx =1, pady =1)
canvas.grid()
canvas.bind('<ButtonPress-1>', ClicCase)
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
root.mainloop()