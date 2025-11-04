import turtle

def draw_circle(pen, size):
    pen.circle(size)

def draw_square(pen, size):
    for i in range(4):
        pen.forward(size * 1.5)
        pen.left(90)

def draw_triangle(pen, size):
    for i in range(3):
        pen.forward(size * 1.5)
        pen.left(120)

def draw_attractive_design6():
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta", "gold", "coral", "navy", "olive", "maroon", "teal", "violet"]
    shapes = [draw_circle, draw_square, draw_triangle]
    
    pen = turtle.Turtle()
    pen.speed(0)
    turtle.bgcolor("black") 
    pen.pensize(1)

    for i in range(36):
        pen.color(colors[i % 15])
        current_shape = shapes[i % 3]
        current_shape(pen, 100)
        
        pen.left(10)

    pen.hideturtle()

draw_attractive_design6()
turtle.done()
