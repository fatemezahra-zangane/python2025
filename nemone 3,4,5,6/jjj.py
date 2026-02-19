import tikinter as tk

def show_text():
    entered_text=entry.get()
    print(f"u entered:{entered_text}")

root=tk.Tk()
root.title("entry example")


entry=tk.entery(root,font=("arial,12"),width=30)
entry.pack(pady=10)

button=tk.button(root,text="submit",font=("arial",14),commed=show_text)
button.pack(pady=10)

root=mainloop()