""""
groupe MPCI 3
Bertuit Marlone
Moreira Théo  testdvx
Lopes Ferreira Lucas 
Baali Wassim 
Fernandez Sébastien 
https://github.com/uvsq22008953/Projet_Tapatan
"""

import tkinter as tk
import random

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
selectionner=0

#FONCTIONS

def positionnement(a, z, e, r):
    global nb_tours
    global tourdejouer
    global selectionner
    global nb_placements_bleu
    global nb_placements_rouge
    if nb_tours>6:
                if selectionner!=0:
                    canvas.coords(pion_selectionne, a, z, e, r)
                    canvas.update()
                    if tourdejouer==0:
                        tourdejouer=1
                    elif tourdejouer==1:
                        tourdejouer=0
    else:
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

#dxgufx



def ClicCase(event):
    #print('coordonnées', event.x, event.y)
    global tourdejouer
    global nb_placements_bleu
    global nb_placements_rouge
    global nb_tours
    #print('premiere valeur de nb_tours est', nb_tours)
    if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75:
            #print('case1')
            print('nb_tours avant vaut', nb_tours)
            positionnement(25,25,75,75)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75:
            #print('case2')
            print('nb_tours avant vaut', nb_tours)
            positionnement(375,25,425,75)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75:
            #print('case3')
            print('nb_tours avant vaut', nb_tours)
            positionnement(725,25,775,75)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425:
            #print('case4')
            print('nb_tours avant vaut', nb_tours)
            positionnement(25,375,75,425)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425:
            #print('case5')
            print('nb_tours avant vaut', nb_tours)
            positionnement(375,375,425,425)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425:
            #print('case6')
            print('nb_tours avant vaut', nb_tours)
            positionnement(725,375,775,425)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775:
            #print('case7')
            print('nb_tours avant vaut', nb_tours)
            positionnement(25,725,75,775)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775:
            #print('case8')
            print('nb_tours avant vaut', nb_tours)
            positionnement(375,725,425,775)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
    elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775:
            #print('case9')
            print('nb_tours avant vaut', nb_tours)
            positionnement(725,725,775,775)
            print('nb_placements_bleu vaut', nb_placements_bleu)
            print('nb_placements_rouge vaut', nb_placements_rouge)
            print('nb_tours après vaut', nb_tours)
            print('tourdejouer vaut', tourdejouer)
            nb_tours+=1
        

        

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


"""
def _create_circle(x, y, x2, y2, **kwargs):
    return canvas.create_oval(x, y, x2, y2, **kwargs)
tk.Canvas.create_circle = _create_circle

pion_test= canvas.create_rectangle(25, 25, 75, 75, fill="blue", width=2)
pion_selectionne=pion_test

pion_b_1= _create_circle(x1b1, x2b1, y1b1, y2b2, fill="blue", width=2)
pion_b_2= _create_circle(x1b2, x1b2, x1b2, x1b2, fill="blue", width=2)
pion_b_3= _create_circle(x1b3, x1b3, x1b3, x1b3, fill="blue", width=2)
pion_r_1= _create_circle(x1r1, x1r1, x1r1, x1r1, fill="red", width=2)
pion_r_2= _create_circle(x1r2, x1r2, x1r2, x1r2, fill="red", width=2)
pion_r_3= _create_circle(x1r3, x1r3, x1r3, x1r3, fill="red", width=2)
"""





root.mainloop()