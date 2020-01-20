from tkinter import *

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    txtName["bg"] = "#900C3F"
    txtName["fg"] = "blue"
    txtName["text"] = message

window = Tk()
window.geometry("450x300")
window.title("Example 01")

label1 = Label(text = "โปรดใส่ชื่อของคุณ : ")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 20, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

btnOK = Button(text = "ตกลง", command = click)
btnOK.place(x = 300, y = 50, width = 50, height = 25)

txtName = Message(text = "...")
txtName.place(x = 150, y = 150, width = 200, height = 50)
txtName["bg"] = "white"
txtName["fg"] = "black"

window.mainloop()
