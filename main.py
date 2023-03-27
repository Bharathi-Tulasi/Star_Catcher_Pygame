import pygame
import time
import random

pygame.font.init()

width, height = 1240, 700




WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Catcher")

BG = pygame.transform.scale(pygame.image.load("night.jpg"), (width, height))
star_img = pygame.image.load("star1.png")


pygame.mixer.init()
pygame.mixer.music.load("music_star_catcher.wav")
pygame.mixer.music.play()

catcher1_width = 200
catcher1_height = 10
catcher1_vel = 5




star_width = 60
star_height = 60
star_vel = 3
font = pygame.font.SysFont("comicsans", 30)



def draw(catcher1, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    time_text = font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    
    
    pygame.draw.rect(WIN, "white", catcher1)
    
    
    for i in stars:
        WIN.blit(star_img, i)
    

    pygame.display.update()
    

def main():
    run = True

    
    catcher1 = pygame.Rect(200, height - catcher1_height, catcher1_width, catcher1_height)
    

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    stars_increment = 1000
    star_count = 0

    stars = []

    catcher1_collect_count = 0
    

    collected_120_text = True
   
    time_up = False


    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > stars_increment:
            for _ in range(3):
                
                star_x = random.randint(0 , width - star_width)
                star = pygame.Rect(star_x, -star_height,
                                   star_width, star_height)
                stars.append(star)
                
                    
                
            stars_increment = max(500, stars_increment - 30)
            star_count = 0



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (catcher1.x - catcher1_vel) >= 0:
            catcher1.x -= catcher1_vel
        if keys[pygame.K_RIGHT] and (catcher1.x + catcher1_vel + catcher1_width) <= width:
            catcher1.x += catcher1_vel
            
        for star in stars[:]:
            star.y += star_vel
            if star.y > height:
                stars.remove(star)
            elif star.y + star_height >= catcher1.y and star.colliderect(catcher1):
                stars.remove(star)
                
                catcher1_collect_count = catcher1_collect_count + 1
            
                collected_120_text = True
                time_up = True
                break

        if time_up:
            time_up_time = round(elapsed_time)
            
            if catcher1_collect_count  == 120 and time_up_time <= 61 and collected_120_text:

                collected_120_text = font.render("Collected 120! You got another 60 seconds to play", 1, "white")
                WIN.blit(collected_120_text, (width/2 - collected_120_text.get_width()/2, height/2 - collected_120_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(2000)
                
                if time_up_time == 62:
                    collected_120_text = False

            elif time_up_time == 121:
                timeup_text = font.render("Time Up!", 1, "white")
                WIN.blit(timeup_text, (width/2 - timeup_text.get_width()/2, height/2 - timeup_text.get_height()/2))
                
                
                pygame.time.delay(4000)

                catcher1_collect_count_text = font.render(f"Stars Collected: {catcher1_collect_count}", 1, "white")
                WIN.blit(catcher1_collect_count_text, (width/2 - catcher1_collect_count_text.get_width()/2, height/2 - (catcher1_collect_count_text.get_height()/2 - 30)))

                


            
                pygame.display.update()
                pygame.time.delay(5000)



                break

            elif time_up_time == 61 and catcher1_collect_count < 120:
                

                timeup_text = font.render("Time Up!", 1, "white")
                WIN.blit(timeup_text, (width/2 - timeup_text.get_width()/2, height/2 - timeup_text.get_height()/2))
                
                
                pygame.time.delay(4000)

                catcher1_collect_count_text = font.render(f"Stars Collected: {catcher1_collect_count}", 1, "white")
                WIN.blit(catcher1_collect_count_text, (width/2 - catcher1_collect_count_text.get_width()/2, height/2 - (catcher1_collect_count_text.get_height()/2 - 30)))

                


            
                pygame.display.update()
                pygame.time.delay(5000)
                break
            
            

        
        
            




        draw(catcher1, elapsed_time, stars)
    pygame.quit()

if __name__ == "__main__":
    main()