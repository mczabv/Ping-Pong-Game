from pygame import *

# Initialize Pygame
init()

# Window dimensions
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")

# Define the light blue color using RGB (Red, Green, Blue) values
LIGHT_BLUE = (173, 216, 230)

# Game Loop controls
game = True
clock = time.Clock()
FPS = 60

while game:
    # Event handler (allows us to close the window)
    for e in event.get():
        if e.type == QUIT:
            game = False

    # Fill the background with light blue
    window.fill(LIGHT_BLUE)

    # Refresh the screen
    display.update()
    clock.tick(FPS)