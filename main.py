import turtle
import pandas

screen = turtle.Screen()
screen.screensize(700, 900)
screen.title("Indian States and UTs Game")

# Loading image to the screen
image = "india_map.gif"
screen.bgpic(image)  

tur = turtle.Turtle()
tur.penup()
tur.hideturtle()

data = pandas.read_csv("indian_states.csv")
states_list = data["states"].to_list()
temp_state_list = states_list  

should_continue = True
correct = 0  # to keep the count of correct answer given by user
guessed_states = []  # To store all states guessed correctly

while should_continue:
    answer_state = screen.textinput(title=f"Guess the State {correct} / 36", prompt="What's another state's name? ").lower()
    # When user input exit, game should stop and generate a csv file containing all states missed by user

    if answer_state == "exit":
        missing_states = []  # To store all states missed by user when user exit from game

        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        # Now we have to make csv file of missed_states
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_you_missed.csv")
        # Also printing those states on terminal
        print("Missing states are: \n")
        print(missing_states)

        break  

    for state in temp_state_list:
        if state.lower() == answer_state:
            guessed_states.append(state)

            # now when the answer matches we should take that particular row and get it's x, y coordinate
            state_row = data[data["states"] == state]  # getting the row of answer_state and save it as a list
            x_co = int(state_row["x"])  
            y_co = int(state_row["y"]) 

            tur.goto(x_co, y_co)
            tur.write(state, align="center")

            correct += 1
            # Now we have to remove the guessed state from temp_state_list so that same ans don't get counted again
            temp_state_list.remove(state)

    if correct == 36:
        tur.goto(0, 0)
        tur.write("Congrats! You Guessed all States and UTs correctly", align="center", font = ("Arial’", 20, "normal"))
        should_continue = False
        screen.exitonclick()  




