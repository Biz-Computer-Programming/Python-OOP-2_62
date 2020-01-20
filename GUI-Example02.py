from tkinter import *
import random

def click():
    number1 = random.randint(1,6)
    number2 = random.randint(1,6)
    txt1 = str(number1)
    txt2 = str(number2)
    txt = txt1 + "+" + txt2
    total = str(number1 + number2)
    txt = txt + " = " + total
    answer["bg"] = "#5DADE2"
    answer["fg"] =  "red"
    answer["text"] = txt
    
window = Tk()
window.title("การทอดลูกเต๋า")
window.geometry("400x200")

btnRolling = Button(text = "ทอดลูกเต๋า",command = click)
btnRolling.place(x = 25,y = 25, width = 75, height = 25)

answer = Message(text = "",font=("", 16))
answer.place(x = 10, y = 100, width = 150, height = 70)

window.mainloop()
