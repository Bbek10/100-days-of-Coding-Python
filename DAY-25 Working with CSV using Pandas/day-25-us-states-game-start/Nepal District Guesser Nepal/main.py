import turtle
import pandas

screen = turtle.Screen()
image = "image.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("Nepal District Guess")
screen.setup(width=900, height=600)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv("district.csv")
all_districts = data["district"].to_list()

guessed_district = []

while len(guessed_district) < 75:
    answer_district = screen.textinput(title=f"{len(guessed_district)}/75 District guessed",prompt="What's the next district").title()
    #if the guess is Exit
    if answer_district == "Exit":
        missing_district = []
        for district in all_districts:
            if district not in guessed_district:
                missing_district.append(district)
        district_rem = pandas.DataFrame(missing_district)
        district_rem.to_csv("district_to_learn.csv")
        break
    #if the answer is right
    if answer_district in all_districts:
        guessed_district.append(answer_district)
        district_data = data[data.district == answer_district]
        x_cor = int(data[data.district == answer_district].x)
        y_cor = int(data[data.district == answer_district].y)
        t.goto(x_cor,y_cor-5)
        t.write(answer_district, align="center", font=("Arial", 6, "bold"))


turtle.exitonclick()