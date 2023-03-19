import pygame, controls, sys
from man import Man
from background import Background  
from pygame.sprite import Group
from stats import Stats
from score import Score


def run():
    pygame.init()
    icon = pygame.image.load('GalaxyShooter\GalaxyShooter\image\icon.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode(( 600, 750 ))
    pygame.display.set_caption("Stars Shooter")

    man = Man(screen)
    background = Background(screen)
    bullets = Group() 
    mobs = Group()
    controls.create_army(screen, mobs)
    stats = Stats()
    sc = Score(screen, stats)

    while True:
        
        controls.events(screen, man, bullets)
        if stats.run_game:
            man.update_man() 
            controls.update(screen, man, background, bullets, mobs, stats, sc)
            controls.update_bullets(screen, stats, sc, mobs, bullets)
            controls.update_mobs(stats, screen, sc, man, mobs, bullets)

run()