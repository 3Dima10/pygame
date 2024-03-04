import pygame

pygame.init()

clock = pygame.time.Clock()

scrin = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Call of Survival: Zombie Mayhem")
icon = pygame.image.load("image/call.png")
pygame.display.set_icon(icon)

fon = pygame.image.load("image/fon.jpg")
# plair = pygame.image.load("image/plair/srint1.png")

fon = pygame.transform.scale(fon, (800, 500))

plair_anim = 0
fon_x = 0

world = [
    pygame.image.load("image/plair/srint1.png"),
    pygame.image.load("image/plair/srint2.png"),
    pygame.image.load("image/plair/srint3.png"),
    pygame.image.load("image/plair/srint4.png"),
    pygame.image.load("image/plair/srint5.png"),
    pygame.image.load("image/plair/srint6.png"),
    pygame.image.load("image/plair/srint7.png"),
    pygame.image.load("image/plair/srint8.png"),
]

world_plair = [pygame.transform.scale(img, (40, 50)) for img in world]

fon_mp3 = pygame.mixer.Sound("sayns/Lx24_-_Devil_dance.mp3")
fon_mp3.play()
# plair = pygame.transform.scale(plair, (80, 100))

runing = True
while runing:

    scrin.blit(fon, (fon_x, 0))
    scrin.blit(fon, (fon_x + 800, 0))
    # scrin.blit(world[plair_anim], (40, 0))

    scrin.blit(world_plair[plair_anim], (40, 390))
    if plair_anim == 7:
        plair_anim = 0

    else:
        plair_anim += 1

    fon_x -= 2
    
    if fon_x == -800:
        fon_x = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
            pygame.quit()

    clock.tick(15)
    