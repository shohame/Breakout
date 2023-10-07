import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 15
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 30
BLOCK_ROWS = 5
BLOCK_COLS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-1, 1])
        self.dy = -1
        self.speed = 5

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def bounce(self, axis):
        if axis == 'x':
            self.dx *= -1
        elif axis == 'y':
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_RADIUS)

    def hit_wall(self):
        return self.x - BALL_RADIUS <= 0 or self.x + BALL_RADIUS >= SCREEN_WIDTH

    def hit_ceiling(self):
        return self.y - BALL_RADIUS <= 0

    def hit_floor(self):
        return self.y + BALL_RADIUS >= SCREEN_HEIGHT

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.direction = 0

    def move(self):
        self.x += self.direction * self.speed
        self.x = max(0, min(SCREEN_WIDTH - PADDLE_WIDTH, self.x))

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice([RED, GREEN, BLUE])
        self.alive = True

    def draw(self):
        if self.alive:
            pygame.draw.rect(screen, self.color, (self.x, self.y, BLOCK_WIDTH, BLOCK_HEIGHT))

def check_collision(ball, paddle, blocks):
    # Check collision with paddle
    if (paddle.x <= ball.x <= paddle.x + PADDLE_WIDTH) and (paddle.y <= ball.y + BALL_RADIUS <= paddle.y + PADDLE_HEIGHT):
        ball.bounce('y')
        
    # Check collision with blocks
    for block in blocks:
        if (block.alive and (block.x <= ball.x <= block.x + BLOCK_WIDTH) and
                (block.y <= ball.y - BALL_RADIUS <= block.y + BLOCK_HEIGHT or
                 block.y <= ball.y + BALL_RADIUS <= block.y + BLOCK_HEIGHT)):
            ball.bounce('y')
            break

blocks = [Block(x * BLOCK_WIDTH, y * BLOCK_HEIGHT) for y in range(BLOCK_ROWS) for x in range(BLOCK_COLS)]
paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.direction = -1
            if event.key == pygame.K_RIGHT:
                paddle.direction = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle.direction = 0

    ball.move()
    paddle.move()

    if ball.hit_wall():
        ball.bounce('x')

    if ball.hit_ceiling():
        ball.bounce('y')

    if ball.hit_floor():
        ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    check_collision(ball, paddle, blocks)

    ball.draw()
    paddle.draw()
    for block in blocks:
        block.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
