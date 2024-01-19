import tkinter as tk
from time import sleep
from tqdm.tk import tqdm

def load(root):
    root.attributes('-alpha', 0)
    progressbar= tqdm(total=30,desc='Loading Packages' ,tk_parent=root)
    def bar_init():
        for i in range(30):
            sleep(1)
            progressbar.update(i)
        progressbar.close()

    bar_init()

root=tk.Tk()
load(root)
root.mainloop()
