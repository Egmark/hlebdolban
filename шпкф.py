import random
import pygame
import time
import mixer
l = 1
pygame.init()
did = "Desert Eagle | Директива"
scar = "SCAR-20 | Наемникs"
stattrackvoy1 = "StatTrak™ M4A4 | Вой"
dlor = "AWP | История о драконе"
neonrevolution = "AK-47 | Неоновая революция"
buzzkill = "USP-S | Подтвержденное убийство"
sound = pygame.mixer.Sound("Electroman.wav")
sound.set_volume(1)
# screen = pygame.display.set_mode((800, 600))
menu = pygame.image.load("pop.png")
menu = pygame.transform.scale(menu, (800, 600))
loading = pygame.image.load("thumb-1920-895715.png")
loading = pygame.transform.scale(loading, (800, 600))
fon = pygame.image.load("14160044614l.jpg")
fon = pygame.transform.scale(fon, (800, 600))
chfon = pygame.image.load("1614281824_11-p-chernii-fon-kartinka-bez-risunka-13.jpg")
chfon = pygame.transform.scale(chfon, (400, 600))
chfon2 = pygame.image.load("1614281824_11-p-chernii-fon-kartinka-bez-risunka-13.jpg")
chfon2 = pygame.transform.scale(chfon2, (800, 600))
case = pygame.image.load("img-YyGw2L5PVlcBNJRQ-w1370.png")
case = pygame.transform.scale(case, (300, 300))
open = pygame.image.load("ккк.jpg")
open = pygame.transform.scale(open, (150, 30))
screen = pygame.display.set_mode((800, 600))

# dragonlore = pygame.image.load("image2.png")
# dragonlore = pygame.transform.scale(dragonlore, (100, 50))
# stena = pygame.image.load("1593698890_6-p-kirpichnii-fon-11.jpg")
# stena = pygame.transform.scale(stena, (800, 600))
# directiva = pygame.image.load("s802.png")
# directiva = pygame.transform.scale(directiva, (100, 50))
# voy = pygame.image.load("image4.png")
# voy = pygame.transform.scale(voy, (100, 50))
# neonr = pygame.image.load("s799.png")
# neonr = pygame.transform.scale(neonr, (100, 50))
# kill = pygame.image.load("image6.png")
# kill = pygame.transform.scale(kill, (100, 50))
# vopr = pygame.image.load("kartinki-znak-voprosa-4.jpg")
# vopr = pygame.transform.scale(vopr, (600, 400))
# digl=pygame.image.load("дигл.png")
# digl=pygame.transform.scale(digl,(100,50))
# gun_list = [dragonlore,voy,directiva,neonr,kill,digl]
# t=dragonlore
# t2=random.choice(gun_list)
# t1=random.choice(gun_list)
# x=0
# t3=random.choice(gun_list)
otkrit_snova=pygame.image.load("Открыть снова.png")
otkrit_snova = pygame.transform.scale(otkrit_snova, (315, 64))
dragonlore2 = pygame.image.load("image2.png")
dragonlore = pygame.transform.scale(dragonlore2, (100, 52))
dragonlore2 = pygame.transform.scale(dragonlore2, (800, 400))
stena = pygame.image.load("1593698890_6-p-kirpichnii-fon-11.jpg")
stena = pygame.transform.scale(stena, (800, 600))
directiva2 = pygame.image.load("s802.png")
directiva = pygame.transform.scale(directiva2, (100, 51))
directiva2 = pygame.transform.scale(directiva2, (600, 400))
voy2 = pygame.image.load("image4.png")
voy = pygame.transform.scale(voy2, (103, 50))
voy2 = pygame.transform.scale(voy2, (800, 400))
neonr2 = pygame.image.load("s799.png")
neonr = pygame.transform.scale(neonr2, (101, 50))
neonr2 = pygame.transform.scale(neonr2, (800, 400))
kill2 = pygame.image.load("image6.png")
kill = pygame.transform.scale(kill2, (100, 50))
kill2 = pygame.transform.scale(kill2, (600, 400))
vopr = pygame.image.load("kartinki-znak-voprosa-4.jpg")
vopr = pygame.transform.scale(vopr, (600, 400))
digl2 = pygame.image.load("дигл.png")
digl = pygame.transform.scale(digl2, (102, 50))
digl2 = pygame.transform.scale(digl2, (600, 400))
gun_list = [dragonlore ,voy, directiva, neonr, kill, digl]
t = dragonlore
t2 = random.choice(gun_list)
t1 = random.choice(gun_list)
t3 = random.choice(gun_list)

random_gun = [dragonlore for _ in range(3)]
random_gun += [voy for _ in range(7)]
random_gun += [directiva for _ in range(32)]
random_gun += [kill for _ in range(25)]
random_gun += [neonr for _ in range(10)]
random_gun += [digl for _ in range(25)]
random.shuffle(random_gun)
# choise = [directiva,dragonlore]
# drop = random.choice(choise)
pygame.init()
screen.blit(menu, (0, 0))
x1 = 255
x2 = 488
y1 = 513
y2 = 547
x3 = 319
x4 = 469
y3 = 499
y4 = 528
# screen2 =pygame.display.set_mode((800,600))
pygame.display.flip()
if random_gun[18] == dragonlore:
    dropl = dragonlore2
if random_gun[18] == directiva:
    dropl = directiva2
if random_gun[18] == kill:
    dropl = kill2
if random_gun[18] == voy:
    dropl = voy2
if random_gun[18] == neonr:
    dropl = neonr2
if random_gun[18] == digl:
    dropl = digl2
def crutilka(x):
    sec = 0

    sec += 1
    pygame.draw.polygon(screen, (255, 25, 0), ((100, 0), (800 // 2, 0), (150, 300)))
    for i in range(18):
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i, 300, 100, 50))
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i + 150, 300, 100, 50))
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i + 300, 300, 100, 50))
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i + 450, 300, 100, 50))
        pygame.draw.rect(screen, (200, 200, 200), (x + 600 * i + 600, 300, 100, 50))
        screen.blit(random_gun[i], (x + 600 * i, 300, 100, 50))
        screen.blit(random_gun[i + 1], (x + 600 * i + 150, 300, 100, 50))
        screen.blit(random_gun[i+2], (x + 600 * i + 300, 300, 100, 50))
        screen.blit(random_gun[i + 3], (x + 600 * i + 450, 300, 100, 50))
        screen.blit(random_gun[i + 4], (x + 600 * i + 600, 300, 100, 50))





    pygame.display.flip()
    return sec


def start():
    fon = pygame.image.load("14160044614l.jpg")
    fon = pygame.transform.scale(fon, (800, 600))
    screen.blit(fon, (0, 0))
    screen.blit(open, (320, 500))
    pygame.display.flip()


x = 0
crut = False
sec = 0
menu1 = True
again = False
while True:
    sound.play()
    pos = pygame.mouse.get_pos()

    # screen.blit(stena, (0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if 0 < pos[0] < 315 and 500 < pos[1] < 564 and again:
                print('egor tuk')
                x=0
                random_gun = [dragonlore for _ in range(3)]
                random_gun += [voy for _ in range(7)]
                random_gun += [directiva for _ in range(32)]
                random_gun += [kill for _ in range(25)]
                random_gun += [neonr for _ in range(10)]
                random_gun += [digl for _ in range(25)]
                random.shuffle(random_gun)

                if random_gun[18] == dragonlore:
                    dropl = dragonlore2
                if random_gun[18] == directiva:
                    dropl = directiva2
                if random_gun[18] == kill:
                    dropl = kill2
                if random_gun[18] == voy:
                    dropl = voy2
                if random_gun[18] == neonr:
                    dropl = neonr2
                if random_gun[18] == digl:
                    dropl = digl2




                crut = True

                menu1 = False
                screen.blit(chfon2, (0, 0))
                screen.blit(dropl, (50, 100))
                screen.blit(otkrit_snova, (0, 500))


                pygame.display.flip()
            if x3 < pos[0] < x4 and y3 < pos[1] < y4 and menu1:
                x1 = 0
                x2 = 0
                y1 = 0
                y2 = 0
                menu1 = False
                screen.blit(loading, (0, 0))
                pygame.display.flip()
                pygame.time.delay(3000)
                screen.blit(fon, (0, 0))
                screen.blit(chfon, (200, 0))
                screen.blit(case, (250, 230))
                screen.blit(open, (320, 500))
                pygame.display.flip()


            elif x3 < pos[0] < x4 and y3 < pos[1] < y4 and not menu1:

                crut = True

                menu1 = False

                pygame.display.flip()
            elif x3 < pos[0] < x4 and y3 < pos[1] < y4 and not menu1:

                crut = True

                menu1 = False

                pygame.display.flip()

    if crut:
        sec += l
        x -= 10

        screen.blit(chfon2, (0, 0))
        crutilka(x)

        if sec > 980:
            time.sleep(2)
            crut = False
            sec = 0
            x = 0
            #dropl = pygame.transform.scale(random_gun[18], (500, 300))
            screen.blit(chfon2, (0, 0))
            screen.blit(dropl, (50, 100))
            pygame.display.flip()
            time.sleep(0.1)
            screen.blit(otkrit_snova,(0,500))
            again = True

        #     x=0
        #     random_gun = [dragonlore for _ in range(3)]
        #     random_gun += [voy for _ in range(7)]
        #     random_gun += [directiva for _ in range(32)]
        #     random_gun += [kill for _ in range(25)]
        #     random_gun += [neonr for _ in range(10)]
        #     random_gun += [digl for _ in range(25)]
        #     random.shuffle(random_gun)
        #
        #     crut = True
        #
        #     menu1 = False
        #
        #     pygame.display.flip()

    pygame.time.delay(int(round(sec * 0.0)))
    pygame.display.flip()
