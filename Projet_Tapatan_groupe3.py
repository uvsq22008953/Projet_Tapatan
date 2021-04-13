#########################################
# groupe MPCI 3
# Bertuit Marlone
# Moreira Théo  testdvx
# Lopes Ferreira Lucas 
#Baali Wassim 
#Fernandez Sébastien 
# https://github.com/uvsq22008953/Projet_Tapatan
#########################################

import tkinter as tk

def ClicCase(event):
    #print('coordonnées', event.x, event.y)
    if event.x>=50 and event.x<=150 and event.y>=50 and event.y<=150:
        print('case1')
    elif event.x>=550 and event.x<=650 and event.y>=50 and event.y<=150:
        print('case2')
    elif event.x>=1050 and event.x<=1150 and event.y>=50 and event.y<=150:
        print('case3')
    elif event.x>=50 and event.x<=150 and event.y>=550 and event.y<=650:
        print('case4')
    elif event.x>=550 and event.x<=650 and event.y>=550 and event.y<=650:
        print('case5')
    elif event.x>=1050 and event.x<=1150 and event.y>=550 and event.y<=650:
        print('case6')
    elif event.x>=50 and event.x<=150 and event.y>=1050 and event.y<=1150:
        print('case7')
    elif event.x>=550 and event.x<=650 and event.y>=1050 and event.y<=1150:
        print('case8')
    elif event.x>=1050 and event.x<=1150 and event.y>=1050 and event.y<=1150:
        print('case9')

root = tk.Tk()
root.title("Jeu du Tapatan")
canvas = tk.Canvas(root, width=1200, height=1200, borderwidth=0, highlightthickness=0, bg="grey")
canvas.pack(padx =1, pady =1)
canvas.grid()
canvas.bind('<ButtonPress-1>', ClicCase)
ligne1 = canvas.create_line(100, 100, 1100, 1100)
ligne2 = canvas.create_line(600, 100, 600, 1100)
ligne3 = canvas.create_line(1100, 100, 100, 1100)
ligne4 = canvas.create_line(100, 600, 1100, 600)
ligneh1 = canvas.create_line(100, 100, 1100, 100)
ligneh2 = canvas.create_line(100, 1100, 1100, 1100)
lignev1 = canvas.create_line(100, 100, 100, 1100)
lignev2 = canvas.create_line(1100, 100, 1100, 1100)

root.mainloop()