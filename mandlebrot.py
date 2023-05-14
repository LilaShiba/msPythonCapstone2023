import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot(c: complex, max_iterations: int = 100) -> int:
    """
    Calculates the number of iterations for a given complex number `c`
    to escape the Mandelbrot set.

    Args:
        c (complex): Complex number.
        max_iterations (int, optional): Maximum number of iterations. Defaults to 100.

    Returns:
        int: Number of iterations.
    """
    z = 0
    for i in range(max_iterations):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iterations

def animate_mandelbrot(zoom_factor: float = 1.0, frames: int = 100, interval: int = 50):
    """
    Animates the Mandelbrot set using matplotlib.

    Args:
        zoom_factor (float, optional): Zoom factor. Defaults to 1.0.
        frames (int, optional): Number of frames in the animation. Defaults to 100.
        interval (int, optional): Delay between frames in milliseconds. Defaults to 50.
    """
    fig = plt.figure(figsize=(8, 6))
    ax = plt.axes(xlim=(-2.0, 1), ylim=(-1.5, 1.5))
    ax.set_aspect('equal')
    ax.axis('off')

    iterations = 50
    cmap = plt.cm.jet

    x = np.linspace(-2.0 / zoom_factor, 1 / zoom_factor, 400)
    y = np.linspace(-1.5 / zoom_factor, 1.5 / zoom_factor, 300)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    M = np.zeros_like(Z, dtype=int)
    for i in range(len(y)):
        for j in range(len(x)):
            c = Z[i, j]
            M[i, j] = mandelbrot(c, iterations)

    img = ax.imshow(M.T, cmap=cmap, extent=(-2.0 / zoom_factor, 1 / zoom_factor, -1.5 / zoom_factor, 1.5 / zoom_factor))

    def animate(i):
        img.set_array((M + i * 0.1).T)

    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=interval, repeat=False)
    plt.show()

if __name__ == "__main__":
    try:
        animate_mandelbrot(zoom_factor=1.0, frames=100, interval=50)
    except Exception as e:
        print(f"An error occurred: {e}")
