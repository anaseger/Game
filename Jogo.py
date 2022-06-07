import pygame
pygame.init()
x = 400
y = 300
pos_x =300
pos_y = 300
v = 25
v_outros = 15
fundo = pygame.image.load('fundo.png')
carro = pygame.image.load('1.png')
carro02 = pygame.image.load('2.png')
carro03 = pygame.image.load('3.png')
carro04 = pygame.image.load('4.png')
carro05 = pygame.image.load('5.1.png')
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jogo parte 1')
#criando janela
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]: #seta pra cima
        y -= v #decrementar
    if comandos[pygame.K_DOWN]:
        y += v
    if comandos[pygame.K_LEFT]:
        x -= v
    if comandos[pygame.K_RIGHT]:
        x += v
    if(pos_y <= -200): #loop
        pos_y = 900
    pos_y -= v_outros
    
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x  -93,y ))
    janela.blit(carro02,(pos_x ,pos_y))
    janela.blit(carro03,(pos_x -130,pos_y -300))
    janela.blit(carro04,(pos_x +270,pos_y -30))
    janela.blit(carro05,(pos_x +90 ,pos_y +330))

    pygame.display.update()
pygame.quit()
