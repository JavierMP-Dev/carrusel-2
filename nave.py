import pygame

class Nave():
    #sirbe para gestionar el comportamiento de la nave
    def __init__(self, pantalla):
        #inicializa la nave y establece su posicion de partida
        self.pantalla = pantalla

        #carga la imagen de la nave y obtiene su rect
        self.imagen = pygame.image.load("img/nave.png")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        #eempieza cad nueva nave en la parte infierior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom

    def blitme(self):
        #dibuja la nave en su posicion actual
        self.pantalla.blit(self.imagen, self.rect)
        