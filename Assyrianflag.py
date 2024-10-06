#Python Program to draw a filled with colour in Turtle  
import turtle 
T= turtle.Turtle()
tc1 = turtle.Turtle()       
tc2 = turtle.Turtle()  
tt1 = turtle.Turtle()
Ashur = turtle.Screen()

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
def draw_fly(color, start_pos, left_right_direction, for_back_ward):
    t = turtle.Turtle()

    t.speed(0)
    t.color(color)
    t.up()
    t.goto(start_pos)
    t.down()
    t.begin_fill()

    if left_right_direction == "left":
        t.left(135)
    else:
        t.right(135)

    if for_back_ward == "forward":
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

    if color == "Red2":
        t.left(90)
    else:
        t.right(90)

    t.forward(30)

    if color == "Red2":
        t.right(90)
    else:
        t.left(90)
    
    if for_back_ward == "forward":
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
draw_fly("Red2", (-80,48), "left", "forward")
draw_fly("Blue", (-55,60), "left", "forward")

#fly2 red and blue right up
draw_fly("Red2", (80,48), "right", "backward")
draw_fly("Blue", (52,60), "right", "backward")

#fly3 red and blue left down
draw_fly("Red2", (-55,-60), "right", "forward")
draw_fly("Blue", (-80,-48), "right", "forward")

#fly4 red and blue right down
draw_fly("Red2", (45,-60), "left", "backward")
draw_fly("Blue", (80,-48), "left", "backward")

#body
tt1.up()
tt1.goto(52.5,-55)
tt1.down()
width = 250
angle = 13.00
angledu = 66

tt1.color("#00BFFF")
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
tc1.color("White")  
tc1.up()
tc1.goto(0,-65)
tc1.down()
#Instructing to "begin" and "end" filling the "circle"  
tc1.begin_fill()  
tc1.circle(65)  
tc1.hideturtle()
tc1.end_fill()  





#Second circle 
tc2.color("Orange")  
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
tAsh.color("White")
tAsh.penup()
tAsh.goto(0, 400)


turtle.done()  