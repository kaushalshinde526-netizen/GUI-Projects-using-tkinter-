from tkinter import *
from tkinter import messagebox
import sqlite3 
#database connet kela 
con=sqlite3.connect("students.db")
cur=con.cursor()
cur.execute("create table if not exists student(name text, course text, mobile integer primary key)")
con.commit()

#window banu atta
root=Tk()
root.title("Students Registration System")
root.geometry("400x400")
#save function
def save_data():
    name = entry_name.get()
    course=entery_course.get()
    mobile = entry_mobile.get()
    cur.execute("insert into student values(?,?,?)",(name,course,mobile))
    con.commit()
    messagebox.showinfo("Success", "Data Saved Successfully")
    entry_name.delete(0, END)
    entry_course.delete(0, END)
    entry_mobile.delete(0, END)
#heading
heading = Label(root, text="Student Registration Form")
heading.pack()
#Name
label_name = Label(root, text="Enter Name")
label_name.pack()
entry_name = Entry(root)
entry_name.pack()

#course
label_course = Label(root, text="Enter Course")
label_course.pack()
entry_course = Entry(root)
entry_course.pack()

#mobile
label_mobile = Label(root, text="Enter Mobile")
label_mobile.pack()
entry_mobile = Entry(root)
entry_mobile.pack()

#button
button_save = Button(root, text="Save Data", command=save_data)
button_save.pack()

#main loop
root.mainloop()
