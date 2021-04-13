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

def ClicCase(event):
    #print('coordonnées', event.x, event.y)
    if event.x>=25 and event.x<=75 and event.y>=25 and event.y<=75:
        print('case1')
    elif event.x>=375 and event.x<=425 and event.y>=25 and event.y<=75:
        print('case2')
    elif event.x>=725 and event.x<=775 and event.y>=25 and event.y<=75:
        print('case3')
    elif event.x>=25 and event.x<=75 and event.y>=375 and event.y<=425:
        print('case4')
    elif event.x>=375 and event.x<=425 and event.y>=375 and event.y<=425:
        print('case5')
    elif event.x>=725 and event.x<=775 and event.y>=375 and event.y<=425:
        print('case6')
    elif event.x>=25 and event.x<=75 and event.y>=725 and event.y<=775:
        print('case7')
    elif event.x>=375 and event.x<=425 and event.y>=725 and event.y<=775:
        print('case8')
    elif event.x>=725 and event.x<=775 and event.y>=725 and event.y<=775:
        print('case9')

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

root.mainloop()