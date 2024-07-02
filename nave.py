import pygame

class Nave():
    #sirbe para gestionar el comportamiento de la nave
    def __init__(self,ai_configuraciones, pantalla):
        #inicializa la nave y establece su posicion de partida
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        #carga la imagen de la nave y obtiene su rect
        self.imagen = pygame.image.load("img/nave.png")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        #eempieza cad nueva nave en la parte infierior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom

        #almacena un valor decimal para e centro de la nave
        self.center = float(self.rect.centerx)

        #bandera de movimientoo
        self.moving_right = False 
        self.moving_left = False

    def update(self):
        #actualiza la posicion de la nave segun las banderas de movimiento
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_configuraciones.factor_velocidad_nave

        if self.moving_left and self.rect.left > 0:
            self.center -=self.ai_configuraciones.factor_velocidad_nave

        #actualiza el objeto rect desde self.center
        self.rect.centerx = self.center

    def blitme(self):
        #dibuja la nave en su posicion actual
        self.pantalla.blit(self.imagen, self.rect)
        
    def centrar_nave(self):
        """centra la nave en la pantalla"""
        self.center = self.pantalla_rect.centerx