import pygame
import math
import time
from paddle import Paddle
from ball import Ball

pygame.init()

#Colores
BLACK = (0,0,0)
WHITE = (255,255,255)

#Ventana
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#Paletas
paddleA = Paddle(WHITE, 20, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 20, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#Bola
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


carryOn = True

clock = pygame.time.Clock() 

#Puntaje
scoreA = 0
scoreB = 0

#Reseteo de Bola
def resetball():   
        ball.rect.x = 345
        ball.rect.y = 195 
        ballAngle = math.radians(0)
        ballSpeed = 10
        ballDirection = -1

#Reseteo de puntajes
def init():
    global scoreA, scoreB
    scoreA = 0
    scoreB = 0
    

#Reseteo de paletas
def resetpaddle():
    global paddleA, paddleB
    paddleB.rect.x = 670
    paddleB.rect.y = 200
    paddleA.rect.x = 20
    paddleA.rect.y = 200
    

#Victoria player 1
def win():
    scoreA, scoreB

    if scoreA==3:
        font = pygame.font.Font(None, 36)
        text3 = font.render("Jugador 1 Gana", 1, WHITE)
        screen.blit(text3, (260, 250))
        font = pygame.font.Font(None, 36)
        text3 = font.render("Pulsa R para jugar de nuevo", 1, WHITE)
        screen.blit(text3, (200, 270))	
    
    elif scoreB==3:
            font = pygame.font.Font(None, 36)
            text3 = font.render("Jugador 2 Gana", 1, WHITE)
            screen.blit(text3, (250, 250))
            font = pygame.font.Font(None, 36)
            text3 = font.render("Pulsa R para jugar de nuevo", 1, WHITE)
            screen.blit(text3, (200, 270))	

while carryOn: 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_x:
				carryOn = False
			if event.key==pygame.K_r:
                            init() and resetball() and resetpaddle()

            

	keys = pygame.key.get_pressed() 
	if keys[pygame.K_w]:
            paddleA.moveUp(10)
	if keys[pygame.K_s]:
            paddleA.moveDown(10)
	if keys[pygame.K_UP]:
            paddleB.moveUp(10)
	if keys[pygame.K_DOWN]:
            paddleB.moveDown(10)

 	       	
	all_sprites_list.update()

if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
    ball.bounce()
    effect = pygame.mixer.Sound("/home/linux/Escritorio/juego/Sounds/beep.wav")
    effect.play()

if ball.rect.x>=670: 
    scoreA+=1
    ball.velocity[0] = -ball.velocity[0]
if ball.rect.x<=20:
    scoreB+=1
    ball.velocity[0] = -ball.velocity[0]

if ball.rect.y>490:
    ball.velocity[1] = -ball.velocity[1]
if ball.rect.y<0:
    ball.velocity[1] = -ball.velocity[1]

if ball.rect.x>=670: 
    resetball()
if ball.rect.x<=20:
    resetball()
         

screen.fill(BLACK) 	
	
pygame.draw.line(screen, BLACK, [349, 0], [349, 500], 5)

all_sprites_list.draw(screen)

font = pygame.font.Font(None, 74)
text = font.render(str(scoreA), 1, WHITE)
screen.blit(text, (250,10))
text = font.render(str(scoreB), 1, WHITE)
screen.blit(text, (420,10))




clock.tick(60)
   
if scoreA==3:
    win()
    resetball()
    resetpaddle()
    time.sleep(1)



elif scoreB==3:
        win()
        resetball()
        resetpaddle()
        time.sleep(1)

pygame.display.flip()   

pygame.quit() 
