
import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")


# First square
figures.pen.penup()
figures.pen.goto(-250, 120)
figures.pen.pendown()
figures.draw_square(100)

# Second square
figures.pen.penup()
figures.pen.goto(-120, 120)
figures.pen.pendown()
figures.draw_square(100)


# First triangle
figures.pen.penup()
figures.pen.goto(30, 120)
figures.pen.pendown()
figures.draw_triangle(80)

# Second triangle
figures.pen.penup()
figures.pen.goto(170, 120)
figures.pen.pendown()
figures.draw_triangle(80)


# First rectangle
figures.pen.penup()
figures.pen.goto(-250, -80)
figures.pen.pendown()
figures.draw_rectangle(100, 60)

# Second rectangle
figures.pen.penup()
figures.pen.goto(0, -80)
figures.pen.pendown()
figures.draw_rectangle(100, 60)


# Hide the turtle and finish
figures.pen.hideturtle()
window.mainloop()
