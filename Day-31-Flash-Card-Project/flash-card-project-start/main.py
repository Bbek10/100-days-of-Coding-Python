import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR2 = "#FFFFFF"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/deutchEnglish5000.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # always go through documentation or at least video of the documentation
    to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(card_title, text="Deutch", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)




# setup a window
window = Tk()
window.title("FlashCardiB")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# set up a canvas - that allows us to overlap anything if it has its coordinates defined using Grid
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
# x 400 y 263 for image ( relative to canvas size  i.e w 800 and height 526 )
card_background = canvas.create_image(400, 263, image=card_front_image)
# x y for text
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


# Buttons -> need command to call the function
# Need buttons to have an Image
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=1)

tick_image = PhotoImage(file="images/right.png")
known_button = Button(image=tick_image, command=is_known)
known_button.grid(row=1, column=0)
next_card()


window.mainloop()
