import pygame


x = 500
y = 100
MAX_X = 800
MAX_Y = 600
game_over = False
bg_color = (0, 10, 0)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))  #((MAX_X, MAX_Y), pygame.FULLSCREEN )
pygame.display.set_caption("my first game")

# print (pygame.image.get_extended())

myimage = pygame.image.load("car.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                y += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                x += 20

        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

    screen.fill(bg_color)
    screen.blit(myimage, (x, y))
    pygame.display.flip()



