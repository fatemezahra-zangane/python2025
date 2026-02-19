
import tikinter as tk



def on_butten_click():
    print("buttun clicked")



root=tk.Tk()
root.title("buttun example")


button=tk.button(root,text="click me",font=(arial,13),fg="white",bg="green"command=on_button_click)


button.pack(pady=20)
