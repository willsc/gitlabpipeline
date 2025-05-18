#!/usr/bin/env python3

"""
ASCII Mandelbrot Set Renderer

Displays a text-based visualization of the Mandelbrot set in the console.
"""

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return n
    return max_iter


def render(width=80, height=40,
           x_min=-2.0, x_max=1.0,
           y_min=-1.0, y_max=1.0,
           max_iter=100):
    # Gradient of characters from low to high density
    charset = " .:-=+*#%@"
    for y in range(height):
        row = ''
        cy = y_min + (y / (height - 1)) * (y_max - y_min)
        for x in range(width):
            cx = x_min + (x / (width - 1)) * (x_max - x_min)
            c = complex(cx, cy)
            m = mandelbrot(c, max_iter)
            # Choose character based on iteration count
            if m == max_iter:
                row += charset[-1]
            else:
                idx = int(m / max_iter * (len(charset) - 1))
                row += charset[idx]
        print(row)


def main():
    render()

if __name__ == '__main__':
    main()
