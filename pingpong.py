from pygame import *
#Classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # Update method for the LEFT paddle (uses W and S keys)
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 150: # 500 is win_height, 150 is paddle height
            self.rect.y += self.speed

    # Update method for the RIGHT paddle (uses Arrow keys)
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 150:
            self.rect.y += self.speed
#create rackets
paddle1 = Player("racket.png", 30, 200, 30, 150, 8) #left racket
paddle2 = Player("racket.png", 640, 200, 30, 150, 8) #right racket

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

    # Move the paddles based on keyboard input
    paddle1.update_l()
    paddle2.update_r()

    # Draw the paddles on the screen
    paddle1.reset()
    paddle2.reset()

    # Refresh the screen
    display.update()
    clock.tick(FPS)
