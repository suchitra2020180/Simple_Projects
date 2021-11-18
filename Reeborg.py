Reeborg.com

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()
    

#turn_left()
#turn_left()
#turn_left()
def condition():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        move()
        turn_right()
        turn_right()
        turn_left()
        #move()
    #turn_right()
while not at_goal():
    condition()