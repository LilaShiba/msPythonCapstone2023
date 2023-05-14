from turtle import done
from dog_template import *

def draw_dog_face():
    # Draw the head
    move_turtle(-50, 0)
    draw_circle(50, "brown")

    # Draw the left ear
    move_turtle(-80, 50)
    draw_triangle(30, "brown")

    # Draw the right ear
    move_turtle(20, 50)
    draw_triangle(30, "brown")

    # Draw the left eye
    move_turtle(-60, 20)
    draw_circle(5, "white")
    move_turtle(-60, 20)
    draw_circle(2, "black")

    # Draw the right eye
    move_turtle(0, 20)
    draw_circle(5, "white")
    move_turtle(0, 20)
    draw_circle(2, "black")

    # Draw the nose
    move_turtle(-25, -10)
    draw_triangle(10, "black")

    # Draw the mouth
    move_turtle(-25, -20)
    draw_triangle(10, "black")
    
    move_turtle(-15, -20)
    draw_triangle(10, "black")
    
    move_turtle(-5, -20)
    draw_triangle(10, "black")

# Call the function to draw the dog face
draw_dog_face()

# Keep the turtle window open
done()
