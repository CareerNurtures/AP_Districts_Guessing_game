import pandas
import turtle

data = pandas.read_csv("AP_Cord.csv")
turtle.Screen().title("District guessing game")
bg_image = "apmap.gif"
turtle.Screen().addshape(bg_image)
turtle.Screen().screensize(canvwidth=400,canvheight=400)
turtle.Screen().setup(1080,700)
turtle.shape(bg_image)


states = data["Districts"].tolist()
score = 0
guessed = []


# NOTE : The co-ordinates work correctly only if u setup( 1080,700 ) else districts will place at wrong locations

while True:

    user_data = turtle.Screen().textinput(title=f"Score:{score}/13", prompt="Enter a district name: ").title()

    if user_data in states:

        if user_data not in guessed:
            score += 1
        guessed.append(user_data)
        myturtle = turtle.Turtle()
        myturtle.hideturtle()
        myturtle.penup()

        current_district = data[data.Districts == user_data]
        myturtle.goto(int(current_district.x), int(current_district.y))
        myturtle.write(user_data)

    if score == 13 or user_data == "End":
        break



