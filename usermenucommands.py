import tkinter as tk
from tkinter import messagebox
import sqlite3
from HashingAlgo import hash
from IterateAuthorise import iterativeSearch
from toolbarmovement import start_drag, move_window
from loginform import login

def newuser(root):
    def newuserSQLinput():
        newnamelist=newname.get().split()                                                             
        if len(newnamelist) >2:
            messagebox.showerror("", "Too many names")
            return
        if len(newnamelist)==1:
            messagebox.showerror("","Please enter first and last name")
            return
        newpassword.set(hash(newusername.get(), newpassword.get()))
        connection=sqlite3.connect("BSLComprehension.login_credentials")
        connection.execute("INSERT INTO username VALUES(:firstname, :lastname, :email, :username)",
                   {"firstname": newnamelist[0], "lastname": newnamelist[1], "email": newemail.get(), "username": newusername.get()})
        connection.execute("INSERT INTO password VALUES(:firstname, :lastname, :password)",
                   {"firstname": newnamelist[0], "lastname": newnamelist[1], "password": newpassword.get()})
        connection.commit()
        connection.close()
        messagebox.showinfo("", "Successfully Added")
        newuserform.destroy()



    newuserform = tk.Toplevel(root, bg='lightgray')
    newuserform.title("New User")
    newuserform.overrideredirect(True)
    width, height = 400, 270
    x, y = (int(((root.winfo_screenwidth())/2)-((width+75)/2))), (int(((root.winfo_screenheight())/2)-(height/2)))
    newuserform.geometry('{}x{}+{}+{}'.format(width+75, height, x, y))

    newusertoolbar = tk.Frame(newuserform, bg="#3676d1", relief="raised", bd=1)
    newusertoolbar.grid(row=0, column=0, columnspan=3, ipadx=195)
    newusertoolbar.bind("<Button-1>", lambda e: start_drag(e))
    newusertoolbar.bind("<B1-Motion>", lambda e:move_window(e, newuserform))
    newusertitle = tk.Label(newusertoolbar, text="New User", bg="#3676d1", fg="#ffffff", font=("sans", "10", "bold"))
    newusertitle.pack(side=tk.LEFT)
    exitbutton = tk.Button(newusertoolbar, text="X", relief="raised", bg="#FF7276", command=lambda: newuserform.destroy())
    exitbutton.pack(side=tk.RIGHT)

    newuserformtitle = tk.Label(newuserform, text='Create New User',bg='lightgray',font=('Helvetica','30','bold'))
    newuserformtitle.grid(row=1, column=0, columnspan=3, padx=60, pady=10)

    newnamelabel=tk.Label(newuserform, text='Name:',bg='lightgray', font='20')
    newnamelabel.grid(row=2, column=0)
    newname=tk.StringVar()
    newnameentry=tk.Entry(newuserform, textvariable=newname)
    newnameentry.grid(row=2, column=1, ipadx=50,columnspan=2)

    newemaillabel=tk.Label(newuserform, text='Email:',bg='lightgray',font='20')
    newemaillabel.grid(row=3, column=0)
    newemail=tk.StringVar()
    newemailentry=tk.Entry(newuserform, textvariable=newemail)
    newemailentry.grid(row=3, column=1, ipadx=50,columnspan=2)

    newusernamelabel=tk.Label(newuserform, text='Username:',bg='lightgray',font='20')
    newusernamelabel.grid(row=4, column=0)
    newusername=tk.StringVar()
    newusernameentry=tk.Entry(newuserform, textvariable=newusername)
    newusernameentry.grid(row=4, column=1, ipadx=50,columnspan=2)

    newpasswordlabel=tk.Label(newuserform, text='Password:',bg='lightgray',font='20')
    newpasswordlabel.grid(row=5, column=0)
    newpassword=tk.StringVar()
    newpasswordentry=tk.Entry(newuserform, textvariable=newpassword, show="*")
    newpasswordentry.grid(row=5, column=1, ipadx=50,columnspan=2)

    createbutton = tk.Button(newuserform, text="Create", bg="darkgreen", command=lambda:newuserSQLinput())
    createbutton.grid(row=6, column=1, pady=25, ipadx=50)
    closebutton = tk.Button(newuserform, text="Close", bg="orangered", command=lambda:newuserform.destroy())
    closebutton.grid(row=6, column=2, pady=25, ipadx=50)

    newuserform.mainloop()

def changepassword(root):
    def changepasswordSQLinput():
        oldpass.set(hash(username.get(), oldpass.get()))
        newpass.set(hash(username.get(), newpass.get()))
        tablevalues= iterativeSearch()
        for i in range(len(tablevalues)):
            DBusername = list(tablevalues[0][i]).pop()
            DBpassword = list(tablevalues[1][i]).pop()
            if DBusername == username.get():
                if DBpassword == str(oldpass.get()):
                    connection = sqlite3.connect('BSLComprehension.login_credentials')
                    transfer=connection.cursor()
                    transfer.execute('UPDATE password SET password=:formatnewpass WHERE password=:formatoldpass',{'formatnewpass':newpass.get(), 'formatoldpass':oldpass.get()})
                    connection.commit()
                    connection.close()
                    changepassform.destroy()
                    messagebox.showinfo('','Password Changed')
        messagebox.showerror("", "Incorrect Credentials")
        return
    changepassform = tk.Toplevel(root, bg='lightgray')
    changepassform.title("Change Password")
    changepassform.overrideredirect(True)
    width, height = 400, 250
    x, y = (int(((root.winfo_screenwidth())/2)-((width+75)/2))), (int(((root.winfo_screenheight())/2)-(height/2)))
    changepassform.geometry('{}x{}+{}+{}'.format(width+75, height, x, y))
    changepasstoolbar = tk.Frame(changepassform, bg="#3676d1", relief="raised", bd=1)
    changepasstoolbar.grid(row=0, column=0, columnspan=3, ipadx=168)
    changepasstoolbar.bind("<Button-1>", lambda e: start_drag(e))
    changepasstoolbar.bind("<B1-Motion>", lambda e:move_window(e, changepassform))
    changepasstitle = tk.Label(changepasstoolbar, text="Change Password", bg="#3676d1", fg="#ffffff", font=("sans", "10", "bold"))
    changepasstitle.pack(side=tk.LEFT)
    exitbutton = tk.Button(changepasstoolbar, text="X", relief="raised", bg="#FF7276", command=lambda: changepassform.destroy())
    exitbutton.pack(side=tk.RIGHT)

    newuserformtitle = tk.Label(changepassform, text='Change Password',bg='lightgray',font=('Helvetica','30','bold'))
    newuserformtitle.grid(row=1, column=0, columnspan=3, padx=60, pady=10)

    usernamelabel=tk.Label(changepassform, text='Username:',bg='lightgray', font='20')
    usernamelabel.grid(row=2, column=0)
    username=tk.StringVar()
    usernameentry=tk.Entry(changepassform, textvariable=username)
    usernameentry.grid(row=2, column=1, ipadx=50,columnspan=2)

    oldpasslabel=tk.Label(changepassform, text='Old Password:',bg='lightgray',font='20')
    oldpasslabel.grid(row=3, column=0)
    oldpass=tk.StringVar()
    oldpassentry=tk.Entry(changepassform, textvariable=oldpass, show="*")
    oldpassentry.grid(row=3, column=1, ipadx=50,columnspan=2)

    newpasslabel=tk.Label(changepassform, text='New Password:',bg='lightgray',font='20')
    newpasslabel.grid(row=4, column=0)
    newpass=tk.StringVar()
    newpassentry=tk.Entry(changepassform, textvariable=newpass, show="*")
    newpassentry.grid(row=4, column=1, ipadx=50,columnspan=2)

    createbutton = tk.Button(changepassform, text="Change", bg="darkgreen", command=lambda:changepasswordSQLinput())
    createbutton.grid(row=5, column=1, pady=25, ipadx=50)
    closebutton = tk.Button(changepassform, text="Close", bg="orangered", command=lambda:changepassform.destroy())
    closebutton.grid(row=5, column=2, pady=25, ipadx=50)
    changepassform.mainloop()

def deleteall(root):
    confirmation = messagebox.askokcancel("","Delete all stored users?, Program will have to be restarted")
    if confirmation == False:
        return
    connection = sqlite3.connect("BSLComprehension.login_credentials")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE username')
    cursor.execute('DROP TABLE password')
    connection.commit()

    connection.execute('''CREATE TABLE IF NOT EXISTS username(
                        firstname text,
                        lastname text,
                        email text,
                        username text
                        ) ''')
    connection.execute('''CREATE TABLE IF NOT EXISTS password(
                        firstname text,
                        lastname text,
                        password text
                        )''')
    connection.execute("INSERT INTO username VALUES(:firstname, :lastname, :email, :username)",
                    {"firstname": "master", "lastname": "master", "email": "master@gmail.com", "username": "master"})

    connection.execute("INSERT INTO password VALUES(:firstname, :lastname, :password)",
                    {"firstname": "master", "lastname": "master", "password": "b'w5rDgsOmw6jDisOk'"})
    connection.commit()
    connection.close()
    root.destroy()

