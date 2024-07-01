import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #sirve para representar a un solo alienigena en la flota
    def __init__(self,ai_configuraciones,pantalla):
        """inicializa el aieny establece su posciion inicial"""
        super(Alien, self).__init__()
        
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        #carga la imagen del alien y establece su atributo rect
        self.image = pygame.image.load("img/alien.bmp")
        self.rect = self.image.get_rect()

        #inicia cada nuevo alien cerca de la parte superior izquierda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #almacena la posicion exacta del alien
        self.x = float(self.rect.x)

    def blitme(self):
        #dibuja el alien en su ubicacion actual
        self.pantalla.blit(self.imagen,self.rect)

    def update(self):
        #mueve el alien a la derecha
        self.x += self.ai_configuraciones.alien_speed_factor
        self.rect.x = self.x

