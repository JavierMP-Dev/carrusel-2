import pygame

from pygame.sprite import Group
from configuraciones import Configuraciones
from estadisticas import Estadisticas
from button import Button
from nave import Nave
import funciones_juego as fj

def run_game():
    #inicializar el juego, las configuraciones y crear un objeto en pantalla
    pygame.init()
    ai_configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode((ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    pygame.display.set_caption("Invacion alienigena")

    #crea el boton play
    play_button = Button(ai_configuraciones, pantalla, "Play")
    

    #crea una instancia para almacernar estadisticas de juego
    estadisticas = Estadisticas(ai_configuraciones)

    #crea una nave, un grupo de balas y un grupo de aliens
    nave = Nave(ai_configuraciones, pantalla)
    balas = Group()
    aliens = Group()
    
    # Crea la flota de alienigenas
    fj.crear_flota(ai_configuraciones, pantalla,nave, aliens)

    #iniciar el bucle principal del juego
    while True: 
        #escuchar eventos de teclado o raton
        fj.verificar_eventos(ai_configuraciones,pantalla,estadisticas, play_button, nave, balas)
            #se llama a la funcion verificar que esta en funciones_juego 
        if estadisticas.game_active:
            nave.update() #se llama a la funcion update que esta en la clase nave
            #funcion actualizar balas
            fj.update_balas(ai_configuraciones,pantalla, nave, aliens, balas)
            fj.update_aliens(ai_configuraciones,estadisticas,pantalla, aliens,nave,balas)
            
        fj.actualizar_pantalla(ai_configuraciones, pantalla,estadisticas, nave, aliens, balas, play_button)

run_game()