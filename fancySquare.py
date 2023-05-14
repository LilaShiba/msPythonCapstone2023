import turtle

# Set up the turtle canvas
canvas = turtle.Screen()
canvas.setup(width=800, height=600)
turtle.speed(0)  # Set the turtle speed to the fastest

def draw_shape(size, sides, color):
    """
    Draws a shape with the given size, number of sides, and color.
    """
    turtle.color(color)
    for _ in range(sides):
        turtle.forward(size)
        turtle.right(360 / sides)

def animate():
    """
    Animates the drawing by rotating and changing colors.
    """
    colors = ["red", "blue", "green", "orange", "purple"]
    size = 100
    sides = 4
    angle = 5

    for _ in range(72):
        draw_shape(size, sides, colors[_ % len(colors)])
        turtle.right(angle)

def main():
    """
    Main function to run the animation.
    """
    # Hide the turtle cursor
    turtle.hideturtle()

    # Animate the drawing
    animate()

    turtle.done()

if __name__ == "__main__":
    main()
