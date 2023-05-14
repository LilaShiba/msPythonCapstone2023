# 🐶 Drawing a 2D Dog Face 🐶

This project provides a simple example of drawing a 2D dog face using Turtle graphics in Python. You will learn how to create and customize a dog face and add your own functions to the `dog_template.py` file.

# 📚 Understanding the Code 📚 

The project consists of two files:

1. `dog_template.py`: This file contains basic functions for drawing shapes and moving the turtle. You can use these functions to create more complex drawings.

2. `main.py`: This file contains a function called `draw_dog_face()` that uses the functions from `dog_template.py` to draw a simple 2D dog face. You can modify the parameters of these functions to create your own custom dog face.

# 🎯 Centering the Dog Face 🎯 

To center the dog face on the screen, follow these steps:

1. Open the `main.py` file.
2. Find the `draw_dog_face()` function.
3. Modify the `move_turtle()` function calls with the appropriate coordinates to center the face.

# 🐾 Drawing Whiskers 🐾 

To add whiskers to your dog face drawing, you can create a new function in the `dog_template.py` file. Here are some tips to help you get started:

1. Define a new function called `draw_whiskers()`. This function will draw the whiskers on the dog's face.

2. Inside the `draw_whiskers()` function, use the `move_turtle()` function to position the turtle at the starting point of the first whisker.

3. Set the turtle's pen color and width using `turtle.pencolor()` and `turtle.pensize()` functions. For example, you can use a black color and a smaller pen size to draw thin whiskers.

4. Use a combination of `turtle.forward()`, `turtle.left()`, and `turtle.right()` functions to draw each whisker.

5. Repeat steps 2-4 for the remaining whiskers.

6. Import the `draw_whiskers()` function in the `main.py` file.

7. Call the `draw_whiskers()` function within the `draw_dog_face()` function or create a new function to combine your drawings.

Here's a simple example of how you can create a `draw_whiskers()` function:

```python
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
```

# 🚀 Have Fun and Be Creative! 🚀
Now it's time for you to explore and have fun creating your own unique dog face designs! Remember, you can always add more functions to the dog_template.py file and create more complex drawings. Don't be afraid to experiment and let your creativity shine! 🌟


1. Animate the Dog: Use the turtle library to animate the dog face by adding movement or changing expressions. For example, you can make the dog blink its eyes or wag its tail.

2. Create a Full Dog Image: Expand the drawing to include the dog's body, legs, and tail. You can create additional functions in the dog_template.py file to draw these elements and modify the draw_dog_face() function to incorporate them.

3. Design Different Dog Breeds: Customize your dog face to resemble specific dog breeds. Research different dog breeds and modify the shapes, colors, and features of your dog face to reflect their characteristics.

4. Build a Dog Face Generator: Create a program that randomly generates different dog face designs. You can use functions with randomized parameters to generate variations in size, shape, and color of the dog's face components.

<br>

# 🌌 May the Force Be with You, Young Jedi! 🌌

Remember, the goal is to have fun and learn through trying. Feel free to explore these extensions or come up with your own creative ideas to make your dog face drawings even more exciting and unique!

## Contributing

Instructions for contributing to the project or guidelines for developers.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Contact information for the project maintainer or contributors.