import tkinter as tk
from tkinter import messagebox
from HashingAlgo import hash
from IterateAuthorise import authorise
from toolbarmovement import start_drag, move_window

def init(root,usernameTk, passwordTk):
    passwordPy = passwordTk.get()
    usernamePy = usernameTk.get()
    if usernamePy=="":
        messagebox.showerror("", "Username field can't be left blank")
        return
    if passwordPy=="":
        messagebox.showerror("", "Password field can't be left blank")
        return
    passwordPy = hash(usernameTk.get(), passwordPy)
    booleanreturn = authorise(usernamePy, passwordPy)
    if booleanreturn == False:
        messagebox.showerror("", "Incorrect Credentials")
        return
    root.destroy()
    


def FocusIn_username(usernameEntry):
    usernameEntry.delete(0, tk.END)
    usernameEntry.config(fg='black')


def FocusIn_password(passwordEntry):
    passwordEntry.delete(0, tk.END)
    passwordEntry.config(fg='black')

def login():
    root = tk.Tk()
    root.title("")
    x, y = (int(((root.winfo_screenwidth())/2)-((220)/2))), (int(((root.winfo_screenheight())/2)-(165/2)))
    root.geometry('{}x{}+{}+{}'.format(220, 165, x, y))
    root.configure(background="white")
    root.overrideredirect(True)
    root.bind('<Return>', lambda event: init(root, usernameTk, passwordTk))
    root.bind('<Escape>', lambda event: quit())
    root.bind('<Down>', lambda event: passwordEntry.focus())
    root.bind('<Up>', lambda event: usernameEntry.focus())

    toolbar = tk.Frame(root, bg="#3676d1", relief="raised", bd=1)
    toolbar.grid(row=0, column=0, columnspan=2, ipadx=57)
    toolbar.bind("<Button-1>", lambda e: start_drag(e))
    toolbar.bind("<B1-Motion>", lambda e:move_window(e, root))
    title = tk.Label(toolbar, text="Admin Login", bg="#3676d1", fg="#ffffff", font=("sans", "10", "bold"))
    title.pack(side=tk.LEFT)
    exitbutton = tk.Button(toolbar, text="X", relief="raised", bg="#FF7276", command=lambda: quit())
    exitbutton.pack(side=tk.RIGHT)

    UserRaw = tk.PhotoImage(file='D:\\Paradigms\\Python\\Programming project\\UserPicture.png')
    UserPicture = UserRaw.subsample(2, 2)
    PassRaw = tk.PhotoImage(file='D:\\Paradigms\\Python\\Programming project\\PassPicture.png')
    PassPicture = PassRaw.subsample(2, 2)

    username_icon = tk.Label(root, image=UserPicture).grid(row=2, column=0, pady=5)
    usernameTk = tk.StringVar()

    usernameEntry = tk.Entry(root, textvariable=usernameTk, borderwidth=3, fg='grey')
    usernameEntry.grid(row=2, column=1, ipady=5, ipadx=20, pady=5)
    usernameEntry.insert(0, 'Username')
    usernameEntry.bind('<FocusIn>', lambda event: FocusIn_username(usernameEntry))

    password_icon = tk.Label(root, image=PassPicture).grid(row=3, column=0)
    passwordTk = tk.StringVar()

    passwordEntry = tk.Entry(root, textvariable=passwordTk, borderwidth=3, fg='grey', show="*")
    passwordEntry.grid(row=3, column=1, ipady=5, ipadx=20)
    passwordEntry.insert(0, 'Password')
    passwordEntry.bind('<FocusIn>', lambda event: FocusIn_password(passwordEntry))

    loginbutton = tk.Button(root, text="Login", bg='#3676d1', fg='white', font=(
        'Sans', '14', 'bold'), command=lambda: init(root, usernameTk, passwordTk))
    loginbutton.grid(row=4, column=0, columnspan=2, ipadx=70, padx=2, pady=2)
    root.mainloop()