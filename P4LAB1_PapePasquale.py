# Pasquale Pape
# 10/28/2024
# P4LAB1
# while loop to make a square using turtle

import turtle
#set up the window and turtle object
window = turtle.Screen
t = turtle.Turtle()

t.pensize(6)
t.pencolor("green")
t.shape("turtle")

#while loop to draw sides of square
line = 0
while line < 4:
    t.right(90)
    t.forward(150)
    line += 1

#for loop to draw sides of triangle
for line1 in range(3):
    t.left(120)
    t.forward(150)
