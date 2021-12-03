import turtle
import pandas as pd
Font =("Courier", 16, "normal")
image = "./us-states-game-start/blank_states_img.gif"
data = pd.read_csv("./us-states-game-start/50_states.csv")
print(data.columns)
my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
# Adding image to screen
my_screen.addshape(image)
turtle.shape(image)
game_is_on = True
guessed_states = [] # Allow user to select a state
# Game is on until 10 names entered would be correct
while len(guessed_states) < 10:
    user_ans = my_screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats another state name").title()
    X = data[data["state"] == user_ans]["x"]
    Y = data[data["state"] == user_ans]["y"]
    # print(f"X: {X}, Y: {Y}")
    # print(user_ans)
    # if user_ans is in list then creata a turtle to write the name of the state
    if user_ans == "Exit":
        missing_states = []
        for state in data["state"].to_list():
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_ans in data["state"].to_list():   # Need to convert tolist to check the presence
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(X), int(Y))
        # t.write(f"{user_ans}", align="center", font=Font)
        t.write(f"{user_ans}")
        guessed_states.append(user_ans)

# my_screen.exitonclick()
