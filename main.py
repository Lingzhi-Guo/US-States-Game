import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

correct_answer = 0
correct_answer_list = []
states_info = pandas.read_csv("50_states.csv")
state_list = states_info["state"].to_list()

while correct_answer < 50:
    answer_state = screen.textinput(title=f"Guess the state ({correct_answer}/50)", prompt="What's another state's name?")
    answer_state = answer_state.capitalize()

    if answer_state in state_list:
        if answer_state not in correct_answer_list:
            correct_answer += 1
            correct_answer_list.append(answer_state)
            x_cor = states_info[states_info.state == answer_state].x.item()
            y_cor = states_info[states_info.state == answer_state].y.item()
            state_turtle = turtle.Turtle()
            state_turtle.penup()
            state_turtle.hideturtle()
            state_turtle.goto(x=x_cor, y=y_cor)
            state_turtle.write(arg=answer_state, move=False, font=("Helvetica", 17, "normal"))

    elif answer_state == "Exit":
        output_list = []
        for state in state_list:
            if state not in correct_answer_list:
                output_list.append(state)
        output = pandas.DataFrame(output_list)
        output.to_csv("States_You_Missed.csv")
        break
    else:
        pass

state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()
state_turtle.goto(x=-200, y=0)
state_turtle.color("red")
state_turtle.write(arg="Congratulations! You won!", move=False, font=("Helvetica", 30, "normal"))











screen.exitonclick()