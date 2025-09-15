import pygame
from PIL import Image
import random

## init
pygame.init()
# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

stars = [[random.randrange(0, window_lebar), random.randrange(0, window_panjang)] for _ in range(100)]
asteroids = [[random.randrange(0, window_lebar), random.randrange(0, window_panjang)] for _ in range(6)]
earths = [[random.randrange(0, window_lebar), random.randrange(0, window_panjang)] for _ in range(2)]
marss = [[random.randrange(0, window_lebar), random.randrange(0, window_panjang)] for _ in range(1)]
saturnuss = [[random.randrange(0, window_lebar), random.randrange(0, window_panjang)] for _ in range(1)]
asteroidd = pygame.image.load("asteroid.png")
spaceship = pygame.image.load("spaceships.png")
earthd = pygame.image.load("earth.png")
marsd = pygame.image.load("mars.png")
saturnusd = pygame.image.load("saturnus.png")
exploxion = pygame.image.load("exploxion.png")

# atur ukuran agar sesuai
asteroidd = pygame.transform.scale(asteroidd, (23, 23))
spaceship = pygame.transform.scale(spaceship, (40, 40))
exploxion = pygame.transform.scale(exploxion, (80, 80))
earthd = pygame.transform.scale(earthd, (30, 30))
marsd = pygame.transform.scale(marsd, (30, 30))
saturnusd = pygame.transform.scale(saturnusd, (40, 40))

def update_stars():
    for star in stars:
        star[1] += 0.2
        if star[1] > window_panjang:  
            star[0] = random.randrange(0, window_lebar)
            star[1] = 0

def draw_stars():
    for star in stars:
        pygame.draw.circle(window, (255, 255, 255), star, 1)  

def update_asteroid():
    for asteroid in asteroids:
        asteroid[1] += 0.2
        if asteroid[1] > window_panjang:  
            asteroid[0] = random.randrange(0, window_lebar)
            asteroid[1] = 0

def draw_asteroid():
    for asteroid in asteroids:
        window.blit(asteroidd, (asteroid[0], asteroid[1]))

def update_earth():
    for earth in earths:
        earth[1] += 0.2
        if earth[1] > window_panjang:  
            earth[0] = random.randrange(0, window_lebar)
            earth[1] = 0

def draw_earth():
    for earth in earths:
        window.blit(earthd, (earth[0], earth[1]))

def update_mars():
    for mars in marss:
        mars[1] += 0.2
        if mars[1] > window_panjang:  
            mars[0] = random.randrange(0, window_lebar)
            mars[1] = 0

def draw_mars():
    for mars in marss:
        window.blit(marsd, (mars[0], mars[1]))

def update_saturnus():
    for saturnus in saturnuss:
        saturnus[1] += 0.2
        if saturnus[1] > window_panjang:  
            saturnus[0] = random.randrange(0, window_lebar)
            saturnus[1] = 0

def draw_saturnus():
    for saturnus in saturnuss:
        window.blit(saturnusd, (saturnus[0], saturnus[1]))
  
# variable running game
isRun = True
is_exploded = False
explosion_time = 0


# score
font_skor = pygame.font.Font(None, 30)
skor = 0

# posisi user
x = 250
y = 250

# ukuran
panjang = 40
lebar = 40


# kecepatan gerak
speed = 1

while isRun:

    pygame.time.delay(2)

    # user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
    
    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed

    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    # game dynamic

    # update asset
    window.fill((0,0,0))
    update_stars()
    draw_stars()
    update_asteroid()
    draw_asteroid()
    update_earth()
    draw_earth()
    update_mars()
    draw_mars()
    update_saturnus()
    draw_saturnus()

    # tampilkan score
    skor_text = font_skor.render(f"Score: {skor}", True, (255,255,255))
    window.blit(skor_text, (10,10))

    # buat rect
    player_rect = pygame.Rect(x, y, lebar, panjang)

    # gambar spaceship atau ledakan
    if is_exploded:
        window.blit(exploxion, (x - 20, y - 20))  # posisi disesuaikan
        if pygame.time.get_ticks() - explosion_time > 800:  # tampil 0.5 detik
            is_exploded = False
    else:
        window.blit(spaceship, (x, y))


    # rect untuk earth
    earth_rects = [pygame.Rect(earth[0], earth[1], 25, 25) for earth in earths]
    asteroid_rects = [pygame.Rect(ast[0], ast[1], 25, 25) for ast in asteroids]
    mars_rects = [pygame.Rect(m[0], m[1], 25, 25) for m in marss]
    saturnus_rects = [pygame.Rect(s[0], s[1], 31, 31) for s in saturnuss]



    # cek tabrakan
    for i, rect in enumerate(earth_rects):
        if player_rect.colliderect(rect):
            skor += 1
            # respawn earth yang disentuh
            earths[i][0] = random.randrange(window_lebar - 25)
            earths[i][1] = 0  

    for i, rect in enumerate(asteroid_rects):
        if player_rect.colliderect(rect):
            skor = 0
            is_exploded = True
            explosion_time = pygame.time.get_ticks()
            asteroids[i][0] = random.randrange(window_lebar - 25)
            asteroids[i][1] = 0  


    for i, rect in enumerate(mars_rects):
        if player_rect.colliderect(rect):
            skor = 0
            is_exploded = True
            explosion_time = pygame.time.get_ticks()
            marss[i][0] = random.randrange(window_lebar - 25)
            marss[i][1] = 0  


    for i, rect in enumerate(saturnus_rects):
        if player_rect.colliderect(rect):
            skor = 0
            is_exploded = True
            explosion_time = pygame.time.get_ticks()
            saturnuss[i][0] = random.randrange(window_lebar - 31)
            saturnuss[i][1] = 0  



    pygame.display.update()

pygame.quit()