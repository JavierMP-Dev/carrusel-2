import sys
import pygame
from configuraciones import Configuraciones

from nave import Nave

def run_game():
    #inicializar el juego, las configuraciones y crear un objeto en pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invacion alienigena")

    #crea una nave
    nave = Nave(pantalla)

    #iniciar el bucle principal del juego
    while True: 
        #escuchar eventos de teclado o raton
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Volver a dibujar la pantalla durante cada pasada por el bucle while
        pantalla.fill(ai_configuraciones.bg_color)
        nave.blitme()
        #hacer visible la pntalla dibujada mas reciente
        pygame.display.flip()

run_game()