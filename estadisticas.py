class Estadisticas():
    """Seguimiento de las estadisticas de invacion alienigena"""
    def __init__(self, ai_configuraciones):
        """Inicializa las estadisticas"""
        self.ai_configuraciones = ai_configuraciones
        self.reset_stats()
        #inicia invacion alienigena en une stadp activo
        self.game_active = False

    def reset_stats(self):
        """Inicializa estadisticas que pueden cambiar durante el juego"""
        self.naves_restantes = self.ai_configuraciones.cantidad_naves