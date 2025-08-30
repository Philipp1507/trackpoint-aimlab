import pygame as pg
import random

pg.init()

WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Trackpoint Aimlab")


# Styling
BG_COLOR = (255, 255, 255)
CIRCLE_COLOR = (255, 0, 50)
TEXT_COLOR = (0, 0, 0)
FONT = pg.font.SysFont("FreeSans", 20)

# Sound/Image file init
correct_sound = pg.mixer.Sound("correct.mp3")
error_sound = pg.mixer.Sound("error.mp3")
settings_img = pg.image.load("settings.png")
settings_img = pg.transform.scale(settings_img, (40, 40))
settings_rect = settings_img.get_rect(topright=((WIDTH - 10), 10))

clock = pg.time.Clock()

# Initial Circle Placement
x = random.randint(20, WIDTH - 20)
y = random.randint(20, HEIGHT - 20)

running = True
start_time = pg.time.get_ticks()
time_used = 0



def open_settings():
    print("This is a placeholder")

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:

            pos = pg.mouse.get_pos()

            if settings_rect.collidepoint(pos):
                open_settings()
                continue

            if abs(int(pos[0]) - x) <= 20:
                if abs(int(pos[1]) - y) <= 20:
                    
                    pg.mixer.Sound.play(correct_sound)

                    time_used = (pg.time.get_ticks() - start_time) / 1000
                    start_time = pg.time.get_ticks()

                    x = random.randint(20, WIDTH - 20)
                    y = random.randint(20, HEIGHT - 20)
                    
                    continue
            pg.mixer.Sound.play(error_sound)



    screen.fill(BG_COLOR)
    pg.draw.circle(screen, CIRCLE_COLOR, (x, y), 20)

    timer = FONT.render(str(time_used), True, TEXT_COLOR)
    screen.blit(timer, (20, 20))

    screen.blit(settings_img, settings_rect)

    pg.display.flip()
    clock.tick(60)

pg.quit()
