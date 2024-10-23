import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Autorização extraoficial')
root.geometry('600x600')
root.configure(background='#EE82EE')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width() - 10)
        y = random.randint(0, root.winfo_height() - button_1.winfo_height() - 10)
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo(
        'Essa é a minha super', 'Essa super não é uma supervisora, é uma prefeita'
    )        

def denied():
    button_1.destroy()

margin = Canvas(root, width=500, bg= '#EE82EE', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#EE82EE', text= 'Posso sair mais cedo, libera ai?',
                fg= '#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#F5DEB3', command=denied,
                     relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 =tk.Button(root, text='Sim', bg='#F5DEB3', relief=RIDGE,
                    bd=3, command=accepted, font=('Montserrat', 14, 'bold')) 
button_2.pack()

root.mainloop()