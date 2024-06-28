import pygame

from pygame.sprite import Group
from configuraciones import Configuraciones
from nave import Nave
from alien import Alien
import funciones_juego as fj

def run_game():
    #inicializar el juego, las configuraciones y crear un objeto en pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invacion alienigena")

    #crea una nave
    nave = Nave(ai_configuraciones, pantalla)
    #crea un grupo para almacenar las balas
    balas = Group()
    #aqui crea un alien
    alien = Alien(ai_configuraciones, pantalla)
  
    #iniciar el bucle principal del juego
    while True: 
        #escuchar eventos de teclado o raton
        fj.verificar_eventos(ai_configuraciones,pantalla, nave, balas) #se llama a la funcion verificar que esta en funciones_juego 
        nave.update() #se llama a la funcion update que esta en la clase nave
        
        #funcion actualizar balas
        fj.update_bala(balas)

        #funcion llamada desde otro script
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave, alien, balas)

run_game()