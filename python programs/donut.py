import turtle
from math import cos, sin
import colorsys

# Screen setup
WIDTH, HEIGHT = 800, 800
window = turtle.Screen()
window.setup(WIDTH, HEIGHT)
window.bgcolor("black")
window.title("3D Donut Animation")

# Donut parameters
R1 = 10
R2 = 20
K2 = 200
K1 = HEIGHT * K2 * 3 / (8 * (R1 + R2))

A, B = 0, 0  # Rotation angles

theta_spacing = 0.07
phi_spacing = 0.02

chars = ".,-~:;=!*#$@"  # Characters for shading

# Initialize turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

def hsv2rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return int(r * 255), int(g * 255), int(b * 255)

def draw_donut(A, B, hue):
    t.clear()  # Clear previous frame
    t.goto(-WIDTH//2, HEIGHT//2)  # Reset position

    zbuffer = [[0] * WIDTH for _ in range(HEIGHT)]
    output = [[' '] * WIDTH for _ in range(HEIGHT)]

    for theta in range(0, 628, int(theta_spacing * 100)):  # theta goes around the cross-sectional circle of a torus
        for phi in range(0, 628, int(phi_spacing * 100)):  # phi goes around the center of revolution of a torus

            cosA = cos(A)
            sinA = sin(A)
            cosB = cos(B)
            sinB = sin(B)

            costheta = cos(theta / 100)
            sintheta = sin(theta / 100)
            cosphi = cos(phi / 100)
            sinphi = sin(phi / 100)

            # x, y coordinates before revolving
            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            # 3D (x, y, z) coordinates after rotation
            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z  # one over z

            # x, y projection
            xp = int(WIDTH / 2 + K1 * ooz * x)
            yp = int(HEIGHT / 2 - K1 * ooz * y)

            # Ensure xp and yp are within the buffer range
            if 0 <= xp < WIDTH and 0 <= yp < HEIGHT:
                # luminance (L ranges from -sqrt(2) to sqrt(2))
                L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (
                    cosA * sintheta - costheta * sinA * sinphi)

                if ooz > zbuffer[yp][xp]:  # Check z-buffer for depth
                    zbuffer[yp][xp] = ooz
                    luminance_index = int(L * 8)  # Calculate luminance index
                    char = chars[max(luminance_index, 0)]  # Select character for shading
                    r, g, b = hsv2rgb(hue, 1, 1)
                    t.goto(xp - WIDTH // 2, HEIGHT // 2 - yp)  # Convert to turtle coordinates
                    t.dot(5, (r, g, b))  # Draw a dot for each point

# Main loop
hue = 0
def main():
    global A, B, hue
    while True:
        draw_donut(A, B, hue)
        A += 0.04  # Increment rotation angles
        B += 0.02
        hue += 0.01  # Cycle through hues
        window.update()  # Update turtle window

# Set up turtle screen to refresh automatically
window.tracer(0)
main()

# Close the window on click
window.mainloop()
