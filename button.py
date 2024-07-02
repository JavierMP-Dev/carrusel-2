import pygame.font

class Button():
    """Clase para botones"""
    def __init__(self, ai_configuraciones, pantalla, msg):
        """INicializa los atributos"""
        self.pantalla = pantalla
        self.pantalla_rect = pantalla.get_rect()
        
        #establece las dimenasiones y propiedades del boton
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #construye el objeto rect del boton y lo centra
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.pantalla.rect.center
        
        #el mensaje del boton debe prepararse una sola vez
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        """Convierte el mensaje en una imagen renderizada y centra el texto en e boton"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center