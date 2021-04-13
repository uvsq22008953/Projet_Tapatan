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
nb_tours=0
tourdejouer=0
# 0 si tour des rouges // 1 si tour des bleus
premier_tour=random.randint(0,2)
if premier_tour==0:
    tourdejouer=0
    #ROUGES COMMENCENT
else:
    tourdejouer=1
    #BLEUS COMMENCENT
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

#FONCTIONS
def ClicCase(event):
    #print('coordonnées', event.x, event.y)
    if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75:
        #print('case1')
        canvas.coords(pion_selectionne, 25, 25, 75, 75)
        canvas.update()
        selectionner=0
    elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75:
        #print('case2')
        canvas.coords(pion_selectionne, 375, 25, 425, 75)
        canvas.update()
        selectionner=0
    elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75:
        #print('case3')
        canvas.coords(pion_selectionne, 725, 25, 775, 75)
        canvas.update()
        selectionner=0
    elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425:
        #print('case4')
        canvas.coords(pion_selectionne, 25, 375, 75, 425)
        canvas.update()
        selectionner=0
    elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425:
        #print('case5')
        canvas.coords(pion_selectionne, 375, 375, 425, 425)
        canvas.update()
        selectionner=0
    elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425:
        #print('case6')
        canvas.coords(pion_selectionne, 725, 375, 775, 425)
        canvas.update()
        selectionner=0
    elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775:
        #print('case7')
        canvas.coords(pion_selectionne, 25, 725, 75, 775)
        canvas.update()
        selectionner=0
    elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775:
        #print('case8')
        canvas.coords(pion_selectionne, 375, 725, 425, 775)
        canvas.update()
        selectionner=0
    elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775:
        #print('case9')
        canvas.coords(pion_selectionne, 725, 725, 775, 775)
        canvas.update()
        selectionner=0

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
"""
pion_test= canvas.create_rectangle(25, 25, 75, 75, fill="blue", width=2)
pion_selectionne=pion_test
"""
pion_b_1= _create_circle(x1b1, x2b1, y1b1, y2b2, fill="blue", width=2)
pion_b_2= _create_circle(x1b2, x1b2, x1b2, x1b2, fill="blue", width=2)
pion_b_3= _create_circle(x1b3, x1b3, x1b3, x1b3, fill="blue", width=2)
pion_r_1= _create_circle(x1r1, x1r1, x1r1, x1r1, fill="red", width=2)
pion_r_2= _create_circle(x1r2, x1r2, x1r2, x1r2, fill="red", width=2)
pion_r_3= _create_circle(x1r3, x1r3, x1r3, x1r3, fill="red", width=2)
"""





root.mainloop()