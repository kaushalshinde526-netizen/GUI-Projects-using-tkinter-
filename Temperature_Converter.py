from tkinter import*

root=Tk()
root.title("Temperature Converter App")
root.geometry("1000x500+300+40")
root.resizable(False,False)
f=("Arial",30,"bold")

def convert():
       try:
            temp=float(ent_temp.get())
            if c.get()==1:
                    ans=(temp*1.8)+32
                    msg =str(temp)+"°C" + " = " + str(round(ans,1))+"°F"
            else:
                    ans=(temp - 32)/1.8
                    msg=str(temp)+"°F" + " = " + str(round(ans,1))+"°C"
            lab_msg.configure(text=msg,fg="blue")

       except ValueError:
            msg="please enter numbers only"
            lab_msg.configure(text=msg,fg="red")

lab_temp=Label(root,text="Enter Temperature",font=f)
lab_temp.place(x=50,y=50)
ent_temp=Entry(root,font=f)
ent_temp.place(x=500,y=50)

c=IntVar()
c.set(1)
lab_select=Label(root,text="Select One", font=f)
rb_c2f=Radiobutton(root,text="Cel 2 Fah",font=f,variable=c,value=1)
rb_f2c=Radiobutton(root,text="Fah 2 Cel",font=f,variable=c,value=2)
lab_select.place(x=50,y=150)
rb_c2f.place(x=500,y=150)
rb_f2c.place(x=500,y=220)

btn_convert=Button(root,text="Convert",font=f,command=convert)
btn_convert.place(x=500,y=300)
lab_msg=Label(root,text="",font=f)
lab_msg.place(x=50,y=400)

root.mainloop()
