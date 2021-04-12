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

root = tk.Tk()
root.title("Jeu du Tapatan")
canvas = tk.Canvas(root, width=1200, height=1200, borderwidth=0, highlightthickness=0, bg="grey")
canvas.pack(padx =1, pady =1)
canvas.grid()
ligne1 = canvas.create_line(100, 100, 1100, 1100)
ligne2 = canvas.create_line(600, 100, 600, 1100)
ligne3 = canvas.create_line(1100, 100, 100, 1100)
ligne4 = canvas.create_line(100, 600, 1100, 600)
ligneh1 = canvas.create_line(100, 100, 1100, 100)
ligneh2 = canvas.create_line(100, 1100, 1100, 1100)
lignev1 = canvas.create_line(100, 100, 100, 1100)
lignev2 = canvas.create_line(1100, 100, 1100, 1100)
root.mainloop()