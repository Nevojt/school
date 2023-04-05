import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Calculated CMR")
window.geometry("480x300")
window.config(padx=15, pady=15)


# Paleta P1, EURO
palety_label = ttk.Label(window, text="Palety", font=("Arial", 12, "bold"))
palety_label.grid(row=0, column=0, padx=10, pady=15)

palety_ilosc = ttk.Label(window, text="ilosc", font=("Arial", 12, "bold"))
palety_ilosc.grid(row=0, column=2, padx=10, pady=15)


palety_input = ttk.Entry(window, width=10)
palety_input.grid(row=0, column=3)

n = tk.StringVar()
palety_choose = ttk.Combobox(window, width=10, textvariable=n)

palety_choose["values"] = ["P1", "EURO"]
palety_choose.grid(row=0, column=1, padx=10, pady=15)
palety_choose.current()

output_palety = ttk.Label(window, text="0", font=("Arial", 12, "bold"))
output_palety.grid(row=0, column=4, padx=10, pady=15)


def calculate():
    palety = int(palety_input.get())
    butelka = int(butelka_input.get())
    waga = float(waga_input.get())

    if palety_choose.get() == "P1":
        pal_suma = palety * 8
    elif palety_choose.get() == "EURO":
        pal_suma = palety * 22
    else:
        pal_suma = 0

    karton_suma = round(palety * 3.5)
    folia_suma = round(palety * 0.5)
    butelka_suma = round(butelka * waga)

    output_palety.config(text=pal_suma)
    output_karton.config(text=karton_suma)
    output_folia.config(text=folia_suma)
    output_butelka.config(text=butelka_suma)

    suma = pal_suma + karton_suma + folia_suma + butelka_suma
    razem.config(text=round(suma))   

button_pal = tk.Button(window, text="Calculate", command=calculate, font=("Arial", 12, "bold"))
button_pal.grid(row=4, column=2, padx=10, pady=15)
    

# Karton palety * 3.5 kg
karton_label = ttk.Label(window, text="Karton", font=("Arial", 12, "bold"))
karton_label.grid(row=1, column=0, padx=10, pady=15)

output_karton = ttk.Label(window, text="0", font=("Arial", 12, "bold"))
output_karton.grid(row=1, column=4, padx=10, pady=15)


# Folia palety * 0.5 kg     
folia_label = ttk.Label(window, text="Folia", font=("Arial", 12, "bold"))
folia_label.grid(row=2, column=0, padx=10, pady=15)

output_folia = ttk.Label(window, text="0", font=("Arial", 12, "bold"))
output_folia.grid(row=2, column=4, padx=10, pady=15)

# Butelka (ilosc X waga)
butelka_label = ttk.Label(window, text="Butelka", font=("Arial", 12, "bold"))
butelka_label.grid(row=3, column=0, padx=10, pady=15)

butelka_input = ttk.Entry(window, width=10)
butelka_input.grid(row=3, column=1, padx=10, pady=15)

waga_label = ttk.Label(window, text="Waga", font=("Arial", 12, "bold"))
waga_label.grid(row=3, column=2, padx=10, pady=15)

waga_input = ttk.Entry(window, width=10)
waga_input.grid(row=3, column=3, padx=10, pady=15)

output_butelka = ttk.Label(window, text="0", font=("Arial", 12, "bold"))
output_butelka.grid(row=3, column=4, padx=10, pady=15)


suma_label = ttk.Label(window, text="Razem", font=("Arial", 12, "bold"))
suma_label.grid(row=4, column=3, padx=10, pady=15)

razem = ttk.Label(window, text="0", font=("Arial", 12, "bold"))
razem.grid(row=4, column=4, padx=10, pady=15)

# karton(), folia(), butelka(), suma(),











window.mainloop()