import pygame
from random import randint
pygame.font.init()#iniciar objeto fonte
pygame.init()

x = 400
y = 100
pos_x =300
pos_y = 800
pos_y_a = 800
pos_y_c = 800
pos_y_d = 800
v = 30
v_outros = 10
timer = 0
tempo_segundos = 0

fundo = pygame.image.load('fundo.png')
carro = pygame.image.load('1.png')
carro02 = pygame.image.load('2.png')
carro03 = pygame.image.load('3.png')
carro04 = pygame.image.load('4.png')
carro05 = pygame.image.load('5.png')
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Jogo parte 1')

#time 
font = pygame.font.SysFont('arial', 30)
texto = font.render('Tempo: ', True, (255,255,255), (0,0,0)) #cor da fonte


#criando janela
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]: #seta pra cima
        #y -= v #decrementar
    #if comandos[pygame.K_DOWN]:
        #y += v
    

    if(pos_y <= -450): #loop
        pos_y = 1000
    pos_y -= v_outros
    
    if comandos[pygame.K_RIGHT] and x<= 575:
        x += v
    if comandos[pygame.K_LEFT] and x >= 140:
        x -= v

    if (pos_y <= -80):
        pos_y = randint(800,1200)
    if (pos_y_a <= -80):
        pos_y_a = randint(1400,1800)
    if (pos_y_c <= -80):
        pos_y_c = randint(2000,2200)
    if (pos_y_d <= -80):
        pos_y_d = randint(2800,3000)

    pos_y -= v_outros
    pos_y_a -= v_outros + 25
    pos_y_c -= v_outros + 8
    pos_y_d -= v_outros + 20

    if (timer<20):
        timer += 1
    else:
        tempo_segundos += 1
        texto = font.render('Tempo: '+str(tempo_segundos), True, (255,255,255), (0,0,0))
        timer = 0
    
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x ,y ))
    janela.blit(carro02,(pos_x ,pos_y))
    janela.blit(carro03,(pos_x -130,pos_y_a ))
    janela.blit(carro04,(pos_x +270,pos_y_c ))
    janela.blit(carro05,(pos_x +90 ,pos_y_d ))
    janela.blit(texto,(10,50))

    pygame.display.update()
pygame.quit()
