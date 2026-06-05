from tkinter import *


def convert():
	btn_convert.config(text="conversion is..")
	btn_convert.config(state="disabled")
	root.update_idletasks()
	if csrc.get() == 1:
		scur = "M"
	elif csrc.get() == 2:
		scur = "KM"
	else:
		scur = "MILES"
	if cdest.get() == 1:
		sdest = "M"
	elif cdest.get() == 2:
		sdest = "KM"
	else:
		sdest = "MILES"
	try:
		dist = float(ent_dist.get())
		if scur == sdest:
			ans = dist
		elif (scur == "M" ) and (sdest == "KM" ):
			ans = dist / 1000
		elif (scur == "M" ) and (sdest == "MILES"):
			ans = dist / 1609
		elif (scur == "KM" ) and (sdest == "M" ):
			ans = dist * 1000
		elif (scur == "KM" ) and (sdest == "MILES"):
			ans = dist / 1.609
		elif (scur == "MILES" ) and (sdest == "M"):
			ans = dist * 1609
		elif (scur == "MILES" ) and (sdest == "KM"):
			ans = dist * 1.609
		msg = "converted distance" + " = " + str(round(ans,4)) + " " + str(sdest)
		lab_msg.configure(text=msg,fg="blue")
	except Exception:
		msg = "please enter numbers only"
		lab_msg.configure(text=msg,fg="red")	
	btn_convert.config(state="normal",text="Convert")
root = Tk()
root.title("Multiple Distance Converter")
root.geometry("1000x600+300+30")
root.resizable(False, False)

f = ("Times New Roman",30,"bold")


lab_dist = Label(root,text="Enter Distance",font=f)
ent_dist = Entry(root,font=f)
csrc = IntVar()
csrc.set(1)
lab_src = Label(root,text="Select Source",font=f)
srb_m = Radiobutton(root,text="M",font=f,variable=csrc,value=1)
srb_km = Radiobutton(root,text="KM",font=f,variable=csrc,value=2)
srb_miles = Radiobutton(root,text="MILES",font=f,variable=csrc,value=3)


cdest = IntVar()
cdest.set(1)
lab_dest = Label(root,text="Select Destination",font=f)
drb_m = Radiobutton(root,text="M",font=f,variable=cdest,value=1)
drb_km = Radiobutton(root,text="KM",font=f,variable=cdest,value=2)
drb_miles = Radiobutton(root,text="MILES",font=f,variable=cdest,value=3)

btn_convert = Button(root,text="convert",font=f,command=convert)
lab_msg = Label(root,font=f)

lab_dist.place(x=40,y=40)
ent_dist.place(x=400,y=40)
lab_src.place(x=40,y=140)
srb_m.place(x=40,y=200)
srb_km.place(x=40,y=260)
srb_miles.place(x=40,y=320)


lab_dest.place(x=400,y=140)
drb_m.place(x=400,y=200)
drb_km.place(x=400,y=260)
drb_miles.place(x=400,y=320)


btn_convert.place(x=400,y=450)
lab_msg.place(x=40,y=550)


root.mainloop()