import tkinter as tk
import numpy as np
from tkinter import messagebox
import random
import time
''' Matrice sudoku random '''
P = [
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
     


sudoku=tk.Tk()
sudoku.title('Sudoku - by Abdenour')


sudoku.iconphoto(True, tk.PhotoImage(file='sudoku1.gif'))

labelgame=tk.Label(sudoku,text='Game ON')
labelgame.pack(side='top')
'''
canevas=tk.LabelFrame(sudoku,text='Sudoku',width=500, height=500)
canevas.pack()
'''
canevas=tk.Canvas(sudoku,width=450,height=450,bg='green')
canevas.pack()
canevas.create_line(200,0,200,400,fill='red')

'''random matrix
En cours 
'''

class entryy:
    def __init__(self, master,i,j):
        entry_text = tk.StringVar()
        P = [
        [7,8,4,  1,5,9,  3,2,6],
        [5,3,9,  6,7,2,  8,4,1],
        [6,1,2,  4,3,8,  7,5,9],

        [9,2,8,  7,1,5,  4,6,3],
        [3,5,7,  8,4,6,  1,9,2],
        [4,6,1,  9,2,3,  5,8,7],

        [8,7,6,  3,9,4,  2,1,5],
        [2,4,3,  5,6,1,  9,7,8],
        [1,9,5,  2,8,7,  6,3,4]
        ]

        M=np.matrix(P)          
        entry_widget = tk.Entry(master, width = 20, textvariable = entry_text) 
        entry_widget.grid(row=i, column=j)
        
        entry_widget.insert(M[i-1,j-1],int(M[i-1,j-1]))
        def integer(entry_text):
            try:
                int(entry_text.get())
                if int(entry_text.get()) > 0 :
                    entry_text.set(entry_text.get()[-1])
                if int(entry_text.get())==0:
                    messagebox.showinfo('Value Error','Caracters & Zero are not accepted') 
                    entry_text.set('')
                
            except ValueError:
                messagebox.showinfo('Value Error','Caracters & Zero are not accepted')      
                entry_text.set('')   
        entry_text.trace("w", lambda *args: integer(entry_text))
      



def table(caneva):
    cells={}
    entry_equipes=[]  
    for i in range(1,10): #Rows
        for j in range(1,10): #Columns
            print("valeur de ", i)
            print("valeur de ", j)

            b=entryy(canevas,i,j)        
            entry_equipes.append(b)




def about():
    messagebox.showinfo('Developper','Developped by Abdenour DELLIL')
"""
def shuffle():
    x = list(9)
    random.shuffle(9)
    return x
"""
sudoku_check=tk.Button(sudoku, text='check game')
sudoku_check.pack(padx=0,pady=15,fill='x')


sudoku_about=tk.Button(sudoku,text="About",command=about)
sudoku_about.pack(padx=0,pady=16,fill='x')

sudoku_newgame=tk.Button(sudoku,text="New Game")
sudoku_newgame.pack(padx=0,pady=17,fill='x')

sudoku_exit=tk.Button(sudoku,text="Exit",command=sudoku.destroy)
sudoku_exit.pack(side="bottom",padx=0,pady=17,fill="x")

table(canevas)

sudoku.configure(width=400,height=400,bg="#FFA07A")


start = time.time()
end = time.time()
print("Time to run: {}".format(end - start))

sudoku.mainloop()
