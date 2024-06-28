class Configuraciones():
    #esta clase almacena las configuraciones del juego
    def __init__(self):
        #inicializa las configuraciones del juego
       

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #configuraciones de la nave
        self.factor_velocidad_nave = 1.2

        #configuraciones de balas
        self.bala_factor_velocidad = 1
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 60, 60, 60
        self.balas_allowed = 3