import pygame

pygame.init()


size = 500,500
tela = pygame.display.set_mode(size)

pygame.display.set_caption('Titulo')

teste = True
while teste:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            teste = False
    tela.fill("#009440")
    pygame.draw.rect(tela, 'yellow',[100, 177, 300,150], 0)
    pygame.draw.circle(tela, ('blue'),(250,250),(70))
    pygame.draw.rect(tela, 'white',[180, 235, 140, 25], 0)
    pygame.display.flip()
    

pygame.quit()
