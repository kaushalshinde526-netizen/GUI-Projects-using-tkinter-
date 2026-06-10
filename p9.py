from tkinter import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt

root = Tk()
root.title("Share Holding Pattern")
root.geometry("600x700+300+10")

f = ("Arial", 20, "bold")

def generate():
    company = ent_company.get()

    if company == "":
        showerror("Company Issue", "Name should not be empty")
        ent_company.focus()
        return

    promoter = ent_promoter.get()

    if promoter == "":
        showerror("Promoter Issue", "Name should not be empty")
        ent_promoter.focus()
        return

    fii = ent_fii.get()

    if fii == "":
        showerror("FII Issue", "Name should not be empty")
        ent_fii.focus()
        return

    dii = ent_dii.get()

    if dii == "":
        showerror("DII Issue", "Name should not be empty")
        ent_dii.focus()
        return

    public = ent_public.get()

    if public == "":
        showerror("Public Issue", "Name should not be empty")
        ent_public.focus()
        return

    stakeholder = ["promoter", "fii", "dii", "public"]

    percentage = [
        float(promoter),
        float(fii),
        float(dii),
        float(public)
    ]

    plt.pie(
        percentage,
        labels=stakeholder,
        autopct="%2.2f%%",
        explode=[0, 0, 0, 0.2],
        shadow=True
    )

    plt.title(company)
    plt.savefig(company.replace(" ", "_") + ".pdf")
    plt.show()


lab_company = Label(root, text="Enter Company Name", font=f)
ent_company = Entry(root, font=f)

lab_promoter = Label(root, text="Enter Promoter Holding", font=f)
ent_promoter = Entry(root, font=f)

lab_fii = Label(root, text="Enter FII Holding", font=f)
ent_fii = Entry(root, font=f)

lab_dii = Label(root, text="Enter DII Holding", font=f)
ent_dii = Entry(root, font=f)

lab_public = Label(root, text="Enter Public Holding", font=f)
ent_public = Entry(root, font=f)

btn_generate = Button(
    root,
    text="Generate Pie Chart",
    font=f,
    command=generate
)

lab_company.pack(pady=10)
ent_company.pack(pady=10)

lab_promoter.pack(pady=10)
ent_promoter.pack(pady=10)

lab_fii.pack(pady=10)
ent_fii.pack(pady=10)

lab_dii.pack(pady=10)
ent_dii.pack(pady=10)

lab_public.pack(pady=10)
ent_public.pack(pady=10)

btn_generate.pack(pady=10)

root.mainloop()