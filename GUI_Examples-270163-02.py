from tkinter import *

def convertToMiles():
    km = txtValue.get()
    km = float(km)
    result = round(km * 0.6214,2)
    string = str(result) + " ไมล์"
    msgResult["text"] = string

def convertToKm():
    mile = txtValue.get()
    mile = float(mile)
    result = round(mile * 1.6093,2)
    string = str(result) + " กิโลเมตร"
    msgResult["text"] = string
    
window = Tk()
window.title("แปลงค่า กิโลเมตร<>ไมล์")
window.geometry("300x200")

lblConvert = Label(text = "โปรดใส่ค่าที่ต้องการเปลี่ยน : ")
lblConvert.place(x = 30, y = 20)

txtValue = Entry(text = "")
txtValue.place(x = 30,y = 45, width = 100, height = 25)
txtValue["justify"] = "center"
txtValue.focus()

btnToMiles = Button(text = "แปลงจากกิโลเมตรเป็นไมล์", command = convertToMiles)
btnToMiles.place(x = 20, y = 75, width = 130, height = 25)

btnToKm = Button(text = "แปลงจากไมล์เป็นกิโลเมตร", command = convertToKm)
btnToKm.place(x = 160, y = 75, width = 130, height = 25)

msgResult = Message(text = 0)
msgResult.place(x = 30, y = 150, width = 200, height = 25)
msgResult["bg"] = "yellow"
msgResult["fg"] = "red"

window.mainloop()
