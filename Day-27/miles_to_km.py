from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)

def miles_to_km():
    miles_val = miles.get()
    km = round(float(miles_val) * 1.609, 3)
    miles_label.config(text=km)

#Entry to get miles
miles = Entry(width=20)
print(miles.get())
miles.grid(column=1,row=0)



#Label to write miles
miles_label = Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=3, row=0)
miles_label.config(padx=10, pady=10)

#Label to write is equal to
miles_label = Label(text="is equal to", font=("Arial", 14))
miles_label.grid(column=0, row=1)
miles_label.config(padx=10, pady=10)

#Label to show km
miles_label = Label(text="0", font=("Arial", 14))
miles_label.grid(column=1, row=1)
miles_label.config(padx=10, pady=10)

#Label to write km
km_label = Label(text="km", font=("Arial", 14))
km_label.grid(column=3, row=1)
km_label.config(padx=10, pady=10)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
