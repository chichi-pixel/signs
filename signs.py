import turtle
import colorsys

#create window to display pattern

t = turtle.Turtle()
s=turtle.Screen()

#setting background color

s.bgcolor("black")

# speed of purple to draw pattern

t.speed(2)

h = 0
n = 30

#loop for drawing pattern
for i in range(450):
    c = colorsys.hsv_to_rgb(h, 1, 0.10)
    h+=1/n
    t.color(c)
    t.left(145)
    for m in range(5):
        t.forward(300)
        t.left(150)



