import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

states = pandas.read_csv("50_states.csv")
# print(states)
states_list = states.state.to_list()
correct_guess_list = []
missed_state_list = []

# print(states_list)

ralph = turtle.Turtle("square")
ralph.hideturtle()
ralph.penup()
ralph.pencolor("black")

game_start = screen.textinput("U.S. State Guessing Game", "Ready to guess? Type 'Y' or 'N'").lower()

if game_start == 'y':
    total_states = 50
    correct_guess = 0

    while correct_guess < total_states:

        if correct_guess == 0:
            user_guess = screen.textinput(f"{correct_guess}/{total_states}", "Whats your first state?").title()

        else:
            user_guess = screen.textinput(f"{correct_guess}/{total_states}", "Whats the next state?").title()

        if user_guess == 'Exit':
            break

        else:
            for state in states_list:

                if state == user_guess:

                    if state not in correct_guess_list:
                        correct_guess += 1
                        x = states.x[states.state == state].item()
                        y = states.y[states.state == state].item()
                        print(f"{state} = {x, y}")
                        ralph.setposition(x, y)
                        ralph.write(state, False, 'center', ("Sans Seriff", 7, 'normal'))
                        correct_guess_list.append(state)

print(f"Number of Correct guesses = {correct_guess}, \nNumber of missed = {50-(correct_guess)}, \nGuessed States = {correct_guess_list}")

# for state in states_list:
#     if state not in correct_guess_list:
#         missed_state_list.append(state)

missed_state_list = [state for state in states_list if state not in correct_guess_list]
print(f"Missed States = {missed_state_list}")

data = pandas.DataFrame(missed_state_list)
data.to_csv("Missed State List.csv")


"""============================================"""
"""==============tutle_on_click_coor=================="""

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

"""==============tutle_on_click_coor=================="""
"""============================================"""