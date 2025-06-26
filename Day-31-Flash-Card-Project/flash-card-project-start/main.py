from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# setup a window
window = Tk()
window.title("FlashCardiB")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

# set up a canvas - that allows us to overlap anything if it has its coordinates defined using Grid
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front_image = PhotoImage(file="images/card_front.png")
# x 400 y 263 for image ( relative to canvas size  i.e w 800 and height 526 )
canvas.create_image(400, 263, image=card_front_image)
# x y for text
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

# Buttons
# Need buttons to have an Image
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image)
unknown_button.grid(row=1, column=1)

tick_image = PhotoImage(file="images/right.png")
known_button = Button(image=tick_image)
known_button.grid(row=1, column=0)



window.mainloop()
