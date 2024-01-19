import tkinter as tk
from usermenucommands import *
from filemenucommands import *

def menu(root, translationresult):
    mainwindow_menu=tk.Menu(root)
    root.config(menu=mainwindow_menu)

    file_dropdown=tk.Menu(mainwindow_menu, tearoff=False)
    mainwindow_menu.add_cascade(label='File', menu=file_dropdown)
    file_dropdown.add_command(label='New')
    file_dropdown.add_command(label='Open')
    file_dropdown.add_separator()
    file_dropdown.add_command(label='Save', command=lambda: save(translationresult))
    file_dropdown.add_command(label='Save As...')
    file_dropdown.add_separator()
    file_dropdown.add_command(label='Import')
    file_dropdown.add_command(label='Export',command=lambda: export(root, translationresult))
    file_dropdown.add_separator()
    file_dropdown.add_command(label='Exit', command=root.destroy)

    edit_dropdown = tk.Menu(root, tearoff=False)
    root.config(menu=mainwindow_menu)
    mainwindow_menu.add_cascade(label='Edit', menu=edit_dropdown)
    edit_dropdown.add_command(label='Undo')
    edit_dropdown.add_command(label='Redo')
    edit_dropdown.add_separator()
    edit_dropdown.add_command(label='Cut')
    edit_dropdown.add_command(label='Copy')
    edit_dropdown.add_command(label='Paste')

    config_dropdown = tk.Menu(mainwindow_menu, tearoff=False)
    mainwindow_menu.add_cascade(label='User', menu=config_dropdown)
    config_dropdown.add_command(label='New User', command= lambda: newuser(root))
    config_dropdown.add_separator()
    config_dropdown.add_command(label='View Password')
    config_dropdown.add_command(label='Change Password', command=lambda: changepassword(root))
    config_dropdown.add_separator()
    config_dropdown.add_command(label='Erase all Users', command=lambda: deleteall(root))

    help_dropdown = tk.Menu(mainwindow_menu, tearoff=False)
    mainwindow_menu.add_cascade(label='Help', menu=help_dropdown)
