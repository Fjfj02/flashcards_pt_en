#flash cards to learn brazilian portuguese, you can delete your progress if you want (words_to_learn.csv), enjoy :)

BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

# ---------------------------- ERRORS AND EXCEPTIONS ------------------------------- #

card = {}
words = {}

#reading data
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/brazilianportuguese_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

# ---------------------------- CARDS FUNCTION ------------------------------- #

def next_card():
    '''function to pass the words'''
    global card, timer
    window.after_cancel(timer)
    card = random.choice(words)
    canvas1.itemconfig(language, text="Brazilian Portuguese", fill="black")
    canvas1.itemconfig(word, text=card["Brazilian Portuguese"], fill="black")
    canvas1.itemconfig(card_background, image=front_card)
    timer = window.after(2300, func=flip_card)

def flip_card():
    '''function to show the answer'''
    canvas1.itemconfig(language, text="English", fill="white")
    canvas1.itemconfig(word, text=card["English"], fill="white")
    canvas1.itemconfig(card_background, image=back_card)

def is_know():
    '''function to create a new document with the needed words'''
    words.remove(card)
    data = pandas.DataFrame(words)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

#create window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(2300, func=flip_card)

#put image
canvas1 = Canvas(width=800, height=526)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
card_background = canvas1.create_image(400, 263, image=front_card)
canvas1.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = canvas1.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas1.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas1.grid(column=0, row=0, columnspan=2)

#create buttons
x_image = PhotoImage(file="./images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_know)
check_button.grid(column=1, row=1)

#to init with something
next_card()

#app running
window.mainloop()