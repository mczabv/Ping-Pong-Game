from pygame import *
from random import randint

# Classes
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

# Ball Class
class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, 0)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > 500 - 50 or self.rect.y < 0:
            self.speed_y *= -1  

# Initialize Pygame
init()

# Window dimensions
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")

# Create rackets
paddle1 = Player("racket.png", 30, 200, 30, 150, 15) # Left racket
paddle2 = Player("racket.png", 640, 200, 30, 150, 15) # Right racket

# Create ball
ball = Ball("ball.png", 325, 225, 50, 50, 15, 15)

# Font initialization
font.init()
font1 = font.Font(None, 35)

# Create text labels for losing
lose1 = font1.render('PLAYER 2 WINS!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 1 WINS!', True, (180, 0, 0))
restart_text = font1.render('Press R to Restart', True, (255, 255, 255))

# State variable to track if the game is over
finish = False

# Define the light blue color using RGB values
LIGHT_BLUE = (173, 216, 230)

# Game Loop controls
game = True
clock = time.Clock()
FPS = 60

# --- MAIN GAME LOOP ---
while game:
    # Event handler
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_r and finish:
                # Reset game state
                finish = False
                # Reset positions
                ball.rect.x = 325
                ball.rect.y = 225
                paddle1.rect.y = 200
                paddle2.rect.y = 200
                
    # Fill the background with light blue every frame
    window.fill(LIGHT_BLUE)

    # 1. Always clear the screen with the background color first
    window.fill(LIGHT_BLUE)

    if not finish:
        # Move paddles and ball only if the game is still running
        paddle1.update_l()
        paddle2.update_r()
        ball.update()

        # Check racket collisions
        if sprite.collide_rect(paddle1, ball) or sprite.collide_rect(paddle2, ball):
            ball.speed_x *= -1

    # 2. Always draw current positions of elements (even when paused/finished)
    paddle1.reset()
    paddle2.reset()
    ball.reset()

    # 3. Check Win/Lose conditions and draw text ON TOP of the sprites
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (250, 200))
        window.blit(restart_text, (240, 250)) # Prints underneath the winner text

    if ball.rect.x > win_width - 50: 
        finish = True
        window.blit(lose2, (250, 200))
        window.blit(restart_text, (240, 250)) # Prints underneath the winner text

    # Refresh the screen
    display.update()
    clock.tick(FPS)

    # Always draw current positions of elements
    paddle1.reset()
    paddle2.reset()
    ball.reset()

    # Refresh the screen
    display.update()
    clock.tick(FPS)
