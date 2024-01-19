def start_drag(e):
        e.widget.offset =(e.x,e.y)

def move_window(e, root):
    root.geometry(f"+{e.x_root-e.widget.offset[0]}+{e.y_root-e.widget.offset[1]}")