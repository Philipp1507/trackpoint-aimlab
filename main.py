import pygame as pg
import random

pg.init()

width, height = 800, 600
bg = (255, 255, 255)
circle_color = (255, 0, 50)

correct = pg.mixer.Sound("correct.mp3")
error = pg.mixer.Sound("error.mp3")

clock = pg.time.Clock()

font = pg.font.SysFont("FreeSans", 20)
text_color = (0, 0, 0)

screen = pg.display.set_mode((width, height))
pg.display.set_caption("Trackpoint Aimlab")

x = random.randint(20, width - 20)
y = random.randint(20, height - 20)

running = True
start_time = pg.time.get_ticks()
time_used = 0

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if abs(int(pos[0]) - x) <= 20:
                if abs(int(pos[1]) - y) <= 20:
                    pg.mixer.Sound.play(correct)

                    time_used = (pg.time.get_ticks() - start_time) / 1000
                    start_time = pg.time.get_ticks()

                    x = random.randint(20, width - 20)
                    y = random.randint(20, height - 20)
                    
                    continue
            pg.mixer.Sound.play(error)



    screen.fill(bg)
    pg.draw.circle(screen, circle_color, (x, y), 20)

    timer = font.render(str(time_used), True, text_color)
    screen.blit(timer, (20, 20))

    pg.display.flip()
    clock.tick(60)

pg.quit()
