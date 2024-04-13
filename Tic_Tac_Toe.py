import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title( "TIC-TAC-TOE" )

digits = [1,2,3,4,5,6,7,8,9]
mark = str()
count = 0
panels = [ 'panel',  'g0.0',  'g0.1', 'g0.2', 'g1.0', 'g1.1', 'g1.2', 'g2.0', 'g2.1', 'g2.2' ]

def disable_all_buttons():
    b1.config(state="disabled")
    b2.config(state="disabled")
    b3.config(state="disabled")
    b4.config(state="disabled")
    b5.config(state="disabled")
    b6.config(state="disabled")
    b7.config(state="disabled")
    b8.config(state="disabled")
    b9.config(state="disabled")

   
#win function has to know 8 situations for each x and o, 16 functions is redundant.How can i do that in less?
#if i can establish each combo as horizontal vertical and diagonal i can get it down to 6 combinations. 3 for x and 3 for o

def win():
    #can i make a dictionary or an array that inputs each winning combo as 1 then runa while loopthrough it?
   
    #if b1['text'] == b2['text'] == b3['text']:
    #because b1 text and  b2 text are both space it won't work
        #  b1.config(bg='blue'), b2.config(bg='blue'), b3.config(bg='blue')    
         
    if b1['text']== b2['text']== b3['text'] !=' ':
            b1.config(bg='blue'), b2.config(bg='blue'),b3.config(bg='blue')
            if b1['text'] == b2['text'] == b3['text']=='X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()

        
    elif b4['text']== b5['text']== b6['text'] != ' ':
            b4.config(bg='blue'), b5.config(bg='blue'),b6.config(bg='blue')
            if b4['text'] == b5['text'] == b6['text'] == 'X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()
        
    elif b7['text']== b8['text']== b9['text'] != ' ':
            b7.config(bg='blue'), b8.config(bg='blue'),b9.config(bg='blue')
            if b7['text'] == b8['text'] == b9['text']== 'X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()
    elif b1['text']== b4['text']== b7['text'] !=' ':
            b1.config(bg='blue'), b4.config(bg='blue'),b7.config(bg='blue')
            if b1['text'] ==b4['text'] == b7['text'] == 'X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()
    elif b2['text']== b5['text']== b8['text'] !=' ':
            b2.config(bg='blue'), b5.config(bg='blue'),b8.config(bg='blue')
            if b2['text'] ==b5['text'] == b8['text'] == 'X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()
    elif b3['text']== b6['text']== b9['text'] != ' ':
            b3.config(bg='blue'), b6.config(bg='blue'),b9.config(bg='blue')
            if b3['text'] == b6['text'] == b9['text'] =='X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()
    elif b1['text']== b5['text']== b9['text'] !=' ':
            b1.config(bg='blue'), b5.config(bg='blue'),b9.config(bg='blue')
            if b1['text'] == b5['text']== b9['text'] == 'X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()
    elif b3['text']== b5['text']== b7['text'] != ' ':
            b3.config(bg='blue'), b5.config(bg='blue'),b7.config(bg='blue')
            if b3['text'] == b5['text'] ==b7['text']== 'X':
                 messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player1 wins :-) ")
                 disable_all_buttons()
            else:
                messagebox.showinfo("Tic Tac Toe", "Congrats!!! Player2 wins :-) ")
                disable_all_buttons()
    
    else:
        if count == 9:
            messagebox.showinfo("Tic Tac Toe", "It's a Tie:-( \n Try Again")
            disable_all_buttons()


            
    
def checker(b):
    global digits 
    global mark
    global count
    #9 if statements are too much. I could not lower it 
    while b['text'] == ' ':
        count+=1
        if count % 2 == 0:
            b['text'] = 'O'
        elif count % 2 == 1:
            b['text'] = 'X'
        elif b in digits:
                digits.remove(b)
    win()
    
#check if digit['text'] works. it did not :-(
#changing it to represent buttons works
    
#Reset function
def reset():  
    global b1, b2, b3, b4, b5 , b6, b7, b8, b9
    global count, digits
    count = 0 
    b1['text'] = b2['text'] = b3['text']= b4['text']=b5 ['text']=b6 ['text'] =b7 ['text'] =b8 ['text'] =b9['text'] = ' '
    b1.config(state= 'active'), b1.config(state= 'active'), b1.config(state= 'active'), b1.config(state= 'active'), b2.config(state= 'active'), b3.config(state= 'active'), b4.config(state= 'active'), b5.config(state= 'active'), b6.config(state= 'active'),b7.config(state= 'active'),b8.config(state= 'active'),b9.config(state= 'active')
    b1.config(bg="SystemButtonFace"),b2.config(bg="SystemButtonFace"),b3.config(bg="SystemButtonFace"), b4.config(bg="SystemButtonFace"),b5.config(bg="SystemButtonFace"),b6.config(bg="SystemButtonFace"),b6.config(bg="SystemButtonFace"),b7.config(bg="SystemButtonFace"),b8.config(bg="SystemButtonFace"),b9.config(bg="SystemButtonFace")


#buttons
b1= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6, command=lambda: checker(b1))
b2= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b2))
b3= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b3))

b4= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b4))
b5= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b5))
b6= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b6))

b7= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b7))
b8= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b8))
b9= Button(window, text=' ', font= ('Helvetica',30 ), bg='SystemButtonFace', height=3, width=6,command=lambda: checker(b9))

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

#Menu 
menu_set = Menu(window)
window.config(menu=menu_set)

menu_options =Menu(menu_set, tearoff=False)
menu_set.add_cascade(label= "Options", menu = menu_options)
menu_options.add_command(label='New Game', command=reset )

window.mainloop()
