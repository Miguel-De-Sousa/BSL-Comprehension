import tkinter as tk
from tkinter import messagebox
from toolbarmovement import start_drag, move_window

def export(root, text):
    def createfile():
        if filename.get()!="":
            file = open(f'{filename.get()}{filetype.get()}','w')
            file.write(text.get())
            text.set(value="")
            messagebox.showinfo("", "File Creation Successful")
        Exportform.destroy()
    Exportform = tk.Toplevel(root)
    Exportform.overrideredirect(True)
    x, y = (int(((Exportform.winfo_screenwidth())/2)-((180)/2))), (int(((Exportform.winfo_screenheight())/2)-(100/2)))
    Exportform.geometry('{}x{}+{}+{}'.format(190, 135, x, y))

    Exporttoolbar = tk.Frame(Exportform, bg="#3676d1", relief="raised", bd=1)
    Exporttoolbar.grid(row=0, column=0, columnspan=2, ipadx=60)
    Exporttoolbar.bind("<Button-1>", lambda e:start_drag(e))
    Exporttoolbar.bind("<B1-Motion>", lambda e:move_window(e, Exportform))

    toolbartitle = tk.Label(Exporttoolbar, text="Export     ", bg="#3676d1", fg="#ffffff", font=("sans", "10", "bold"))
    toolbartitle.pack(side=tk.LEFT)

    filenametitle = tk.Label(Exportform, text="filename:")
    filenametitle.grid(row=1, column=0, pady=10)
    filename=tk.StringVar()
    filenameEntry=tk.Entry(Exportform, textvariable=filename)
    filenameEntry.grid(row=1, column=1, ipady=2)

    options = ['.txt','.docx', '.pdf' ]
    filetypetitle = tk.Label(Exportform, text="filetype:")
    filetypetitle.grid(row=2, column=0)
    filetype=tk.StringVar(value='.txt')
    filetypeOption=tk.OptionMenu(Exportform,filetype, *options,)
    filetypeOption.grid(row=2, column=1, sticky='EW')

    buttonframe = tk.Frame(Exportform)
    buttonframe.grid(row=3, column=0, columnspan=2)
    saveAsbutton = tk.Button(buttonframe, text='confirm', bg='green', command=createfile)
    saveAsbutton.pack(side=tk.LEFT, padx=20, pady=10)
    
    cancelbutton = tk.Button(buttonframe, text='cancel', bg='orangered', command=lambda:Exportform.destroy())
    cancelbutton.pack(side=tk.RIGHT, padx=20, pady=10)
    Exportform.mainloop()

def save(text):
    if text.get() != "('>',)":
        savefile= open('savefile.txt', 'w')
        savefile.write(text.get())
        messagebox.showinfo("", "Saved File")
    else:
        messagebox.showerror("","Contents Empty, Unable to save")
