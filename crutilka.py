import random
import time
o=0
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
dragonlore = pygame.image.load("image2.png")
dragonlore = pygame.transform.scale(dragonlore, (100, 50))
stena = pygame.image.load("1593698890_6-p-kirpichnii-fon-11.jpg")
stena = pygame.transform.scale(stena, (800, 600))
directiva = pygame.image.load("s802.png")
directiva = pygame.transform.scale(directiva, (100, 50))
voy = pygame.image.load("image4.png")
voy = pygame.transform.scale(voy, (100, 50))
neonr = pygame.image.load("s799.png")
neonr = pygame.transform.scale(neonr, (100, 50))
kill = pygame.image.load("image6.png")
kill = pygame.transform.scale(kill, (600, 400))
vopr = pygame.image.load("kartinki-znak-voprosa-4.jpg")
vopr = pygame.transform.scale(vopr, (600, 400))

gun_list = [voy,directiva,neonr]
t=dragonlore
t2=random.choice(gun_list)
t1=random.choice(gun_list)
t3=random.choice(gun_list)
if t==dragonlore:
    o=1
if t2==dragonlore and o==1:
    t2=neonr
if t3==directiva:
    t3==voy
if  t3==neonr:
    t3=directiva


def crutilka(x):
    for i in range(100):
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i, 300, 100, 50))
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i + 150, 300, 100, 50))
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i + 300, 300, 100, 50))
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i + 450, 300, 100, 50))
        screen.blit(t3,(x + 600 * i, 300, 100, 50))
        screen.blit(t,(x + 600 * i + 150, 300, 100, 50))
        screen.blit(t1,(x + 600 * i + 300, 300, 100, 50))
        screen.blit(t2,(x + 600 * i + 450, 300, 100, 50))




x = 0
sec = 1


def timing():
    ls = [i for i in range(100, 0)]


while True:

    screen.fill((0, 0, 0))
    x -= 10
    sec += 1

    pygame.draw.polygon(screen, (255, 25, 0), ((100, 0), (800//2, 0), (150, 300)))
    crutilka(x)
    print(sec)
    if sec > 980:
        time.sleep(5)
        break
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit(0)
    pygame.time.delay(int(round(sec * 0.02)))
    pygame.display.flip()
