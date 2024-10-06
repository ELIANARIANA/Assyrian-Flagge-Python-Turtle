#Python Program to draw a filled with colour in Turtle  
import turtle 
T= turtle.Turtle()
tc1 = turtle.Turtle()       
tc2 = turtle.Turtle()  
tt1 = turtle.Turtle()
Ashur = turtle.Screen()

# region: General constants

# region: Colors
COLOR_RED    = "Red2"
COLOR_BLUE   = "Blue"
COLOR_BODY   = "#00BFFF"
COLOR_WHITE  = "White"
COLOR_ORANGE = "Orange"
# endregion

# region: Direction
DIRECTION_LEFT     = "left"
DIRECTION_RIGHT    = "right"
DIRECTION_FORWARD  = "forward"
DIRECTION_BACKWARD = "backward"
#endregion

# endregion  
# pens speed  
tc1.speed(3)
tc2.speed(3)
tt1.speed(3)
T.speed(0)

#coordinate axis
T.forward (900)
T.back (1800)
T.home()
T.left (90)
T.forward (400)
T.back (800)
T.home()
T.hideturtle()

# region: Methods Helper
def draw_wing(color, start_pos, left_right_direction, for_back_ward):
    t = turtle.Turtle()

    t.speed(0)
    t.color(color)
    t.up()
    t.goto(start_pos)
    t.down()
    t.begin_fill()

    if left_right_direction == DIRECTION_LEFT:
        t.left(135)
    else:
        t.right(135)

    if for_back_ward == DIRECTION_FORWARD:
        t.forward(75)
        t.circle(-75, 45)
        t.circle(75 , 80)
        t.circle(-75, 80)
        t.circle(75 , 80)
        t.circle(-75, 50)
    else:
        t.backward(75)
        t.circle(-75, -45)
        t.circle(75 , -80)
        t.circle(-75, -80)
        t.circle(75 , -80)
        t.circle(-75, -50)

    if color == COLOR_RED:
        t.left(90)
    else:
        t.right(90)

    t.forward(30)

    if color == COLOR_RED:
        t.right(90)
    else:
        t.left(90)
    
    if for_back_ward == DIRECTION_FORWARD:
        t.circle(-75, -50)
        t.circle(75 , -80)
        t.circle(-75, -80)
        t.circle(75 , -80)
        t.circle(-75, -45)
        t.backward(75)
    else:
        t.circle(-75, 50)
        t.circle(75 , 80)
        t.circle(-75, 80)
        t.circle(75 , 80)
        t.circle(-75, 45)
        t.backward(-75)
    
    t.goto(start_pos)

    t.hideturtle()
    t.end_fill()

# endregion


#fly1 red and blue left up
draw_wing(COLOR_RED , (-80,48), DIRECTION_LEFT, DIRECTION_FORWARD)
draw_wing(COLOR_BLUE, (-55,60), DIRECTION_LEFT, DIRECTION_FORWARD)

#fly2 red and blue right up
draw_wing(COLOR_RED , (80,48), DIRECTION_RIGHT, DIRECTION_BACKWARD)
draw_wing(COLOR_BLUE, (52,60), DIRECTION_RIGHT, DIRECTION_BACKWARD)

#fly3 red and blue left down
draw_wing(COLOR_RED , (-55,-60), DIRECTION_RIGHT, DIRECTION_FORWARD)
draw_wing(COLOR_BLUE, (-80,-48), DIRECTION_RIGHT, DIRECTION_FORWARD)

#fly4 red and blue right down
draw_wing(COLOR_RED , (45,-60), DIRECTION_LEFT, DIRECTION_BACKWARD)
draw_wing(COLOR_BLUE, (80,-48), DIRECTION_LEFT, DIRECTION_BACKWARD)

#body
tt1.up()
tt1.goto(52.5,-55)
tt1.down()
width = 250
angle = 13.00
angledu = 66

tt1.color(COLOR_BODY)
tt1.begin_fill()

tt1.left(angle)
tt1.fd(width)

tt1.right(angle=+25)
tt1.bk(width)

tt1.right(angledu)
tt1.bk(width)

tt1.right(angle=+25) #angledu=+25
tt1.fd(width)


tt1.right(64.5)
tt1.fd(width)

tt1.right(25)
tt1.bk(width)

tt1.right(64.5)
tt1.bk(width)

tt1.right(25)
tt1.fd(width)


tt1.hideturtle()
tt1.end_fill()



#Fist circle
tc1.color(COLOR_WHITE)  
tc1.up()
tc1.goto(0,-65)
tc1.down()
#Instructing to "begin" and "end" filling the "circle"  
tc1.begin_fill()  
tc1.circle(65)  
tc1.hideturtle()
tc1.end_fill()  





#Second circle 
tc2.color(COLOR_ORANGE)  
tc2.up()
tc2.goto(0,-50)
tc2.down()
#Instructing to "begin" and "end" filling the "circle"  
tc2.begin_fill()  
tc2.circle(50)  
tc2.hideturtle()
tc2.end_fill()  

#Clear  coordinate axis
T.clear()



#add Ashur image 
from PIL import Image
im = Image.open("Ashur.gif")

new_size = (int(im.size[0]/3), int(im.size[1]/3))
im = im.resize(new_size)
im.save("example_resized.gif")
turtle.register_shape("example_resized.gif")

tAsh = turtle.Turtle()

tAsh.shape("example_resized.gif")
tAsh.color(COLOR_WHITE)
tAsh.penup()
tAsh.goto(0, 400)


turtle.done()  