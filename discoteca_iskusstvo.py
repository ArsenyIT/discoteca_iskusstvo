from all_colors import *
import random
import pygame
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load('resours/Комарово.mp3')
pygame.mixer.music.play(-1)

size = (0, 0)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("50 Random Circle")
Background = (255, 255, 255)
screen.fill(Background)
colors = [Black, White, DarkSlateGrey, SlateGrey, Red, Green, Blue, Orange, Yellow, Navy, Grey, GreenYellow,
          Brown, RosyBrown, SandyBrown, SaddleBrown, Lime, LimeGreen, Tan, Peru, Cyan, LightCyan, DarkCyan,
          Salmon, DarkSalmon, LightSalmon, Linen, Silver, DimGrey,LightGrey, DarkGrey, Ivory, Beige, Azure,
          Snow, Aqua, Teal, Olive, SeaGreen, Sienna, Chocolate, Maroon, Wheat, Purple, Indigo, Violet, Plum,
          Magenta, Pink, Gold, Coral, Tomato, Khaki, LightSlateGrey, Gainsboro, MistyRose, LavenderBlush]
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color = random.choice(colors)
    screen.fill(color)
    for _ in range(50):
        x = random.randint(0, 1280)
        y = random.randint(0, 1000)
        radius = random.randint(10, 100)
        color = random.choice(colors)
        pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))

pygame.quit()