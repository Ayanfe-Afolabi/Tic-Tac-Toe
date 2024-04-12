import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title( "TIC-TAC-TOE" )

digits = [1,2,3,4,5,6,7,8,9]
mark = str()
count = 0
panels = [ 'panel',  'g0.0',  'g0.1', 'g0.2', 'g1.0', 'g1.1', 'g1.2', 'g2.0', 'g2.1', 'g2.2' ]

#win function has to know 10 situations for each x and o, 20 functions is redundant.How can i do that in less?


    
    
def checker(b):
    global digits 
    global mark
    global count
    #9 if statements are too much
    while b['text'] == ' ':
        count+=1
        if count % 2 == 0:
            b['text'] = 'O'
        elif count % 2 == 1:
            b['text'] = 'X'
        elif b in digits:
                digits.remove(b)
#check if digit['text'] works
    
b1= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6, command=lambda: checker(b1))
b2= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b2))
b3= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b3))

b4= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b4))
b5= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b5))
b6= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b6))

b7= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b7))
b8= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b8))
b9= Button(window, text=' ', font= ('Helvetica',20 ), height=3, width=6,command=lambda: checker(b9))

#grid of buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

window.mainloop()
