from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def mw_to_cw():
    mw.withdraw()
    cw.deiconify()

def cw_to_mw():
    cw.withdraw()
    mw.deiconify()

def mw_to_rw():
    mw.withdraw()
    rw.deiconify()
    rw_st_data.delete(0.0, END)
    view()

def rw_to_mw():
    rw.withdraw()
    mw.deiconify()

def mw_to_uw():
    mw.withdraw()
    uw.deiconify()

def uw_to_mw():
    uw.withdraw()
    mw.deiconify()

def mw_to_dw():
    mw.withdraw()
    dw.deiconify()

def dw_to_mw():
    dw.withdraw()
    mw.deiconify()

def db_setp():

    con = None

    try:
        con = connect("ems.db")

        sql = "create table if not exists employee(id int primary key, name text, salary float)"

        cursor = con.cursor()
        cursor.execute(sql)

        con.commit()

        print("done")

    except Exception as e:

        print("issue ", e)

        if con is not None:
            con.rollback()

    finally:

        if con is not None:
            con.close()

db_setp()

def save():

    if cw_ent_id.get() == "":
        showerror("id issue", "id is empty")
        cw_ent_id.focus()
        return

    try:
        id = int(cw_ent_id.get())

    except ValueError:
        showerror("invalid id", "id should be integer")
        cw_ent_id.delete(0, END)
        cw_ent_id.focus()
        return

    if cw_ent_name.get() == "":
        showerror("name issue", "name is empty")
        cw_ent_name.focus()
        return

    name = cw_ent_name.get()

    if cw_ent_salary.get() == "":
        showerror("salary issue", "salary is empty")
        cw_ent_salary.focus()
        return

    try:
        salary = float(cw_ent_salary.get())

    except ValueError:
        showerror("invalid salary", "salary should be number")
        cw_ent_salary.delete(0, END)
        cw_ent_salary.focus()
        return

    con = None

    try:

        con = connect("ems.db")

        sql = "insert into employee(id, name, salary) values(?, ?, ?)"

        cursor = con.cursor()
        cursor.execute(sql, (id, name, salary))

        con.commit()

        print("done")

        showinfo("success", "record saved")

        cw_ent_id.delete(0, END)
        cw_ent_name.delete(0, END)
        cw_ent_salary.delete(0, END)

        cw_ent_id.focus()

    except Exception as e:

        print("issue ", e)

        showerror("create issue", str(e))

        if con is not None:
            con.rollback()

    finally:

        if con is not None:
            con.close()

def update():

    if uw_ent_id.get() == "":
        showerror("id issue", "id is empty")
        uw_ent_id.focus()
        return

    try:
        id = int(uw_ent_id.get())

    except ValueError:
        showerror("invalid id", "id should be integer")
        uw_ent_id.delete(0, END)
        uw_ent_id.focus()
        return

    if uw_ent_name.get() == "":
        showerror("name issue", "name is empty")
        uw_ent_name.focus()
        return

    name = uw_ent_name.get()

    if uw_ent_salary.get() == "":
        showerror("salary issue", "salary is empty")
        uw_ent_salary.focus()
        return

    try:
        salary = float(uw_ent_salary.get())

    except ValueError:
        showerror("invalid salary", "salary should be number")
        uw_ent_salary.delete(0, END)
        uw_ent_salary.focus()
        return

    con = None

    try:

        con = connect("ems.db")

        sql = "update employee set name = ?, salary = ? where id = ?"

        cursor = con.cursor()
        cursor.execute(sql, (name, salary, id))

        con.commit()

        print("done")

        if cursor.rowcount == 0:
            showinfo("not found", "record does not exist")
        else:
            showinfo("success", str(cursor.rowcount) + " records updated")

        uw_ent_id.delete(0, END)
        uw_ent_name.delete(0, END)
        uw_ent_salary.delete(0, END)

        uw_ent_id.focus()

    except Exception as e:

        print("issue ", e)

        showerror("update issue", str(e))

        if con is not None:
            con.rollback()

    finally:

        if con is not None:
            con.close()

def delete():

    if dw_ent_id.get() == "":
        showerror("id issue", "id is empty")
        dw_ent_id.focus()
        return

    try:
        id = int(dw_ent_id.get())

    except ValueError:
        showerror("invalid id", "id should be integer")
        dw_ent_id.delete(0, END)
        dw_ent_id.focus()
        return

    con = None

    try:

        con = connect("ems.db")

        sql = "delete from employee where id = ?"

        cursor = con.cursor()
        cursor.execute(sql, (id,))

        con.commit()

        print("done")

        if cursor.rowcount == 0:
            showinfo("not found", "record does not exist")
        else:
            showinfo("success", str(cursor.rowcount) + " records deleted")

        dw_ent_id.delete(0, END)
        dw_ent_id.focus()

    except Exception as e:

        print("issue ", e)

        showerror("delete issue", str(e))

        if con is not None:
            con.rollback()

    finally:

        if con is not None:
            con.close()

def view():

    con = None

    try:

        con = connect("ems.db")

        sql = "select id, name, salary from employee"

        cursor = con.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        info = ""

        for d in data:

            info = info + "id = " + str(d[0]) + "\n"
            info = info + "name = " + str(d[1]) + "\n"
            info = info + "salary = " + str(d[2]) + "\n"
            info = info + "-------------------------\n"

        rw_st_data.insert(INSERT, info)

    except Exception as e:

        print("issue ", e)

        showerror("read issue", str(e))

    finally:

        if con is not None:
            con.close()

mw = Tk()

mw.title("Emp. Mgt System")
mw.geometry("600x700+300+20")

f = ("Arial", 30, "bold")

mw_btn_create = Button(mw, text="Create Record", font=f, width=12, command=mw_to_cw)
mw_btn_read = Button(mw, text="Read Records", font=f, width=12, command=mw_to_rw)
mw_btn_update = Button(mw, text="Update Record", font=f, width=12, command=mw_to_uw)
mw_btn_delete = Button(mw, text="Delete Record", font=f, width=12, command=mw_to_dw)

mw_btn_create.pack(pady=20)
mw_btn_read.pack(pady=20)
mw_btn_update.pack(pady=20)
mw_btn_delete.pack(pady=20)



cw = Toplevel()

cw.title("Create Employee")
cw.geometry("600x700+300+20")

cw_lab_id = Label(cw, text="Enter Emp Id", font=f)
cw_ent_id = Entry(cw, font=f)

cw_lab_name = Label(cw, text="Enter Emp Name", font=f)
cw_ent_name = Entry(cw, font=f)

cw_lab_salary = Label(cw, text="Enter Emp Salary", font=f)
cw_ent_salary = Entry(cw, font=f)

cw_btn_save = Button(cw, text="Save Employee", font=f, command=save)
cw_btn_back = Button(cw, text="Back to Main", font=f, command=cw_to_mw)

cw_lab_id.pack(pady=10)
cw_ent_id.pack(pady=10)

cw_lab_name.pack(pady=10)
cw_ent_name.pack(pady=10)

cw_lab_salary.pack(pady=10)
cw_ent_salary.pack(pady=10)

cw_btn_save.pack(pady=10)
cw_btn_back.pack(pady=10)

cw.withdraw()



rw = Toplevel()

rw.title("View Employee")
rw.geometry("600x700+300+20")

rw_st_data = ScrolledText(rw, font=f, width=20, height=10)

rw_btn_back = Button(rw, text="Back To Main", font=f, command=rw_to_mw)

rw_st_data.pack(pady=10)
rw_btn_back.pack(pady=10)

rw.withdraw()


uw = Toplevel()

uw.title("Update Employee")
uw.geometry("600x700+300+20")

uw_lab_id = Label(uw, text="Enter Emp Id", font=f)
uw_ent_id = Entry(uw, font=f)

uw_lab_name = Label(uw, text="Enter Emp Name", font=f)
uw_ent_name = Entry(uw, font=f)

uw_lab_salary = Label(uw, text="Enter Emp Salary", font=f)
uw_ent_salary = Entry(uw, font=f)

uw_btn_save = Button(uw, text="Update Employee", font=f, command=update)
uw_btn_back = Button(uw, text="Back to Main", font=f, command=uw_to_mw)

uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)

uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)

uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)

uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)

uw.withdraw()

dw = Toplevel()

dw.title("Delete Employee")
dw.geometry("600x700+300+20")

dw_lab_id = Label(dw, text="Enter Emp Id", font=f)
dw_ent_id = Entry(dw, font=f)

dw_btn_save = Button(dw, text="Delete Employee", font=f, command=delete)
dw_btn_back = Button(dw, text="Back To Main", font=f, command=dw_to_mw)

dw_lab_id.pack(pady=10)
dw_ent_id.pack(pady=10)

dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)

dw.withdraw()

mw.mainloop()