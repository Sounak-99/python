import turtle

def draw():
    turtle.color("red")
    turtle.begin_fill()
    turtle.pensize(10)
    turtle.left(50)
    turtle.forward(262)
    turtle.circle(100, 200)
    turtle.right(140)
    turtle.circle(100, 200)
    turtle.forward(262)
    turtle.end_fill()

def write_name(name):
    turtle.penup()
    turtle.setpos(-50, 50)
    turtle.pendown()
    turtle.color("white")
    turtle.write(name, font=("Arial", 24, "bold"))

def main():
    turtle.bgcolor("white")
    draw()
    write_name("ok")
    turtle.hideturtle()
    turtle.done()

def run_program():
    main()

run_program()
