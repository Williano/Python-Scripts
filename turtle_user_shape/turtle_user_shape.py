import turtle

window = turtle.Screen()
window.setup()
window.title("Draw User Shape")
window.bgcolor("purple")

mat = turtle.Turtle()
mat.shape("turtle")
mat.color("black")
mat.pensize(3)
mat.speed(12)


drawing = True

while drawing:

    mat.penup()

    SQUARE = 1
    TRIANGLE = 2
    QUIT = 0

    shape_choice = int(input("What do you want me to draw? (1 = square, 2 = triangle, 0 = quit):"))

    if shape_choice == SQUARE:
        side_length = int(input("How long do you want the sides of your square to be?"
                                "Please enter the number of pixels (e.g. 100):"))

        mat.pendown()

        x_pos = int(mat.xcor())
        y_pos = int(mat.ycor())
        heading = int(mat.heading())
        print("My 1st corner is at: {}, {} and my heading is {}".format(x_pos, y_pos, heading))

        mat.forward(side_length)
        x_pos = int(mat.xcor())
        y_pos = int(mat.ycor())
        heading = int(mat.heading())
        print("My 2nd corner is at: {}, {} and my heading is {}".format(x_pos, y_pos, heading))
        mat.left(90)

        mat.forward(side_length)
        x_pos = int(mat.xcor())
        y_pos = int(mat.ycor())
        heading = int(mat.heading())
        print("My 3rd corner is at: {}, {} and my heading is {}".format(x_pos, y_pos, heading))
        mat.left(90)

        mat.forward(side_length)
        x_pos = int(mat.xcor())
        y_pos = int(mat.ycor())
        heading = int(mat.heading())
        print("My 4th corner is at: {}, {} and my heading is {}".format(x_pos, y_pos, heading))
        mat.left(90)
        mat.forward(side_length)

    elif shape_choice == TRIANGLE:

        print("I will draw an equilateral triangle.")
        side_length = int(input("How long do you want the sides of your triangle to be?"
                                "Please enter the number of pixels (e.g. 100): "))

        mat.pendown()

        x_pos = int(mat.xcor())
        y_pos = int(mat.ycor())
        heading = int(mat.heading())
        print("My 1st corner is at: {}, {} and my heading is {}".format(x_pos, y_pos, heading))

        mat.forward(side_length)
        x_pos = int(mat.xcor())
        y_pos = int(mat.ycor())
        heading = int(mat.heading())
        print("My 2nd corner is at: {}, {} and my heading is {}".format(x_pos, y_pos, heading))
        mat.left(120)

        mat.forward(side_length)
        x_pos = int(mat.xcor())
        y_pos = int(mat.ycor())
        heading = int(mat.heading())
        print("My 3rd corner is at: {}, {} and my heading is {}".format(x_pos, y_pos, heading))
        mat.left(120)
        mat.forward(side_length)
        mat.left(120)

    else:
        drawing = False
else:
    print("Thank you for playing")


