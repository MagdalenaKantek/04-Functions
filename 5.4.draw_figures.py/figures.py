
import turtle

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)


# Draw a square
def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)


# Draw an equilateral triangle
def draw_triangle(length):
    for i in range(3):
        pen.forward(length)
        pen.right(120)


# Draw a rectangle
def draw_rectangle(length_a, length_b):
    for i in range(4):
        if i % 2 == 0:
            pen.forward(length_a)
        else:
            pen.forward(length_b)
        pen.right(90)
