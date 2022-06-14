import random
from turtle import Turtle,Screen
import turtle

from scipy import rand

# Generated colors from main picture
color_list = [(44, 95, 148), (179, 46, 75), (227, 208, 100), (209, 156, 88), (179, 169, 33), (137, 88, 63), (115, 179, 209), (201, 74, 121), (214, 130, 174), (229, 70, 50), (90, 104, 191), (46, 166, 119), (27, 146, 84), (122, 218, 208), (52, 56, 93), (121, 43, 71), (119, 47, 36), (35, 183, 194), (227, 170, 189), (128, 185, 162), (174, 186, 220), (156, 206, 217), (234, 171, 162), (51, 54, 70), (211, 209, 39), (87, 43, 32)]

t = Turtle()

turtle.colormode(255)
t.penup()
t.ht()
t.setheading(225)
t.forward(250)
t.setheading(0)

number_of_dot = 101

for i in range(1, number_of_dot):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)




screen = Screen()
screen.exitonclick()