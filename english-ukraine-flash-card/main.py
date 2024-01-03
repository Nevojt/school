from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


try:
    data = pd.read_csv("english-ukraine-flash-card/data/england-ukraine.csv")
except FileNotFoundError:
    original_data = pd.read_csv("english-ukraine-flash-card/data/england-ukraine.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    

# England 
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front_imag)
    flip_timer = window.after(3000, func=flip_card)
    
    
# Flip card
def flip_card():
    canvas.itemconfig(card_title, text="Українська", fill="white")
    canvas.itemconfig(card_word, text=current_card["Ukraine"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)
    
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("english-ukraine-flash-card/datawords_to_learn.csv", index=False) 
    next_card()


window = Tk()
window.title("Flash Language")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



flip_timer = window.after(3000, func=flip_card)
# Create a frame
canvas = Canvas(window, width=800, height=526)
card_front_imag = PhotoImage(file="english-ukraine-flash-card/images/card_front.png")
card_back_image = PhotoImage(file="english-ukraine-flash-card/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_imag)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
cross_image = PhotoImage(file="english-ukraine-flash-card/images/wrong.png")
unknown_button = Button(window, image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="english-ukraine-flash-card/images/right.png")
correct_button = Button(window, image=check_image, command=is_known)
correct_button.grid(row=1, column=1)






next_card()


window.mainloop()