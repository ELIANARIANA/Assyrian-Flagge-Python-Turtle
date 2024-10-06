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

def draw_body(color, start_pos):
    t = turtle.Turtle()
    t.up()
    t.goto(start_pos)
    t.down()
    width = 250
    angle = 13.00
    angledu = 66

    t.color(color)
    t.begin_fill()

    t.left(angle)
    t.fd(width)

    t.right(angle=+25)
    t.bk(width)

    t.right(angledu)
    t.bk(width)

    t.right(angle=+25) #angledu=+25
    t.fd(width)


    t.right(64.5)
    t.fd(width)

    t.right(25)
    t.bk(width)

    t.right(64.5)
    t.bk(width)

    t.right(25)
    t.fd(width)

    t.hideturtle()
    t.end_fill()

def draw_circle(color ,start_pos, diameter):
    t = turtle.Turtle()
    t.speed(3)
    t.color(color)  
    t.up()
    t.goto(start_pos)
    t.down()
    #Instructing to "begin" and "end" filling the "circle"  
    t.begin_fill()  
    t.circle(diameter)  
    t.hideturtle()
    t.end_fill()  

def resize_and_add_image(image, image_pos):
    from PIL import Image
    im = Image.open(image)

    new_size = (int(im.size[0]/3), int(im.size[1]/3))
    im = im.resize(new_size)
    im.save("{image}_resized.gif")

    turtle.register_shape("{image}_resized.gif")

    tAsh = turtle.Turtle()

    tAsh.shape("{image}_resized.gif")
    tAsh.color(COLOR_WHITE)
    tAsh.penup()
    tAsh.goto(image_pos)
    
# endregion

# region: Draw all the wings of the Assyrian flag
#wing1 red and blue left up
draw_wing(COLOR_RED , (-80,48), DIRECTION_LEFT, DIRECTION_FORWARD)
draw_wing(COLOR_BLUE, (-55,60), DIRECTION_LEFT, DIRECTION_FORWARD)

#wing2 red and blue right up
draw_wing(COLOR_RED , (80,48), DIRECTION_RIGHT, DIRECTION_BACKWARD)
draw_wing(COLOR_BLUE, (52,60), DIRECTION_RIGHT, DIRECTION_BACKWARD)

#wing3 red and blue left down
draw_wing(COLOR_RED , (-55,-60), DIRECTION_RIGHT, DIRECTION_FORWARD)
draw_wing(COLOR_BLUE, (-80,-48), DIRECTION_RIGHT, DIRECTION_FORWARD)

#wing4 red and blue right down
draw_wing(COLOR_RED , (45,-60), DIRECTION_LEFT, DIRECTION_BACKWARD)
draw_wing(COLOR_BLUE, (80,-48), DIRECTION_LEFT, DIRECTION_BACKWARD)
# endregion

# region: Draw the body of the Assyrian flag
draw_body(COLOR_BODY, (52.5,-55))
# endregion

# region: Draw the circles of the Assyrian flag
#Fist circle
draw_circle(COLOR_WHITE, (0, -65), 65)

#Second circle 
draw_circle(COLOR_ORANGE, (0,-50), 50)  
# endregion

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