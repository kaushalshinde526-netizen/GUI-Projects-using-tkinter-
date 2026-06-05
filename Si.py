from tkinter import *

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("700x700+300+20")
root.resizable(False, False)

f = ("Times New Roman", 30, "bold")

def find():

    try:
        p = float(ent_principal.get())
    except ValueError:
        msg = "Principal amount should be numbers only"
        lab_msg.configure(text=msg, fg="red")
        return

    if p < 1000:
        msg = "Principal amount should be minimum 1000"
        lab_msg.configure(text=msg, fg="red")
        return

    try:
        r = float(ent_rate.get())
    except ValueError:
        msg = "Rate should be numbers only"
        lab_msg.configure(text=msg, fg="red")
        return

    if r <= 0:
        msg = "Rate should be minimum 0.1"
        lab_msg.configure(text=msg, fg="red")
        return

    try:
        t = float(ent_time.get())
    except ValueError:
        msg = "Time should be numbers only"
        lab_msg.configure(text=msg, fg="red")
        return

    if t <= 0:
        msg = "Time should be minimum 0.1"
        lab_msg.configure(text=msg, fg="red")
        return

    si = (p * r * t) / 100

    msg = "Simple Interest = " + str(round(si, 2))

    lab_msg.configure(text=msg, fg="blue")


lab_header = Label(root,
                   text="Simple Interest Calculator",
                   font=f)
lab_header.pack(pady=20)

lab_principal = Label(root,
                      text="Enter Principal Amount",
                      font=f,
                      fg="orange")

ent_principal = Entry(root, font=f)

lab_principal.pack(pady=10)
ent_principal.pack(pady=10)

lab_rate = Label(root,
                 text="Enter Rate of Interest",
                 font=f)

ent_rate = Entry(root,
                 font=f,
                 fg="black")

lab_rate.pack(pady=10)
ent_rate.pack(pady=10)

lab_time = Label(root,
                 text="Enter Time In Years",
                 font=f)

ent_time = Entry(root,
                 font=f,
                 fg="blue")

lab_time.pack(pady=10)
ent_time.pack(pady=10)

btn_find = Button(root,
                  text="Find Simple Interest",
                  font=f,
                  command=find)

lab_msg = Label(root,
                font=("Times New Roman", 25, "bold"))

btn_find.pack(pady=20)
lab_msg.pack(pady=20)

root.mainloop()