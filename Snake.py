import pygame
import random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sanke")
running = True

WIDTH, HEIGHT = 600, 400
Border = pygame.Rect(0, 0, WIDTH, HEIGHT)
Clock = pygame.time.Clock()
x = 300
y = 200
Base_speed = 1
Segments = [(300,200)]
Direction = (1,0)
Barrier = pygame.Rect(0,0,600,400)

Move_delay = 150 #ms
Last_move_time = pygame.time.get_ticks()

food = (random.randint(0,29) * 20, random.randint(0,19) * 20)
Game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if Game_over:
                if event.key == pygame.K_F5:
                    Segments.clear()
                    Segments = [(300,200)]
                    Direction = (1,0)
                    food = (random.randint(0,29) * 20, random.randint(0,19) * 20)
                    Last_move_time = pygame.time.get_ticks()
                    Game_over = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

    if not Game_over:
        new_direction = Direction       

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            new_direction = (-1, 0)
        if keys[pygame.K_d]:
            new_direction = (1, 0)
        if keys[pygame.K_w]:
            new_direction = (0, -1)
        if keys[pygame.K_s]:
            new_direction = (0, 1)

        dx, dy = Direction
        if new_direction !=(-dx,-dy):
            Direction = new_direction

        current_time = pygame.time.get_ticks()
        if current_time - Last_move_time >= Move_delay:
            head_x, head_y = Segments[0]
            dx, dy = Direction
            new_head = (head_x + dx * 20, head_y + dy * 20)
            if new_head in Segments:
                Game_over = True
                print("Game Over","\nScore:",len(Segments)-1)
            Segments.insert(0, new_head)
            if new_head == food:
                food = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)
            else:
                Segments.pop()
            head_x, head_y = Segments[0]
            if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
                Game_over = True
                print("Game Over","\nScore:",len(Segments)-1)
            Last_move_time = current_time

        screen.fill((0,0,0))
        
        Score = pygame.font.SysFont("Arial",30)
        Score_count ="Score: "+  str(len(Segments)-1)
        Point_surface = Score.render(Score_count, True, (255,255,255))
        screen.blit(Point_surface,(20,20))
        pygame.draw.rect(screen, (255,255,255), Border, 2)
        if Game_over == True:
            font = pygame.font.SysFont("Arial", 30, bold=True)
            text = font.render("Game Over", True,(0,0,0), (255,255,255))
            screen.blit(text,(220,160))

        for part in Segments:
            pygame.draw.rect(screen, (0,255,0), (*part,20,20))
        
        pygame.draw.rect(screen,(255,0,0), (*food, 20, 20))

    pygame.display.update()
    Clock.tick(60)


pygame.quit()