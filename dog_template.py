import turtle
from typing import Tuple

def draw_circle(radius: float, color: str) -> None:
    """
    Draw a circle with the specified radius and color.

    Args:
    radius (float): The radius of the circle.
    color (str): The color of the circle.
    """
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_triangle(length: float, color: str) -> None:
    """
    Draw an equilateral triangle with the specified side length and color.

    Args:
    length (float): The side length of the triangle.
    color (str): The color of the triangle.
    """
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)
    turtle.end_fill()

def draw_rectangle(width: float, height: float, color: str) -> None:
    """
    Draw a rectangle with the specified width, height, and color.

    Args:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.
    color (str): The color of the rectangle.
    """
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def move_turtle(x: float, y: float) -> None:
    """
    Move the turtle to the specified (x, y) coordinates without drawing.

    Args:
    x (float): The x-coordinate to move the turtle to.
    y (float): The y-coordinate to move the turtle to.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
def draw_whiskers():
    # Set the pen color and width
    turtle.pencolor("black")
    turtle.pensize(1)

    # Draw the first whisker
    move_turtle(-35, -20)
    turtle.right(20)
    turtle.forward(30)

    # Draw the second whisker
    move_turtle(-35, -25)
    turtle.right(20)
    turtle.forward(30)

    # Draw the third whisker
    move_turtle(-35, -30)
    turtle.right(20)
    turtle.forward(30)

    # Reset the turtle heading
    turtle.setheading(0)