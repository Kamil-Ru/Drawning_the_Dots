import turtle
import random

color_list = [(1, 150, 2), (14, 14, 14), (35, 28, 74), (58, 60, 72), (60, 31, 53), (79, 79, 90), (139, 139, 151),
              (177, 8, 10), (181, 160, 130), (187, 3, 0), (198, 134, 140), (206, 60, 7), (225, 93, 91), (230, 92, 95),
              (237, 206, 85), (239, 188, 0)]

tim = turtle
tim.penup()
tim.pensize(20)
tim.speed("fastest")
tim.colormode(255)
y = -300
side_of_the_square = 10

for dot_count in range(side_of_the_square):

    tim.setposition(-300, y)

    for dot_count in range(side_of_the_square):
        tim.dot(20, random.choice(color_list))

    y += 50

screen = turtle.Screen()
screen.exitonclick()
