import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.geometry('400x200')

def handle_choice():
    user_choice = simpledialog.askstring("Вхід", "Ваш вибір напою?")
    # тут виконати логіку вашої кавомашини
    label.config(text=f"Ви обрали: {user_choice}")

label = tk.Label(root, text="Оберіть напій з меню")
label.pack(pady=20)

button = tk.Button(root, text="Обрати", command=handle_choice)
button.pack(pady=20)

root.mainloop()
