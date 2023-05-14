import turtle
import random
import time
from dog_template import draw_circle, draw_triangle, draw_rectangle, move_turtle

# Set up the turtle canvas
canvas = turtle.Screen()
canvas.setup(width=800, height=600)
turtle.hideturtle()  # Hide the turtle cursor
turtle.speed(0)  # Set the turtle speed to the fastest

# Set up the turtle window coordinates
left_bound = -400
right_bound = 400
top_bound = 300
bottom_bound = -300

def draw_dog_face() -> None:
    """
    Draws the main components of the dog face.
    """
    # Draw the head
    move_turtle(0, 80)
    draw_circle(80, "brown")

    # Draw the left ear
    move_turtle(-40, 140)
    draw_triangle(40, "brown")

    # Draw the right ear
    move_turtle(40, 140)
    draw_triangle(40, "brown")

    # Draw the left eye
    move_turtle(-20, 100)
    draw_circle(10, "white")
    move_turtle(-20, 100)
    draw_circle(4, "black")

    # Draw the right eye
    move_turtle(20, 100)
    draw_circle(10, "white")
    move_turtle(20, 100)
    draw_circle(4, "black")

    # Draw the nose
    move_turtle(0, 80)
    draw_triangle(20, "black")

    # Draw the mouth
    move_turtle(0, 60)
    draw_rectangle(30, 10, "black")

def draw_whiskers() -> None:
    """
    Draws the whiskers on both sides of the dog face.
    """
    # Set the pen color and width
    turtle.pencolor("black")
    turtle.pensize(2)

    # Draw the left whiskers
    move_turtle(-40, 70)
    turtle.right(20)
    turtle.forward(40)
    move_turtle(-40, 70)
    turtle.left(40)
    turtle.forward(40)
    move_turtle(-40, 70)
    turtle.right(20)
    turtle.forward(40)

    # Draw the right whiskers
    move_turtle(40, 70)
    turtle.left(20)
    turtle.forward(40)
    move_turtle(40, 70)
    turtle.right(40)
    turtle.forward(40)
    move_turtle(40, 70)
    turtle.left(20)
    turtle.forward(40)

    # Reset the turtle heading
    turtle.setheading(0)

def draw_background() -> None:
    """
    Draws the background of the canvas.
    """
    # Draw a blue sky background
    move_turtle(left_bound, top_bound)
    draw_rectangle(right_bound - left_bound, bottom_bound - top_bound, "sky blue")

def wink_animation() -> None:
    """
    Performs the winking animation of the left eye.
    """
    # Close the left eye
    move_turtle(-20, 100)
    draw_rectangle(10, 4, "brown")

    # Wait for 0.5 seconds
    time.sleep(0.5)

    # Open the left eye
    move_turtle(-20, 100)
    draw_rectangle(10, 4, "white")

    # Wait for 0.5 seconds
    time.sleep(0.5)

def draw_rain() -> None:
    """
    Simulates rain in the background.
    """
    turtle.penup()
    turtle.goto(left_bound, top_bound)  # Start at the top left corner of the window
    turtle.pendown()
    turtle.pensize(2)
    turtle.pencolor("blue")

    for _ in range(100):
        x = random.randint(left_bound, right_bound)  # Randomly choose x coordinate
        y = random.randint(bottom_bound, top_bound)  # Randomly choose y coordinate
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(10)

    turtle.penup()

def main() -> None:
    """
    Main function to draw the dog face with rain in the background.
    """
    # Draw the background
    draw_background()

    # Draw the dog face
    draw_dog_face()

    # Draw the whiskers
    draw_whiskers()

    # Perform the wink animation
    wink_animation()

    # Draw the rain
    draw_rain()

    # Save the image as a PostScript file
    canvas = turtle.getcanvas()
    canvas.postscript(file="dog_face.ps", colormode="color")

    turtle.done()

if __name__ == "__main__":
    main()
