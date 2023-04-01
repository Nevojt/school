from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.geometry("300x150")
window.config(padx=15, pady=15)



label = Label(window, text="Miles", font=("Arial", 15))
label.grid(row=0, column=2)
label.config(padx=15, pady=10)

is_equal_to = Label(window, text="is equal to", font=("Arial", 14))
is_equal_to.grid(row=1, column=0)

output = Label(window, text="0", font=("Arial", 15, "bold"))
output.grid(row=1, column=1)

label_km = Label(window, text="Km", font=("Arial", 15))
label_km.grid(row=1, column=2)


input_ml = Entry(window, width=7)
input_ml.grid(row=0, column=1)

def calculates():
    output.config(text=float(input_ml.get()) * 1.609)
    

button = Button(window, text="Calculate", command=calculates, font=("Arial", 13))
button.grid(row=2, column=1)


window.mainloop()
