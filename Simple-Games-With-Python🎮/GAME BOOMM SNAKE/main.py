import pygame
import random

## init
pygame.init()
# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

stars = [[random.randrange(0, window_lebar), random.randrange(0, window_panjang)] for _ in range(100)]

def update_stars():
    for star in stars:
        star[1] += 0.2
        if star[1] > window_panjang:  
            star[0] = random.randrange(0, window_lebar)
            star[1] = 0

def draw_stars():
    for star in stars:
        pygame.draw.circle(window, (255, 255, 255), star, 1)  
# variable running game
isRun = True


# score
font_skor = pygame.font.Font(None, 30)
skor = 0

# posisi user
x = 250
y = 250

# posisi poin
z = random.randrange(250)
k = random.randrange(250)

# posisi bom
a1 = random.randrange(250)
a2 = random.randrange(250)
a3 = random.randrange(250)
a4 = random.randrange(250)
a5 = random.randrange(250)
a6 = random.randrange(250)
b1 = random.randrange(250)
b2 = random.randrange(250)
b3 = random.randrange(250)
b4 = random.randrange(250)
b5 = random.randrange(250)
b6 = random.randrange(250)

# ukuran
panjang = 20
lebar = 20



# kecepatan gerak
speed = 1

while isRun:



    def terlalu_dekat(x1, y1, x2, y2, min_dist=40):
        return abs(x1 - x2) < min_dist and abs(y1 - y2) < min_dist

    def spawn_aman(existing, min_dist=40):
        while True:
            rx = random.randrange(window_lebar - lebar)
            ry = random.randrange(window_panjang - panjang)
            if all(not terlalu_dekat(rx, ry, ex, ey, min_dist) for ex, ey in existing):
                return rx, ry

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

    # tampilkan score
    skor_text = font_skor.render(f"Score: {skor}", True, (255,255,255))
    window.blit(skor_text, (10,10))

    # buat rect
    player_rect = pygame.Rect(x, y, lebar, panjang)
    target_rect = pygame.Rect(z, k, lebar, panjang)
    bom_rect1 = pygame.Rect(a1, b1, lebar, panjang)
    bom_rect2 = pygame.Rect(a2, b2, lebar, panjang)
    bom_rect3 = pygame.Rect(a3, b3, lebar, panjang)
    bom_rect4 = pygame.Rect(a4, b4, lebar, panjang)
    bom_rect5 = pygame.Rect(a5, b5, lebar, panjang)
    bom_rect6 = pygame.Rect(a6, b6, lebar, panjang)


    # gambar
    pygame.draw.rect(window, (255,255,255), player_rect)
    pygame.draw.rect(window, (0,255,0), target_rect)
    pygame.draw.rect(window, (255,0,0), bom_rect1)
    pygame.draw.rect(window, (255,0,0), bom_rect2)
    pygame.draw.rect(window, (255,0,0), bom_rect3)
    pygame.draw.rect(window, (255,0,0), bom_rect4)
    pygame.draw.rect(window, (255,0,0), bom_rect5)
    pygame.draw.rect(window, (255,0,0), bom_rect6)

    if player_rect.colliderect(target_rect):
        # spawn poin hijau dulu
        z, k = spawn_aman([], min_dist=50)

        # spawn bom dengan jarak aman
        existing = [(z, k)]
        a1, b1 = spawn_aman(existing, min_dist=50); existing.append((a1, b1))
        a2, b2 = spawn_aman(existing, min_dist=50); existing.append((a2, b2))
        a3, b3 = spawn_aman(existing, min_dist=50); existing.append((a3, b3))
        a4, b4 = spawn_aman(existing, min_dist=50); existing.append((a4, b4))
        a5, b5 = spawn_aman(existing, min_dist=50); existing.append((a5, b5))
        a6, b6 = spawn_aman(existing, min_dist=50); existing.append((a6, b6))

        skor += 1

    
    if player_rect.colliderect(bom_rect1):
        # spawn poin hijau dulu
        z, k = spawn_aman([], min_dist=50)

        # spawn bom dengan jarak aman
        existing = [(z, k)]
        a1, b1 = spawn_aman(existing, min_dist=50); existing.append((a1, b1))
        a2, b2 = spawn_aman(existing, min_dist=50); existing.append((a2, b2))
        a3, b3 = spawn_aman(existing, min_dist=50); existing.append((a3, b3))
        a4, b4 = spawn_aman(existing, min_dist=50); existing.append((a4, b4))
        a5, b5 = spawn_aman(existing, min_dist=50); existing.append((a5, b5))
        a6, b6 = spawn_aman(existing, min_dist=50); existing.append((a6, b6))

        skor = 0

        
    elif player_rect.colliderect(bom_rect2):
        # spawn poin hijau dulu
        z, k = spawn_aman([], min_dist=50)

        # spawn bom dengan jarak aman
        existing = [(z, k)]
        a1, b1 = spawn_aman(existing, min_dist=50); existing.append((a1, b1))
        a2, b2 = spawn_aman(existing, min_dist=50); existing.append((a2, b2))
        a3, b3 = spawn_aman(existing, min_dist=50); existing.append((a3, b3))
        a4, b4 = spawn_aman(existing, min_dist=50); existing.append((a4, b4))
        a5, b5 = spawn_aman(existing, min_dist=50); existing.append((a5, b5))
        a6, b6 = spawn_aman(existing, min_dist=50); existing.append((a6, b6))

        skor = 0

    elif player_rect.colliderect(bom_rect3):
        # spawn poin hijau dulu
        z, k = spawn_aman([], min_dist=50)

        # spawn bom dengan jarak aman
        existing = [(z, k)]
        a1, b1 = spawn_aman(existing, min_dist=50); existing.append((a1, b1))
        a2, b2 = spawn_aman(existing, min_dist=50); existing.append((a2, b2))
        a3, b3 = spawn_aman(existing, min_dist=50); existing.append((a3, b3))
        a4, b4 = spawn_aman(existing, min_dist=50); existing.append((a4, b4))
        a5, b5 = spawn_aman(existing, min_dist=50); existing.append((a5, b5))
        a6, b6 = spawn_aman(existing, min_dist=50); existing.append((a6, b6))

        skor = 0
    
    elif player_rect.colliderect(bom_rect4):
        # spawn poin hijau dulu
        z, k = spawn_aman([], min_dist=50)

        # spawn bom dengan jarak aman
        existing = [(z, k)]
        a1, b1 = spawn_aman(existing, min_dist=50); existing.append((a1, b1))
        a2, b2 = spawn_aman(existing, min_dist=50); existing.append((a2, b2))
        a3, b3 = spawn_aman(existing, min_dist=50); existing.append((a3, b3))
        a4, b4 = spawn_aman(existing, min_dist=50); existing.append((a4, b4))
        a5, b5 = spawn_aman(existing, min_dist=50); existing.append((a5, b5))
        a6, b6 = spawn_aman(existing, min_dist=50); existing.append((a6, b6))

        skor = 0

    elif player_rect.colliderect(bom_rect5):
        # spawn poin hijau dulu
        z, k = spawn_aman([], min_dist=50)

        # spawn bom dengan jarak aman
        existing = [(z, k)]
        a1, b1 = spawn_aman(existing, min_dist=50); existing.append((a1, b1))
        a2, b2 = spawn_aman(existing, min_dist=50); existing.append((a2, b2))
        a3, b3 = spawn_aman(existing, min_dist=50); existing.append((a3, b3))
        a4, b4 = spawn_aman(existing, min_dist=50); existing.append((a4, b4))
        a5, b5 = spawn_aman(existing, min_dist=50); existing.append((a5, b5))
        a6, b6 = spawn_aman(existing, min_dist=50); existing.append((a6, b6))

        skor = 0

    elif player_rect.colliderect(bom_rect6):
        # spawn poin hijau dulu
        z, k = spawn_aman([], min_dist=50)

        # spawn bom dengan jarak aman
        existing = [(z, k)]
        a1, b1 = spawn_aman(existing, min_dist=50); existing.append((a1, b1))
        a2, b2 = spawn_aman(existing, min_dist=50); existing.append((a2, b2))
        a3, b3 = spawn_aman(existing, min_dist=50); existing.append((a3, b3))
        a4, b4 = spawn_aman(existing, min_dist=50); existing.append((a4, b4))
        a5, b5 = spawn_aman(existing, min_dist=50); existing.append((a5, b5))
        a6, b6 = spawn_aman(existing, min_dist=50); existing.append((a6, b6))

        skor = 0

    pygame.display.update()

pygame.quit()