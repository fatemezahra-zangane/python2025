import tkinter as tk


root=tk.Tk()
root.title("lable example")

lable=tk.Label(root,text="hello",font=("arial",18),fg="blue")

lable.pack(pady=20)
root.mainloop()