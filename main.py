import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 700


# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 0.5

    def update(self):
        self.speed_y += self.gravity
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check for collisions with the edges of the screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speed_x = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speed_x = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speed_y = 0
        elif self.rect.top < 0:
            self.rect.top = 0
            self.speed_y = 0

    def jump(self):
        self.speed_y = -10

    def move_left(self):
        self.speed_x = -5

    def move_right(self):
        self.speed_x = 5


# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("2D Platformer")

# Create the player object
player = Player()

# Create the sprite group for the player
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Run the game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()

    # Update the player
    all_sprites.update()

    # Draw the screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
