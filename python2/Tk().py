import tkinter
from tkinter import messagebox
from tkinter import ttk
#import mysql.connector
name=tkinter.Tk()
w=name.winfo_screenwidth()
h=name.winfo_screenheight()
name.configure(height=h,width=w,bg="navyblue")
name.title("tkinter")
name.iconbitmap(r"new.ico")


def insert():
    u=tb1.get()
    p=int(tb2.get())
    messagebox.showinfo("KALAIARASI RESIDENCY A/C & NON A/C","your account has been signed in successfully")
    #db=mysql.connector.connect(host='localhost',user=user,password='kalai@123mysql',db='kalai')
    #cur=db.cursor()
    #cur.execute("insert into login values('%s',%d)"%(u,p))
    #db.commit()


def clear():
    tb1.delete(0,"end")
    tb2.delete(0,"end")
    tb1.focus()


lb1=tkinter.Label(name,text="KALAIARASI RESIDENCY A/C & NON A/C",font=("Monotype Corsiva",30,"bold","italic","bold"),relief="raised",bd=10)
lb1.place(x=400,y=0)

lb2=tkinter.Label(name,text="Username",font=("Monotype Corsiva",30,"bold","italic","bold"),relief="raised",bd=10)
lb3=tkinter.Label(name,text="Mobile",font=("Monotype Corsiva",30,"bold","italic","bold"),relief="raised",bd=10)
lb2.place(x=200,y=100)
lb3.place(x=230,y=200)

tb1=tkinter.Entry(name,font=("Monotype Corsiva",30,"bold","italic","bold"))
tb2=tkinter.Entry(name,font=("Monotype Corsiva",30,"bold","italic","bold"))
tb1.place(x=500,y=100)
tb2.place(x=500,y=200)


    
but1=tkinter.Button(name,text="SUBMIT",font=("Monotype Corsiva",30,"bold","italic","bold"),relief="raised",bd=15,command=insert)
but2=tkinter.Button(name,text="CLEAR",font=("Monotype Corsiva",30,"bold","italic","bold"),relief="raised",bd=15,command=clear)

but1.place(x=300,y=500)
but2.place(x=550,y=500)


lists=['dosa','idly','maggi']

combo=ttk.Combobox(name,values=lists)
combo.set("Pick an option:")
#combo.pack(padx=5,pady=5)
combo.place(x=400,y=400)

name.mainloop()
#var1=IntVar()
#var2=IntVar()

#chkbt=Checkbutton(name,width=1,variable=var1)
#chkbt.pack(padx=5,pady=300)

#chkbt1=Checkbutton(name,width=1,variable=var2)
#chkbt1.pack(padx=5,pady=300)

