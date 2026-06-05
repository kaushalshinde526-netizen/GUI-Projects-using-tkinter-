from tkinter import *

root = Tk()
root.title("Interest Calculator")
root.geometry("600x700+300+20")
root.resizable(False, False)

f = ("Times New Roman", 20, "bold")

def find():
    try:
        p = float(ent_principal.get())
    except ValueError:
        msg = "principal amt shud be numbers only"
        lab_msg.configure(text=msg)
        return

    if p <= 1000:
        msg = "principal amt shud be min 1000"
        lab_msg.configure(text=msg)
        return

    try:
        r = float(ent_rate.get())
    except ValueError:
        msg = "rate shud be numbers only"
        lab_msg.configure(text=msg)
        return

    if r <= 0:
        msg = "rate shud be min 0.1"
        lab_msg.configure(text=msg)
        return

    try:
        t = float(ent_time.get())
    except ValueError:
        msg = "time shud be numbers only"
        lab_msg.configure(text=msg)
        return

    if t <= 0:
        msg = "time shud be min 0.1"
        lab_msg.configure(text=msg)
        return

    if c.get() == 1:
        si = (p * r * t) / 100
        msg = "simple interest amt = " + str(round(si, 2))
        lab_msg.configure(text=msg)

    else:
        ci = p * (1 + (r/100)) ** t - p
        msg = "compound interest amt = " + str(round(ci, 2))
        lab_msg.configure(text=msg)

lab_header = Label(root, text="Interest Calculator ", font=f)
lab_header.pack(pady=20)

lab_principal = Label(root, text="Enter Principal Amount", font=f)
ent_principal = Entry(root, font=f)
lab_principal.pack(pady=10)
ent_principal.pack(pady=10)

lab_rate = Label(root, text="Enter Rate of Interest", font=f)
ent_rate = Entry(root, font=f)
lab_rate.pack(pady=10)
ent_rate.pack(pady=10)

lab_time = Label(root, text="Enter Time in Years", font=f)
ent_time = Entry(root, font=f)
lab_time.pack(pady=10)
ent_time.pack(pady=10)

c = IntVar()
c.set(1)

rb_si = Radiobutton(root, text="SI", font=f, variable=c, value=1)
rb_ci = Radiobutton(root, text="CI", font=f, variable=c, value=2)
rb_si.pack(pady=10)
rb_ci.pack(pady=10)

btn_find = Button(root, text="Find Interest", font=f, command=find)
lab_msg = Label(root, font=f)

btn_find.pack(pady=10)
lab_msg.pack(pady=10)

root.mainloop()