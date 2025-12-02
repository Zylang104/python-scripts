import tkinter as tk
import random
def move_randomly():
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    window_w= 300
    window_h= 100
    new_x= random.randint(0,width-window_w)
    new_y= random.randint(0,height-window_h)
    root.geometry(f"{window_w}x{window_h}+{new_x}+{new_y}")
    root.after(100,move_randomly) # set there how much fast you want it to move
def close_window(event):
    root.destroy()
root= tk.Tk()
root.title("Try to close me")
root.attributes('-topmost',True)
label= tk.Label(root,text="Try to close me!",font=("Arial",20), fg="red")
label.pack(expand=True,pady=15,padx=15)
root.bind('<Delete>',close_window)
move_randomly()
root.mainloop()