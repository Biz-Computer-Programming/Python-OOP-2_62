from tkinter import *

def addition():
    number = edtNumber.get()
    number = int(number)
    result = msgTotal["text"]
    result = int(result)
    total = result + number
    msgTotal["text"] = total

def reset():
    total = 0
    msgTotal["text"] = 0
    edtNumber.delete(0,END)
    edtNumber.focus
    
total = 0
number = 0

window = Tk()
window.title("ผลรวมตัวเลข")
window.geometry("400x300")

lblInput = Label(text="โปรดใส่ตัวเลขเริ่มต้น : ")
lblInput.place(x = 30, y = 30,width = 100,height = 25)

edtNumber = Entry(text = 0)
edtNumber.place(x = 150, y = 30, width = 100, height = 25)
edtNumber["justify"] = "center"
edtNumber.focus()

btnAdd = Button(text = "บวก", command = addition)
btnAdd.place(x = 30, y = 60, width = 50, height = 25)

lblOutput = Label(text = "ผลรวมตัวเลข : ")
lblOutput.place(x = 30, y = 90, width = 150, height = 25)

msgTotal = Message(text = 0)
msgTotal.place(x = 150, y = 90, width = 100, height = 25)

btnClear = Button(text = "ตั้งค่าใหม่", command = reset)
btnClear.place(x = 30, y = 120, width = 50, height = 25)

window.mainloop()
