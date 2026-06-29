import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(ent_.get())
        celsius = (fahrenheit - 32) * 5 / 9
        lbl_.config(text=f"{round(celsius, 2)}\N{DEGREE CELSIUS}")
    except ValueError:
        lbl_.config(text="ugh why make it harder")
window = tk.Tk()
window.title("Temperature Converter (disgusted look) you fahreinheit weirdo")
window.resizable(width=False, height=False)
window.geometry("600x300")

frm_entry = tk.Frame(master=window)
ent_ = tk.Entry(master=frm_entry, width=10)
lbl_ = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_.grid(row=0, column=0, sticky="e")
lbl_.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)
lbl_ = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_.grid(row=0, column=2, padx=10)

window.mainloop()
