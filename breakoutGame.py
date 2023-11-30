#setup code
import pygame
import random
pygame.init()
pygame.font.init
screen = pygame.display.set_mode((2560,1600))
vel = 10
# remember these width and height values, we will use them for bouncing the ball on the platform. if its on the first half, the ball moves left, else, the ball moves right.
width = 150
height = 10
x = 75
y = 750
ballX = 50
ballY = 700
speed = 3
xspeed = 3

run = True
   
# Creates Brick Array at beginning, this Array can be appended and removed from. Bricks are 80X25.
blockArray = []
blockXBorder = 5
blockYBorder = 5
blockLength = 80
blockHeight = 25
   
while run:
 
    # Black Background
    screen.fill((0, 0, 0))


    for yBorder in range(5):
        for xBorder in range(17):
            blockArray.append(pygame.draw.rect(screen, (0, 0, 0), (blockXBorder, blockYBorder, blockLength, blockHeight)))
            blockXBorder += 85
        blockXBorder = 5
        blockYBorder += 90

    for brick in blockArray[0:102]:
        pygame.draw.rect(screen, (0, 255, 0), brick)
    # creates time delay of 10ms  
    pygame.time.delay(10) 
    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:  
            run = False
    #CODE GOES HERE:

    ballCollisionX = ballX-10
    ballCollisionY = ballY-10


    # Draws Ball
    def generateBall(CircleX,CircleY):
        pygame.draw.circle(screen, (0, 0, 255), (ballX, ballY), 25)
    generateBall(ballX, ballY)
    ballCollision = pygame.draw.rect(screen, (0, 0, 255), (ballCollisionX, ballCollisionY, 25, 25))
     
    for brick in blockArray:
        if pygame.Rect.colliderect(ballCollision, brick) == True:
            ballY += (speed * -1)
            speed *= -1
            ballY += speed
            blockArray.remove(brick)

    # Draws Platform
    platform = pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    
    # Collision Detection + Gravity + Ball Speed
    
    brickCollision = pygame.Rect.collidelist(ballCollision, blockArray)

    if ballY < 0:
        ballY += (speed * -1)
        speed *= -1
        ballY += speed
    else:
        ballY += speed 
        ballX += xspeed

    if pygame.Rect.colliderect(ballCollision, platform) == True:
        ballY += (speed * -1)
        speed *= -1
        ballY += speed
    # Controls Platform

    if ballX > 1250 or ballX < 0:
        ballX += (xspeed * -1)
        xspeed *= -1
        ballX += xspeed        
        
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x>0:
        x -= vel 
    if keys[pygame.K_RIGHT] and x<1125: 
        x += vel    
	
    # Refreshes Window 
    pygame.display.update()


#now, we must code physics, a score counter, and an intro screen with difficulty/speed setting. also, keep ball still for a few seconds for player to adjust.
