import tkinter as tk
def update_color_backround():
    colors=["red","orange","yellow","green","blue","indigo","violet"]
    global bg_color_index
    root.configure(bg=colors[bg_color_index])
    bg_color_index=(bg_color_index+1)%len(colors)
    root.after(200,update_color_backround)
def update_color_text():
    colors=["red","orange","yellow","green","blue","indigo","violet"]
    global text_color_index
    rainbow_text.configure(fg=colors[text_color_index])
    text_color_index=(text_color_index+1)%len(colors)
    root.after(200,update_color_text)
root=tk.Tk()
root.title("Rainbow")
root.minsize(20,20)
root.maxsize(10000,10000)
root.geometry("1000x600")
bg_color_index=0
text_color_index=0
rainbow_text=tk.Label(root,text="yooooooooooooooooooooooooooooooooooooooooooooooooooooo",font=("arial",24))
rainbow_text.pack(expand=True)
update_color_backround()
update_color_text()
root.mainloop()