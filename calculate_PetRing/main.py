import tkinter as tk
from tkinter import ttk
from math import ceil

window = tk.Tk()
window.title("Calculated CMR")
window.geometry("480x600")
window.config(padx=15, pady=15)




n = tk.StringVar()
k = tk.StringVar()
kp = tk.StringVar()

palety_choose = ttk.Combobox(window, width=10, textvariable=n)
palety_choose["values"] = ["P1", "EURO"]
palety_choose.grid(row=0, column=1, padx=10, pady=15)
palety_choose.current()

karton_choose = ttk.Combobox(window, width=10, textvariable=k)
karton_choose["values"] = ["K1", "K7"]
karton_choose.grid(row=6, column=1, padx=10, pady=15)
karton_choose.current()

palety_karton = ttk.Combobox(window, width=10, textvariable=kp)
palety_karton["values"] = ["P1", "EURO"]
palety_karton.grid(row=5, column=1, padx=10, pady=15)
palety_karton.current()

SUM1 = []
SUM2 = []


def calculate_butelka() -> int:
    palety = int(palety_input.get())
    butelka = int(butelka_input.get())
    waga = float(waga_input.get())

    if palety_choose.get() == "P1":
        pal_suma = palety * 8
    elif palety_choose.get() == "EURO":
        pal_suma = palety * 22
    else:
        pal_suma = 0

    karton_suma = ceil(palety * 3.5)
    folia_suma = ceil(palety * 0.5)
    butelka_suma = ceil(butelka * waga)

    output_palety.config(text=pal_suma)
    output_karton.config(text=karton_suma)
    output_folia.config(text=folia_suma)
    output_butelka.config(text=butelka_suma)

    sum_pal = pal_suma + karton_suma + folia_suma + butelka_suma
    razem.config(text=ceil(sum_pal))
    return SUM1.append(sum_pal)
    
def nakretka() -> int:
    palety = int(karton_input_palet.get())
    karton = int(karton_input.get())
    nakretka = int(nakretka_input_ilosc.get())
    waga_nak = float(nakretka_input.get())

    if palety_karton.get() == "P1":
        pal_kart_suma = palety * 8
    elif palety_karton.get() == "EURO":
        pal_kart_suma = palety * 22
    else:
        pal_kart_suma = 0
    
    if karton_choose.get() == "K1":
        karton_sum = karton * 0.7
    elif karton_choose.get() == "K7":
        karton_sum = karton * 0.5
    else:
        karton_sum = 0

    nakretka_waga = ceil(nakretka * waga_nak)
    
    k1_k7_palety.config(text=pal_kart_suma)
    k1_k7_karton.config(text=ceil(karton_sum))
    output_nakretka.config(text=ceil(nakretka_waga))
    
    sum_nak = pal_kart_suma + karton_sum + nakretka_waga
    razem_nak.config(text=ceil(sum_nak))
    return SUM2.append(sum_nak)
    
    
def suma_razem() -> int:
    summa = SUM1[0] + SUM2[0]
    razem_suma.config(text=ceil(summa))


button_pal = tk.Button(window, text="Calculate", command=calculate_butelka, font=("Arial", 12, "bold"))
button_pal.grid(row=4, column=2, padx=10, pady=15)
suma_label = ttk.Label(window, text="Razem", font=("Arial", 12, "bold"))
suma_label.grid(row=4, column=3, padx=10, pady=15)
razem = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
razem.grid(row=4, column=4, padx=10, pady=15)

button_nak = tk.Button(window, text="Nakretka", command=nakretka, font=("Arial", 12, "bold"))
button_nak.grid(row=8, column=2, padx=10, pady=15)
razem_nak = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
razem_nak.grid(row=8, column=4, padx=10, pady=15)
razem_nak_label = ttk.Label(window, text="Razem", font=("Arial", 12, "bold"))
razem_nak_label.grid(row=8, column=3, padx=10, pady=15)

button_summa = tk.Button(window, text="Suma", command=suma_razem, font=("Arial", 12, "bold"))
button_summa.grid(row=9, column=2, padx=10, pady=15)
razem_suma = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
razem_suma.grid(row=9, column=4, padx=10, pady=15)

# Paleta P1, EURO
palety_label = ttk.Label(window, text="Palety", font=("Arial", 12, "bold"))
palety_label.grid(row=0, column=0, padx=10, pady=15)
palety_ilosc = ttk.Label(window, text="ilosc", font=("Arial", 12, "bold"))
palety_ilosc.grid(row=0, column=2, padx=10, pady=15)
palety_input = ttk.Entry(window, width=10)
palety_input.grid(row=0, column=3)
output_palety = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
output_palety.grid(row=0, column=4, padx=10, pady=15)

# Karton palety * 3.5 kg
karton_label = ttk.Label(window, text="Karton", font=("Arial", 12, "bold"))
karton_label.grid(row=1, column=0, padx=10, pady=15)
output_karton = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
output_karton.grid(row=1, column=4, padx=10, pady=15)

# Karton K1 * 0.7
k1_palety = ttk.Label(window, text="Palety", font=("Arial", 12, "bold"))
k1_palety.grid(row=5, column=0, padx=10, pady=15)
k1_k7_palety = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
k1_k7_palety.grid(row=5, column=4, padx=10, pady=15)
karton_ilosc_palet = ttk.Label(window, text="ilosc", font=("Arial", 12, "bold"))
karton_ilosc_palet.grid(row=5, column=2, padx=10, pady=15)
karton_input_palet = ttk.Entry(window, width=10)
karton_input_palet.grid(row=5, column=3)

k1_label = ttk.Label(window, text="Karton", font=("Arial", 12, "bold"))
k1_label.grid(row=6, column=0, padx=10, pady=15)
k1_k7_karton = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
k1_k7_karton.grid(row=6, column=4, padx=10, pady=15)
karton_ilosc = ttk.Label(window, text="ilosc", font=("Arial", 12, "bold"))
karton_ilosc.grid(row=6, column=2, padx=10, pady=15)
karton_input = ttk.Entry(window, width=10)
karton_input.grid(row=6, column=3)



nakretka_label = ttk.Label(window, text="Nakretka", font=("Arial", 12, "bold"))
nakretka_label.grid(row=7, column=0, padx=10, pady=15)
nakretka_input_ilosc = ttk.Entry(window, width=10)
nakretka_input_ilosc.grid(row=7, column=1, padx=10, pady=15)
nakretka_label = ttk.Label(window, text="Waga", font=("Arial", 12, "bold"))
nakretka_label.grid(row=7, column=2, padx=10, pady=15)
nakretka_input = ttk.Entry(window, width=10)
nakretka_input.grid(row=7, column=3, padx=10, pady=15)
output_nakretka = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
output_nakretka.grid(row=7, column=4, padx=10, pady=15)

# Folia palety * 0.5 kg     
folia_label = ttk.Label(window, text="Folia", font=("Arial", 12, "bold"))
folia_label.grid(row=2, column=0, padx=10, pady=15)
output_folia = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
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
output_butelka = ttk.Label(window, text=0, font=("Arial", 12, "bold"))
output_butelka.grid(row=3, column=4, padx=10, pady=15)






window.mainloop()