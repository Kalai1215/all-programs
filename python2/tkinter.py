import tkinter
from tkinter import messagebox
root=tkinter.Tk()
import mysql.connector
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.configure(height=h,width=w,bg="black")
root.title("residency.com")
root.iconbitmap(r'new.ico')


def insert():
    u=tb1.get()
    p=int(tb2.get())
    messagebox.showinfo("KALAIARASI RESIDENCY A/C & NON A/C","your account has been signed in successfully")
    db=mysql.connector.connect(host='localhost',user='root',db='ash')
    cur=db.cursor()
    cur.execute("insert into login values('%s',%d)"%(u,p))
    db.commit()
def clear():
    tb1.delete(0,"end")
    tb2.delete(0,"end")
    tb1.focus()
def nextpage():
    #root.destroy()
    import page2

lb1=tkinter.Label(root,text="KALAIARASI RESIDENCY A/C & NON A/C",font=("Monotype Corsiva",30,
            "italic"),bg="pink",fg="BLACK",relief="flat",bd=10)
lb1.place(x=350,y=0)

frm=tkinter.Frame(root)
frm.place(x=400,y=100,height=500,width=500)

un=tkinter.Label(frm,text="Username",font=("Monotype Corsiva",15,"italic","bold")
                 ,bg="pink",fg="white",relief="raised",bd=10)
pwd=tkinter.Label(frm,text="Mobile no.",font=("Monotype Corsiva",15,"italic","bold")
                 ,bg="pink",fg="white",relief="raised",bd=10)

un.place(x=20,y=100)
pwd.place(x=20,y=200)

tb1=tkinter.Entry(frm,font=("Monotype Corsiva",20,"italic","bold"))
tb2=tkinter.Entry(frm,font=("Monotype Corsiva",20,"italic","bold"))

tb1.place(x=180,y=100)
tb2.place(x=180,y=200)

b1=tkinter.Button(frm,text='Submit',font=("Monotype Corsiva",15,"italic","bold"),bg="pink",fg="white",relief="ridge",bd=10,command=insert)
b1.place(x=70,y=300)

b2=tkinter.Button(frm,text='Clear',font=("Monotype Corsiva",15,"italic","bold"),bg="pink",fg="white",relief="raised",bd=10,command=clear)
b2.place(x=220,y=300)

a=tkinter.Button(frm,text='Next',font=("Monotype Corsiva",15,"italic","bold"),bg="pink",fg="white",relief="raised",bd=10,command=nextpage)
a.place(x=380,y=300)

root.mainloop()
