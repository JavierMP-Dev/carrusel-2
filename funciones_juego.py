import sys 
import pygame
from bala import Bala 
from alien import Alien

def verificar_eventos_keydown(event,ai_configuraciones, pantalla, nave, balas):
    #responde a las pulsaciones de teclas
     if event.key == pygame.K_RIGHT:
        nave.moving_right = True
     elif event.key == pygame.K_LEFT:
        nave.moving_left = True
     elif event.key == pygame.K_SPACE:
         fuego_bala(ai_configuraciones, pantalla, nave, balas)
     elif event.key == pygame.K_q:
         sys.exit()

def verificar_eventos_keyup(event, nave):
    #responde a las pulsaciones de teclas
     if event.key == pygame.K_RIGHT:
        nave.moving_right = False
     elif event.key == pygame.K_LEFT:
        nave.moving_left = False

def verificar_eventos(ai_configuraciones,pantalla, nave, balas):
    #responde a las pulsaciones y teclas y los eventos del raton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("saliendo")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
           verificar_eventos_keydown(event,ai_configuraciones,pantalla, nave, balas)       
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
        

def actualizar_pantalla(ai_configuraciones, pantalla, nave, alien, balas):
    #actualiza las imagenes en la pantalla y pasa a la nueva pantalla
    # Volver a dibujar la pantalla durante cada pasada por el bucle while
    pantalla.fill(ai_configuraciones.bg_color)
    #Vuelve a dibujar todas las balas detras de la nave y de los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    alien.blitme()
    
    #hacer visible la pntalla dibujada mas reciente
    pygame.display.flip()

def update_bala(balas):
    #actualiza la poscion de las balas y elimina las antiguas
    #Actualiza las posciiones de las balas
    balas.update()
    #deshace las balas que han desaparecido
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)    
        

def fuego_bala(ai_configuraciones, pantalla, nave, balas):
    #dispara bala si aun no alcanza el limite
    #crea una bala y agregala al grupo de balas
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones, pantalla, nave)
        balas.add(nueva_bala)