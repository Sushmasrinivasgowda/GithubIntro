from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
global name,grow_insruction,water_needed,shade_needed,soil_kind,compost,Best_time_to_grow
def Insert_Vegitables():
    name = str(e_name.get())
    grow_insruction = str(e_grow_insruction.get())
    water_needed = str(e_water_needed.get())
    shade_needed = str(e_shade_needed.get())
    soil_kind = str(e_soil_kind.get())
    compost = str(e_soil_kind.get())
    Best_time_to_grow = str(e_Best_time_to_grow.get())
    if (name=="") or (grow_insruction ==" ") or (water_needed =="") or (shade_needed =="")  or (soil_kind =="") or (compost =="") or (Best_time_to_grow ==""):
        MessageBox.showinfo("Insert Status", "All Feilds are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="NewPassword", database="farming_guide")
        cursor = con.cursor()
        cursor.execute("insert into Vegitables values('"+ str(name)+"', '"+ str(grow_insruction) +"', '"+ str(water_needed) +"','"+ str(shade_needed) +"', '"+ str(soil_kind) +"','"+ str(compost) +"','"+ str(Best_time_to_grow) +"')")
        cursor.execute("commit")
        # Text feild
        insert_msg.configure(text="Value Inserted Successfully!")
        insert_msg.place(x=50,y=400)
        Delete_msg.configure(text="")
        update_msg.configure(text="")
def Update_Vegitables():
    con = mysql.connect(host="localhost", user="root", password="NewPassword", database="farming_guide")
    cursor = con.cursor()
    user = e_name.get()
    user1 = e_soil_kind.get()
    # print(user)
    # print(user1)
    cursor.execute(f"UPDATE vegitables SET name='{user}' WHERE soil_kind = '{user1}'")
    con.commit()
    # Text feild
    update_msg.configure(text="Value Updated Successfully!")
    update_msg.place(x=50, y=400)
    insert_msg.configure(text="")
    Delete_msg.configure(text="")

    con.close()


def Delete_Vegitables():
    con = mysql.connect(host="localhost", user="root", password="NewPassword", database="farming_guide")
    cursor = con.cursor()
    user = e_name.get()
    cursor.execute(f"DELETE FROM vegitables where name='{user}'")
    con.commit()
    # Text feild
    Delete_msg.configure(text="Value Deleted Successfully!")
    Delete_msg.place(x=50, y=400)
    insert_msg.configure(text="")
    update_msg.configure(text="")
    con.close()
    # print(user)
window = Tk()
window.title("Farming Guide Adminpage")
window.minsize(width=800, height=600)
window.config(padx=600, pady=200)

#Label
my_label = Label(text="Admin", font=("Arial", 24, "bold"), bg="White")
my_label.config(text="Admin")
my_label.grid(column=0, row=0,columnspan=4)
my_label.place(x=80,y=-30)

#enter
name = Label(window,text="Enter Name :", font=('bold',12))
name.place(x=20,y=30)

grow_insruction = Label(window,text="Enter Grow_insruction :", font=('bold',12))
grow_insruction.place(x=20,y=80)

water_needed = Label(window,text="Enter Water_needed :", font=('bold',12))
water_needed.place(x=20,y=120)

shade_needed = Label(window,text="Enter Shade_needed :", font=('bold',12))
shade_needed.place(x=20,y=160)

soil_kind = Label(window,text="Enter Soil_kind :", font=('bold',12))
soil_kind.place(x=20,y=200)

compost = Label(window,text="Enter Compost :", font=('bold',12))
compost.place(x=20,y=240)

Best_time_to_grow = Label(window,text="Enter Best time to Grow :", font=('bold',12))
Best_time_to_grow.place(x=20,y=280)


# input
e_name = Entry()
e_name.configure(font = 30)
e_name.place(x=200, y=30)
e_grow_insruction = Entry()
e_grow_insruction.configure(font = 30)
e_grow_insruction.place(x=200, y=80)
e_water_needed= Entry()
e_water_needed.configure(font = 30)
e_water_needed.place(x=200, y=120)
e_shade_needed = Entry()
e_shade_needed.configure(font = 30)
e_shade_needed.place(x=200, y=160)
e_soil_kind = Entry()
e_soil_kind.configure(font = 30)
e_soil_kind.place(x=200, y=200)
e_compost = Entry()
e_compost.configure(font = 30)
e_compost.place(x=200, y=240)
e_Best_time_to_grow = Entry()
e_Best_time_to_grow.configure(font = 30)
e_Best_time_to_grow.place(x=200, y=280)

#Buttons
insert = Button(window,text="Insert", font=("italic",15), bg="white", command= Insert_Vegitables)
insert.place(x=100,y=330)

Update = Button(window,text="Update", font=("italic",15), bg="white", command= Update_Vegitables)
Update.place(x=200,y=330)

Delete = Button(window,text="Delete", font=("italic",15), bg="white", command= Delete_Vegitables)
Delete.place(x=300,y=330)

insert_msg = Label(window, font=('bold', 20))
update_msg = Label(window, font=('bold', 20))
Delete_msg = Label(window, font=('bold', 20))

window.mainloop()
