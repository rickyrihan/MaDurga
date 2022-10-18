from time import sleep
from turtle import back, begin_fill, bgcolor, circle, color, end_fill, exitonclick, forward, goto, hideturtle, left, pendown, pensize, penup, right, speed

bgcolor("yellow")
speed(100)
hideturtle()

def position(x, y):
    penup()
    goto(x, y)
    pendown()

sleep(5)
position(0, 200)

# Foot

color("black")
begin_fill()
circle(40)
end_fill()

# Left eyebrow

position(-30, 200)
begin_fill()
right(45)
for i in range(20):
    left(3)
    back(10)
for i in range(10):
    right(3)
    back(10)
right(18)
for i in range(13):
    left(3)
    forward(10)
for i in range(20):
    right(2)
    forward(10)
end_fill()

# Right eyebrow

left(80)
position(30, 200)
begin_fill()
for i in range(20):
    right(3)
    forward(10)
for i in range(10):
    left(3)
    forward(10)
left(18)
for i in range(13):
    right(3)
    back(10)
for i in range(20):
    left(2)
    back(10)
end_fill()

# Right eye

position(40, 150)
pensize(15)
left(10)
for i in range(20):
    right(3)
    forward(10)
for i in range(10):
    left(3)
    forward(5)
right(3)
for i in range(10):
    left(3)
    back(10)
for i in range(20):
    right(3)
    back(10)
pensize(1)
position(130, 130)
begin_fill()
circle(40)
end_fill()
color("white")
begin_fill()
position(115, 175)
circle(10)
end_fill()

# Left eye

position(-40, 150)
color("black")
pensize(15)
right(25)
for i in range(20):
    left(3)
    back(10)
for i in range(10):
    right(3)
    back(5)
left(3)
for i in range(10):
    right(3)
    forward(10)
for i in range(20):
    left(3)
    forward(10)
pensize(1)
position(-130, 130)
begin_fill()
circle(40)
end_fill()
color("white")
begin_fill()
position(-155, 175)
circle(10)
end_fill()

# Nose

color("black")
position(-60, 10)
right(70)
for i in range(5, 12):
    pensize(i)
    left(7)
    forward(10)
for i in range(12, 5, -1):
    pensize(i)
    left(7)
    forward(10)

# Upper Lip

begin_fill()
position(-130, -90)
pensize(1)
begin_fill()
right(60)
for i in range(3):
    left(3)
    forward(5)
for i in range(10):
    left(4)
    forward(6)
for i in range(10):
    right(10)
    forward(7)
left(135)
for i in range(10):
    right(10)
    forward(7)
right(2)
for i in range(10):
    left(4)
    forward(6)
for i in range(3):
    left(3)
    forward(5)
right(160)
for i in range(12):
    right(3)
    forward(7.2)
left(44)
for i in range(15):
    right(5.5)
    forward(7)
left(44)
for i in range(12):
    right(3)
    forward(7)
end_fill()

# Lower Lip

begin_fill()
left(175)
for i in range(14):
    left(2)
    forward(5)
right(45)
for i in range(14):
    left(7)
    forward(10)
right(45)
for i in range(14):
    left(3)
    forward(5)
right(185)
for i in range(7):
    left(3)
    forward(10)
right(0.6)
for i in range(18):
    right(6)
    forward(10)
right(8)
for i in range(7):
    left(3)
    forward(10)
end_fill()

# Nose Ring

pensize(12)
color("red")
position(30, 0)
left(120)
for i in range(47):
    right(7)
    back(10)

# Signature | It says "Rinmay"|

left(110)
pensize(2)
color("blue")
position(200, -200)
right(90)
forward(50)
for i in range(17):
    right(10)
    forward(2)
right(15)
for i in range(35):
    right(1)
    forward(2)
for i in range(130):
    right(2)
    forward(1)
for i in range(21):
    right(10)
    forward(1)
forward(50)
right(5)
for i in range(6):
    left(135)
    forward(14)
    right(135)
    if i!=5:
        forward(14)
right(40)
forward(40)
right(90)
forward(5)
right(110)
forward(35)
left(140)
forward(150)
position(266, -195)
circle(1)

exitonclick()