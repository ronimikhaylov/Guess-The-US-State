import turtle
from tkinter import messagebox


screen = turtle.Screen()
screen.title("U. S. States Game")
image = 'blank_states_img.gif'
data = "50_states.csv"

#display the blank_states_img.gif image

screen.addshape(image)
screen.bgpic(image)
#display a text box to enter the name of the state  
#the top of the text box should have the number of states left to guess
states_dict = {}
num_states_guessed = 0
states_guessed = []
with open (data, 'r') as f:
    #read the data file and store the data in a dictionary with the state name as the key and the x and y coordinates as the value in a tuple
    for line in f:
        state, x, y = line.split(',')
        states_dict[state] = (x, y)
    f.close()
    #store the states as a key, and the numbers as a tuple
#make the turtle invisible
turtle.hideturtle()
turtle.penup()

for key in states_dict:
    message_box = turtle.textinput(title = f'{num_states_guessed}/50 States Guessed', prompt = 'Enter a state:')
    message_box = message_box.title()
    if message_box in states_dict and message_box not in states_guessed:
        num_states_guessed += 1
        #move the turtle to the x and y coordinates of the state
        # if the state is in the dictionary, then move the turtle to the x and y coordinates of the state
        turtle.goto(int(states_dict[message_box][0]), int(states_dict[message_box][1]))
        turtle.write(message_box, font = ('Arial', 12, 'normal'))
        states_guessed.append(message_box)
    elif message_box.lower() == 'exit':
        #save the states that have been guessed and the number of states guessed
        with open('game_summary.csv', 'w') as f:
            states_misseed = list(set(states_dict.keys()) - set(states_guessed))
            f.write(f'States Missed:\n')
            
            for state in states_misseed:
                f.write(state + '\n')
            f.write(f'\nStates Guessed:\n')
            for state in states_guessed:
                f.write(state + '\n')

            f.close()
            break
    elif message_box in states_guessed:
        messagebox.showinfo(title = 'State Already Guessed', message = 'You have already guessed this state')

    else:
        messagebox.showinfo(title = 'State Not Found', message = 'The state you entered was not found')
    if len(states_guessed) == 50:
        messagebox.showinfo(title = 'You Win', message = 'You have guessed all 50 states')
        break
        #in a box, display the message "You have already guessed this state"

        
screen.exitonclick()

    
        

