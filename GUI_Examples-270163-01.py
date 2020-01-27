from tkinter import *

def addToList():
    name = txtName.get()
    name_list.insert(END,name)
    txtName.delete(0, END)
    txtName.focus()
def resetInfo():
    name_list.delete(0,END)
    txtName.focus()

window = Tk();
window.title("Name List")
window.geometry("500x300")

label = Label(text="Enter Your name : ")
label.place(x = 20, y = 20, width = 100, height = 25)

txtName = Entry(text = 0)
txtName.place(x = 120, y = 15, width = 150, height = 25)
txtName.focus()

btnConfirm = Button(text = "Add to List", command = addToList)
btnConfirm.place(x = 120, y = 50, width = 100, height = 25)

name_list = Listbox();
name_list.place(x = 120, y = 80, width = 100, height = 100)

btnClear = Button(text = "Reset", command = resetInfo)
btnClear.place(x = 120, y = 180, width = 40, height = 25)

window.mainloop()


