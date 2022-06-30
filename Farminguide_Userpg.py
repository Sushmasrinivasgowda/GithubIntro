import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

con = mysql.connect(host="localhost", user="root", password="NewPassword", database="farming_guide")
cursor = con.cursor()

window = Tk()
window.title("Farming Guide Userpage")

#Image
canvas = Canvas(width=1550, height=600, bg=YELLOW, highlightthickness=0)
plant_img = PhotoImage(file="image3.png")
canvas.create_image(1550, 600, image=plant_img)
name = canvas.create_text(600, 200, text="Enter The Crop:", font=('bold',20))
canvas.grid(column=0, row=0)

kannada = canvas.create_text(830, 25, text="ಕೃಷಿ ಮಾಹಿತಿ ಮಾರ್ಗದರ್ಶಿಗೆ ಸುಸ್ವಾಗತ", font=('bold',35))

canvas.grid(column=0, row=0)


heading = canvas.create_text(840, 70, text="Welcome To Farming Information Guide", font=('bold',30))
canvas.grid(column=0, row=0)

#input
e_name = Entry()
e_name.configure(font = 40)
e_name.place(x=720, y=190)

def show():

    user = e_name.get()
    #print(user)
    cursor.execute(f"SELECT * from vegitables WHERE name='{user}' ")
    records = cursor.fetchall()
    print(records)
    if (user == "") or (records == []):
         MessageBox.showinfo("Search Status","Please enter valid crop")

    for i, (name,grow_insruction,water_needed,shade_needed,soil_kind,compost ,Best_time_to_grow) in enumerate(records, start=1):
        listBox.insert("", "end", values=(name,grow_insruction,water_needed,shade_needed,soil_kind,compost ,Best_time_to_grow))

# show()


#Buttons
Search = Button(window,text="Search", font=("italic",15), bg="white", command=show)
Search.place(x=700,y=300)

cols = ('name','grow_insruction','water_needed','shade_needed','soil_kind','compost ','Best_time_to_grow')
listBox = ttk.Treeview(window,columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.place(x=70, y=600)


window.mainloop()
