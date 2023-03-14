import pygame, sys
from bullet import Bullet
from mobs import Mob
import time

def events(screen, man, bullets):
    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                man.mright = True
                            
            elif event.key == pygame.K_a:
                man.mLeft = True
# Движение вверх вниз для 'man'  (расскоментировать при желании добавить)                     
            # elif event.key == pygame.K_w:
            #     man.mUp = True
                
            # elif event.key == pygame.K_s:
            #     man.mDown = True
                
            
            #space - fire
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, man)
                bullets.add(new_bullet)


        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                man.mright = False
               
            #left
            elif event.key == pygame.K_a:
                man.mLeft = False

# Движение вверх вниз (расскоментировать при желании добавить)             
            # elif event.key == pygame.K_w:
            #     man.mUp = False
                
            # elif event.key == pygame.K_s:
            #     man.mDown = False
            
            

def update(screen, man, background, bullets, mobs, stats, sc):

    background.output()
    sc.show_score()
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    
    man.output()
    mobs.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, mobs, bullets):
    #обновление позиции пули
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, mobs, True, True)
    if collisions:
        for mobs in collisions.values():
            stats.score +=10 * len(mobs)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_health()

    if len(mobs) == 0:
        bullets.empty()
        create_army(screen, mobs)


def man_kill(stats, screen, sc, man, mobs, bullets):
    if stats.mans_health > 0:
        stats.mans_health -=1
        sc.image_health()
        mobs.empty()
        bullets.empty()
        man.create_man()
        create_army(screen, mobs)
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_mobs(stats, screen, sc, man, mobs, bullets):
    mobs.update()
    if pygame.sprite.spritecollideany(man, mobs):
        man_kill(stats, screen,sc, man, mobs, bullets)
    mobs_check(stats, screen, sc, man, mobs, bullets)

def mobs_check(stats, screen, sc, man, mobs, bullets):
    screen_rect = screen.get_rect()

    for mob in mobs.sprites():
        if mob.rect.bottom >= screen_rect.bottom:
            man_kill(stats, screen, sc, man, mobs, bullets)
            break

def create_army(screen, mobs):
    #создание армии мобов
    mob = Mob(screen)
    mob_width = mob.rect.width
    number_mob_x = int((600 - 2 * mob_width ) / mob_width)
    mob_height = mob.rect.height
    number_mob_y = int((750 - 100 - 2 * mob_height) / mob_height)

    for row_number in range(number_mob_y - 6):
        for mob_number in range(number_mob_x):
            mob = Mob(screen)
            mob.x = mob_width  + mob_width  * mob_number
            mob.y = mob_height + mob_height * row_number
            mob.rect.x = mob.x
            mob.rect.y = mob.rect.height + mob.rect.height * row_number
            mobs.add(mob)
            
def check_high_score(stats, sc):
    #проверка новых рекордов
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open ('python_game\highscore.txt','w') as f:
            f.write(str(stats.high_score))