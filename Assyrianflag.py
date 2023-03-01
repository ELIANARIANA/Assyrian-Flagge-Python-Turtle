#Python Program to draw a filled with colour in Turtle  
import turtle 
T= turtle.Turtle()
tc1 = turtle.Turtle()       
tc2 = turtle.Turtle()  
tt1 = turtle.Turtle()
fr1 = turtle.Turtle()
fr2 = turtle.Turtle()
fr3 = turtle.Turtle()
fr4 = turtle.Turtle()
fb1 = turtle.Turtle()
fb2 = turtle.Turtle()
fb3 = turtle.Turtle()
fb4 = turtle.Turtle()
Ashur = turtle.Screen()

# pens speed  
tc1.speed(3)
tc2.speed(3)
tt1.speed(3)
fr1.speed(0)
fr2.speed(0)
fr3.speed(0)
fr4.speed(0)
fb1.speed(0)
fb2.speed(0)
fb3.speed(0)
fb4.speed(0)
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



#fly1 red left 
fr1.color("Red2")
fr1.up()
fr1.goto(-80,48)
fr1.down()
fr1.begin_fill()
fr1.left(135)
fr1.forward(75)
fr1.circle(-75,45)
fr1.circle(75,80)
fr1.circle(-75,80)
fr1.circle(75,80)
fr1.circle(-75,50)

fr1.left(90)
fr1.forward(30)
fr1.right(90)


fr1.circle(-75,-50)
fr1.circle(75,-80)
fr1.circle(-75,-80)
fr1.circle(75,-80)
fr1.circle(-75,-45)
fr1.backward(75)
fr1.goto(-80,48)

fr1.hideturtle()
fr1.end_fill()



#fly1 Blue left 
fb1.color("Blue")
fb1.up()
fb1.goto(-55,60)
fb1.down()
fb1.begin_fill()
fb1.left(135)
fb1.forward(75)
fb1.circle(-75,45)
fb1.circle(75,80)
fb1.circle(-75,80)
fb1.circle(75,80)
fb1.circle(-75,50)


fb1.right(90)
fb1.forward(30)
fb1.left(90)

fb1.circle(-75,-50)
fb1.circle(75,-80)
fb1.circle(-75,-80)
fb1.circle(75,-80)
fb1.circle(-75,-45)
fb1.backward(75)
fb1.goto(-55,60)

fb1.hideturtle()
fb1.end_fill()




#fly2 red right 
fr2.color("red2")
fr2.up()
fr2.goto(80,48)
fr2.down()
fr2.begin_fill()
fr2.right(135)
fr2.backward(75)
fr2.circle(-75,-45)
fr2.circle(75,-80)
fr2.circle(-75,-80)
fr2.circle(75,-80)
fr2.circle(-75,-50)

fr2.left(90)
fr2.forward(30)
fr2.right(90)

fr2.circle(-75,50)
fr2.circle(75,80)
fr2.circle(-75,80)
fr2.circle(75,80)
fr2.circle(-75,45)
fr2.backward(-75)
fr2.goto(80,48)

fr2.hideturtle()
fr2.end_fill()


#fly2 Blue left 
fb2.color("Blue")
fb2.up()
fb2.goto(52,60)
fb2.down()
fb2.begin_fill()
fb2.right(135)
fb2.backward(75)
fb2.circle(-75,-45)
fb2.circle(75,-80)
fb2.circle(-75,-80)
fb2.circle(75,-80)
fb2.circle(-75,-50)

fb2.right(90)
fb2.forward(30)
fb2.left(90)

fb2.circle(-75,50)
fb2.circle(75,80)
fb2.circle(-75,80)
fb2.circle(75,80)
fb2.circle(-75,45)
fb2.backward(-75)
fb2.goto(52,60)
fb2.hideturtle()
fb2.end_fill()


#fly3 red left
fr3.color("Red2")
fr3.up()
fr3.goto(-55,-60)
fr3.down()
fr3.begin_fill()
fr3.right(135)
fr3.forward(75)
fr3.circle(-75,45)
fr3.circle(75,80)
fr3.circle(-75,80)
fr3.circle(75,80)
fr3.circle(-75,50)

fr3.left(90)
fr3.forward(30)
fr3.right(90)

fr3.circle(-75,-50)
fr3.circle(75,-80)
fr3.circle(-75,-80)
fr3.circle(75,-80)
fr3.circle(-75,-45)
fr3.backward(75)
fr3.goto(-55,-60)

fr3.hideturtle()
fr3.end_fill()

#fly3 blue left
fb3.color("Blue")
fb3.up()
fb3.goto(-80,-48)
fb3.down()
fb3.begin_fill()
fb3.right(135)
fb3.forward(75)
fb3.circle(-75,45)
fb3.circle(75,80)
fb3.circle(-75,80)
fb3.circle(75,80)
fb3.circle(-75,50)

fb3.right(90)
fb3.forward(30)
fb3.left(90)


fb3.circle(-75,-50)
fb3.circle(75,-80)
fb3.circle(-75,-80)
fb3.circle(75,-80)
fb3.circle(-75,-45)
fb3.backward(75)
fb3.goto(-80,-48)

fb3.hideturtle()
fb3.end_fill()


#fly4 red right
fr4.color("Red2")
fr4.up()
fr4.goto(45,-60)
fr4.down()
fr4.begin_fill()
fr4.left(135)
fr4.backward(75)
fr4.circle(-75,-45)
fr4.circle(75,-80)
fr4.circle(-75,-80)
fr4.circle(75,-80)
fr4.circle(-75,-50)

fr4.left(90)
fr4.forward(30)
fr4.right(90)

fr4.circle(-75,50)
fr4.circle(75,80)
fr4.circle(-75,80)
fr4.circle(75,80)
fr4.circle(-75,45)
fr4.backward(-75)
fr4.goto(45,-60)

fr4.hideturtle()
fr4.end_fill()


#fly4 blue right
fb4.color("Blue")
fb4.up()
fb4.goto(80,-48)
fb4.down()
fb4.begin_fill()
fb4.left(135)
fb4.backward(75)
fb4.circle(-75,-45)
fb4.circle(75,-80)
fb4.circle(-75,-80)
fb4.circle(75,-80)
fb4.circle(-75,-50)

fb4.right(90)
fb4.forward(30)
fb4.left(90)


fb4.circle(-75,50)
fb4.circle(75,80)
fb4.circle(-75,80)
fb4.circle(75,80)
fb4.circle(-75,45)
fb4.backward(-75)
fb4.goto(80,-48)

fb4.hideturtle()
fb4.end_fill()

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